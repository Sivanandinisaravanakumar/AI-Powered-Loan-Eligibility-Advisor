# **🏦 AI-Powered Loan Eligibility Advisor**

Empowering smarter financial decisions with artificial intelligence

An end-to-end ML-powered web application that predicts loan eligibility, guides users through a smart chatbot, and ensures secure authentication — built as part of my AI Internship Project at Infosys Springboard.

**🚀 Overview

AI-Powered Loan Eligibility Advisor is an intelligent machine learning system that predicts whether a loan applicant is eligible based on key financial and demographic factors. It uses logistic regression, decision trees, and an interactive chatbot to provide actionable advice — even for rejected applications.

This project includes:
✔ A Flask-based responsive web interface
✔ ML model trained on a rich financial dataset
✔ Firebase-secured login & registration
✔ Smart chatbot guidance for next-step recommendations

Designed to support real-world bank workflows with accuracy, transparency, and fairness.

✨ Key Features
📊 AI-Powered Prediction

Predicts loan approval using 14+ input features via Logistic Regression & Decision Tree models.

🤖 Smart Chatbot

Interactive assistant that:

Collects user data through 11 questions

Explains eligibility results

Suggests financial improvements

Provides document checklists & next steps

🔐 Secure Authentication

Login & registration powered by Firebase Authentication, with email-password sign-in.

📈 Actionable Insights

Gives personalized advice for both:

Eligible users → documentation, timelines

Ineligible users → credit score, income, property area improvements

🌐 Responsive Web UI

Built using Flask + HTML + CSS + JavaScript.

🛠️ Tech Stack
Layer	Technologies
Backend	Python, Flask
Machine Learning	Scikit-learn (Logistic Regression, Decision Tree)
Frontend	HTML5, CSS3, JavaScript
Authentication	Firebase Authentication
Data	train.csv, test.csv (Kaggle-style dataset)
Model Persistence	Pickle (model.pkl)
Deployment	Local Flask server (cloud-ready)
📂 Project Structure
AI-Powered-Loan-Eligibility-Advisor/
│── Flask_app.py                # Main application logic
│── model.pkl                   # Trained ML model
│── train.csv                   # Training dataset
│── test.csv                    # Test dataset
│── loan.png                    # Project activity image
│── system_architecture.png     # System architecture diagram
│── chatbot.py                  # Chatbot module (optional)
│── Streamlit_app.py            # Streamlit version
│── Streamlitbasics.py          # Utilities for Streamlit
│── Eligibility Prediction.ipynb# ML training notebook
│
├── static/                     # CSS, JS, images
├── templates/                  # HTML templates
│   ├── home.html
│   ├── login_firebase.html
│   ├── register_firebase.html
│   ├── predictpage.html
│   ├── prediction.html
│   ├── chatbot.html
│   └── about.html
│
├── Agile_Doc.xlsx              # Agile sprint planning
├── Defect_Tracker.xlsx         # Bug tracking sheet
├── Unit_Test_Plan.xlsx         # Testing documentation
│
├── .gitignore                  # Excludes private keys
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation


🔐 Note: firebase-adminsdk.json must be generated manually from the Firebase Console.
It is intentionally excluded from GitHub for security.

📥 Installation & Setup
Prerequisites

Python ≥ 3.8

Git

Steps
1️⃣ Clone the repository
git clone https://github.com/Sivanandinisaravanakumar/AI-Powered-Loan-Eligibility-Advisor.git
cd AI-Powered-Loan-Eligibility-Advisor

2️⃣ Install dependencies
pip install flask numpy scikit-learn firebase-admin

3️⃣ Configure Firebase Authentication

Go to Firebase Console → Project Settings → Service Accounts

Generate a new serviceAccountKey.json

Place it in the project root

Enable Email/Password authentication

4️⃣ Run the application
python Flask_app.py


Visit: http://localhost:5000

🧪 How It Works

User logs in or registers through Firebase.

Navigates to the Prediction page or Chatbot.

Fills out a detailed loan form → ML model predicts eligibility.

Chatbot asks 11 questions → provides tailored advice.

Users get:

Eligible → documentation checklist + timeline

Not eligible → income/credit improvement plan

📊 Sample Outputs
✅ Eligible Result

🎉 You are ELIGIBLE for the loan!

Next Steps:

Prepare ID, Address, Income proof

Submit documents via bank portal

Expected disbursement: 10–15 business days

Maintain credit score > 750

❌ Not Eligible Result

You are NOT eligible for the loan.

Improvement Plan:

Increase income to ₹35,000+

Improve credit score from 620 → 700+

Reduce loan amount to ₹4.5L or below

Consider a co-applicant or alternative loan types

📜 License

Licensed under the MIT License. See LICENSE for details.

👥 Author

Sivanandini Saravanakumar
AI Intern | Infosys Springboard
📧 sivanandini.sk@gmail.com
