# 🏦 AI-Powered Loan Eligibility Advisor

> *Empowering smarter financial decisions with artificial intelligence.*

![Project Banner](https://github.com/Sivanandinisaravanakumar/AI-Powered-Loan-Eligibility-Advisor/blob/main/static/loann.png)  

---

## 🚀 Overview

**AI-Powered Loan Eligibility Advisor** is an intelligent machine learning-based system designed to predict an applicant’s loan approval eligibility using key financial and personal information — including income, credit history, education, employment status, and property area. The project leverages AI to assist banks and financial institutions in automating loan decisions with improved accuracy and fairness.

Built as part of my **AI Internship Project at Infosys Springboard**, this end-to-end solution combines a Flask web interface, a trained ML model, interactive chatbot guidance, and secure user authentication — delivering a complete, production-ready tool for real-world lending scenarios.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| **📊 AI-Powered Prediction** | Uses Logistic Regression & Decision Tree models to analyze 14+ features for accurate approval/rejection predictions. |
| **🤖 Smart Chatbot** | Engages users in natural language to explain results, provide improvement tips, and guide them through the process — even for rejected applications. |
| **🔐 Secure Authentication** | Firebase-powered login and registration with session management. |
| **📈 Actionable Insights** | Provides personalized next steps for both eligible and ineligible applicants — turning predictions into actionable financial advice. |
| **🌐 Web-Based Interface** | Clean, responsive UI built with Flask, HTML, CSS, and JavaScript — accessible from any device. |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, Flask |
| **ML Model** | Scikit-learn (Logistic Regression, Decision Trees) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Authentication** | Firebase Authentication (Email/Password) |
| **Data** | `train.csv`, `test.csv` (Kaggle-style dataset) |
| **Model Persistence** | Pickle (`model.pkl`) |
| **Deployment** | Local Server (Flask), Ready for Cloud |

---

## 📂 Project Structure

AI-Powered-Loan-Eligibility-Advisor/
│
├── Flask_app.py # Main application logic and routes
├── model.pkl # Trained ML model (saved via pickle)
├── train.csv # Training dataset
├── test.csv # Testing dataset
├── loan.png # Project activity flow image
├── system_architecture.png # System architecture diagram
│
├── pycache/ # Python cache (auto-generated)
├── static/ # Static assets (CSS, JS, images)
├── templates/ # HTML templates
│ ├── home.html # Landing page (after login)
│ ├── login_firebase.html # Firebase-authenticated login
│ ├── register_firebase.html # User registration form
│ ├── predictpage.html # Loan application form
│ ├── prediction.html # Prediction result display
│ ├── chatbot.html # Interactive AI assistant
│ └── about.html # Project details
│
├── chatbot.py # Chatbot logic (if separate)
├── Streamlit_app.py # Streamlit version (if applicable)
├── Streamlitbasics.py # Streamlit utilities
├── Eligibility Prediction.ipynb # Jupyter notebook for model training
│
├── Agile_Doc.xlsx # Agile documentation
├── Defect_Tracker.xlsx # Defect tracking sheet
├── Unit_Test_Plan.xlsx # Unit test plan
├── Project Activity.png # Project activity flow
│
├── .gitignore # Ignores sensitive files (e.g., serviceAccountKey.json)
├── README.md # This file
└── requirements.txt # Python dependencies


> 💡 **Note**: *`firebase-adminsdk.json` is intentionally excluded from version control for security. Developers must generate their own from the Firebase Console.*

---

## 📥 Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### Steps

1. **Clone the repository**
   
    git clone https://github.com/Sivanandinisaravanakumar/AI-Powered-Loan-Eligibility-Advisor.git
   
    cd AI-Powered-Loan-Eligibility-Advisor

3. **Install dependencies**

   *pip install flask numpy scikit-learn firebase-admin*

4. **Set up Firebase Authentication**
   
   Go to Firebase Console
   
   Create a new project or select existing
   
   Enable Email/Password sign-in method
   
   Download firebase-adminsdk.json from Project Settings > Service Accounts
   
   Place it in the project root folder (do NOT commit to GitHub)

6. **Google Gemini API Setup**

   Open Google AI Studio

   Generate an API Key

   Create a .env file:

     *GEMINI_API_KEY=YOUR_API_KEY_HERE*

7. **Run the application**
   
    *python Flask_app.py*

8. **Open your browser and visit:**
   
   (http://127.0.0.1:5000)

9. **Register a new account via the "Sign Up"**
   
---

### 🧠 Machine Learning Model Info

The ML model (model.pkl) is trained in:

   *Eligibility Prediction.ipynb*

Steps Performed:

  1. Data cleaning

  2. Handling missing values

  3. Encoding categorical variables

  4. Log-transforming skewed columns

  5. Training Decision Tree model

  6. Saving model with pickle

Used in:

  ✔ Loan Prediction Form

  ✔ Smart Chatbot Advisor

---

### 🏛️ System Architecture

**Chatbot Flow**

 1. User logs in

 2. Chatbot asks 11 financial questions

 3. Flask preprocesses user responses

 4. model.pkl predicts Eligible / Not Eligible

 5. Gemini generates explanation

 6. User receives final recommendation

---
   
### 📊 Sample Output

✅ **Eligible Result:**
🎉 You are ELIGIBLE for the Loan!
 Next Steps: 
  - Prepare ID, Address, and Income Proof
  - Submit via bank portal
  - Estimated disbursement: 10–15 business days
  
💡 *Tip: Maintain credit score above 750 during this process.*


❌ **Not Eligible Result:**
❌ You are NOT eligible for the loan.
 Improvement Plan: 

  - Increase combined income to ₹35,000+
  - Improve credit score from 620 to 700+ by paying bills on time
  - Reduce loan amount to ₹4.5L or below
    
💡 *Try: Apply for a personal loan or consider a co-applicant*

---

### 📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

---

### 👥 Author
Sivanandini Saravanakumar

AI Intern | Infosys Springboard

Email: sivanandini.sk@gmail.com   |
[🔗 LinkedIn ](https://www.linkedin.com/in/sivanandini-saravanakumar-313287259/)  | 
[🔗 GitHub ](https://github.com/Sivanandinisaravanakumar)
 
