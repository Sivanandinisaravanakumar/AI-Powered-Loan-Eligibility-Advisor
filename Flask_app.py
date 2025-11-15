from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("C:\\Users\\sivan\\Downloads\\AI-Powered-Loan-Eligibility-Advisor\\model.pkl", "rb"))

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Predict Page (form page)
@app.route('/predictpage')
def predictpage():
    return render_template("index.html")

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("C:\\Users\\sivan\\Downloads\\AI-Powered-Loan-Eligibility-Advisor\\model.pkl", "rb"))

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Predict Page (form page)
@app.route('/predictpage')
def predictpage():
    return render_template("index.html")

@app.route('/predict', methods = ["GET","POST"]) #get - typically used to show a blank prediction page or result page. #post-used to submit the form with input values that the server uses to make a prediction.
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
        return render_template("prediction.html",prediction_text="loan status is {}".format(prediction))
    else:
        return render_template("prediction.html")
    
# About Page
@app.route('/about')
def about():
    return render_template("about.html")

# Chatbot Page
@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

#Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ✅ Replace with your actual authentication logic
        if username == "admin" and password == "1234":
            return render_template("home.html")  # redirect to home or dashboard
        else:
            return render_template("login.html", error="Invalid credentials. Please try again.")
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)

