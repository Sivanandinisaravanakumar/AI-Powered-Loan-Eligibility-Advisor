from flask import Flask, render_template, request, redirect, url_for, session, flash
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = 'd4eb319ea84fecef9f8e3bb6fc11a2852a5f26eea6fe569a3042355c67676421'

# Load your model
model = pickle.load(open("C:\\Users\\sivan\\Downloads\\AI-Powered-Loan-Eligibility-Advisor\\model.pkl", "rb"))

# --- USER MANAGEMENT ---
# Dictionary to store users (username -> password)
# In a real app, use a database and hash passwords!
USERS = {
    'admin': '54321' #  existing admin user
}

def login_required(f):
    """
    Decorator to require login for routes
    """
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if user exists and password matches
        if username in USERS and USERS[username] == password:
            session['username'] = username
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template("login.html", error="Invalid credentials. Please try again.")
    
    return render_template("login.html")

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Validation checks
        if not username or not password:
            return render_template("register.html", error="Username and password are required.")
        
        if password != confirm_password:
            return render_template("register.html", error="Passwords do not match.")
        
        if len(password) < 6:
            return render_template("register.html", error="Password must be at least 6 characters long.")
        
        if username in USERS:
            return render_template("register.html", error="Username already exists. Please choose another one.")
        
        # Add user to the dictionary
        USERS[username] = password
        # You could also add a success message here
        return render_template("register.html", success="Registration successful! You can now log in.")
    
    # If GET request, just show the registration form
    return render_template("register.html")


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
    # Make the app accessible via IP address
    app.run(debug=True, host='0.0.0.0') # Add host='0.0.0.0' to access via IP