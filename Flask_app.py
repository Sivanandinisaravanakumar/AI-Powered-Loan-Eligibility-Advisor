import firebase_admin
from firebase_admin import credentials, auth
import flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
import numpy as np
import pickle

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\sivan\\Downloads\\firebase-adminsdk.json") # Update path
firebase_admin.initialize_app(cred)

app = Flask(__name__)
app.secret_key = 'd4eb319ea84fecef9f8e3bb6fc11a2852a5f26eea6fe569a3042355c67676421'

# Load your model (assuming it's still in the same place)
model = pickle.load(open("C:\\Users\\sivan\\Downloads\\AI-Powered-Loan-Eligibility-Advisor\\model.pkl", "rb"))

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in via Firebase token in session
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))
        try:
            # Verify the user ID stored in session against Firebase
            user = auth.get_user(user_id)
        except auth.UserNotFoundError:
            # If user doesn't exist in Firebase, clear session and redirect to login
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Login Page - This will now render a page that handles Firebase login via JS
@app.route('/login')
def login():
    return render_template("login_firebase.html") # You'll create this

# Register Page - This will now render a page that handles Firebase registration via JS
@app.route('/register')
def register():
    return render_template("register_firebase.html") # You'll create this

# Callback route to handle successful Firebase login (receives token from frontend JS)
@app.route('/firebase-login-callback', methods=['POST'])
def firebase_login_callback():
    id_token = request.json.get('id_token') # Token received from frontend JS
    try:
        # Verify the ID token received from the frontend
        decoded_claims = auth.verify_id_token(id_token)
        uid = decoded_claims['uid']
        # Store user ID in session (you can store other claims if needed)
        session['user_id'] = uid
        session['logged_in'] = True
        # Redirect to home or dashboard after successful login
        return flask.jsonify({"status": "success", "redirect_url": url_for('home')})
    except auth.InvalidIdTokenError:
        # Handle invalid token
        return flask.jsonify({"status": "error", "message": "Invalid token"}), 401
    except Exception as e:
        # Handle other errors
        print(f"Login error: {e}")
        return flask.jsonify({"status": "error", "message": "Login failed"}), 500

#LOGOUT PAGE
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """Logout route - clears session and redirects to login"""
    session.clear()
    return redirect(url_for('login'))

# Home Page - Protected
@app.route('/')
@login_required
def home():
    return render_template("home.html")

# Predict Page (form page) - Protected
@app.route('/predictpage')
@login_required
def predictpage():
    return render_template("index.html")

# Predict Route (handles form submission and chatbot API call) - Protected
@app.route('/predict', methods = ["GET","POST"])
@login_required
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit  = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome']) #25000-> 0,1
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])


        #gender
        if (gender == "Male"):
            male = 1
        else:
            male = 0
        
        #married
        if (married == "Yes"):
            married_yes = 1
        else:
            married_yes = 0
        
        #dependents
        if ( dependents == '1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif dependents == '2':
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif dependents == '3+':
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0

        #education 
        if education =="Not Graduate":
            not_graduate = 1
        else:
            not_graduate = 0

        #employed
        if (employed == "Yes"):
            employed_yes = 1
        else:
            employed_yes = 0
        
        #property area
        if area == "Semiurban":
            semiurban = 1
            urban = 0
        elif area == "Urban":
            semiurban = 0
            urban = 1
        else:
            semiurban = 0
            urban = 0

        ApplicantIncomeLog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountLog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        prediction = model.predict([[credit,ApplicantIncomeLog,LoanAmountLog,Loan_Amount_Termlog,totalincomelog,male,married_yes,dependents_1,dependents_2,dependents_3,not_graduate,employed_yes,semiurban,urban]])
        
        #print(prediction)
        if(prediction=="N"):
            prediction = "No"
        else:
            prediction = "Yes"
        # Check if the request is likely coming from the chatbot (e.g., AJAX)
        if request.headers.get('Accept') == 'application/json' or request.is_json:
            # Return JSON for chatbot
            return {"status": "success", "result": prediction, "message": f"Loan status is {prediction}"}
        else:
            # Return HTML for the form submission
            return render_template("prediction.html", prediction_text="loan status is {}".format(prediction))
    else:
        # GET request - show the form page (prediction.html or index.html)
        return render_template("prediction.html") # Or index.html if that's your form
    
# About Page - Protected
@app.route('/about')
@login_required
def about():
    return render_template("about.html")

# Chatbot Page - Protected
@app.route('/chatbot')
@login_required
def chatbot():
    return render_template("chatbot.html")

if __name__ == '__main__':
    app.run(debug=True)