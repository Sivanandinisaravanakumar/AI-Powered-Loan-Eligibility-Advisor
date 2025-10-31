import streamlit as st
import pickle
import numpy as np
from chatbot import show_chatbot

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit Layout for Home Page
def home_page():
    st.title("🚀 Loan Prediction System")
    st.markdown("### 📋 **Welcome to the Loan Prediction System!**")
    st.markdown("""This tool helps you predict whether your loan application will be approved or rejected based on a variety of personal and financial factors. Fill in your details and let the system predict your loan status with an accurate machine learning model.""")

    # Add an image to the home page
    st.image("loan.png", caption="Loan Prediction System")

    st.markdown("### 🛠️ Project Overview")
    st.markdown("""
        This project was developed as part of my **AI internship** at **Infosys Springboard**. The objective was to build a **Loan Prediction System** that uses machine learning to predict whether a loan application will be approved or rejected based on various parameters like personal and financial details of the applicant.
        The system takes the user's input and processes it through a pre-trained model to deliver a prediction about the loan status. We used algorithms like **Logistic Regression** and **Decision Trees** for accurate predictions.
    """)

# Streamlit Layout for About Us Page
def about_us_page():
    st.title("📖 About Us")
    st.markdown("""**Our Mission**: We aim to provide **innovative, efficient, and easy-to-use** financial tools that 
                assist individuals in making better financial decisions. Our mission is to simplify 
                complex loan application processes using advanced technology like **Machine Learning** and **AI**.""")

    # System Architecture Section
    st.markdown("### 🏗️ System Architecture")
    st.markdown("""
        The **Loan Prediction System** architecture is designed to seamlessly collect user inputs, process them through a machine learning model, and deliver accurate predictions for loan approval. Here's a breakdown of the system components:
        
        1. **User Interface (UI)**: The front-end interface built using **Streamlit** allows users to input their personal and financial information.
        2. **Data Preprocessing**: Data entered by users is cleaned and transformed into numerical values, ensuring compatibility with the machine learning model.
        3. **Machine Learning Model**: The core of the system is a trained model (e.g., Random Forest, Logistic Regression), which predicts the likelihood of loan approval based on historical data.
        4. **Prediction Engine**: The system runs the model on the preprocessed data and returns the loan approval decision.
        5. **Visualization & Output**: The result is displayed to the user in a clear format with feedback on whether the loan is likely to be approved or rejected.
        
        Below is a diagram of the system architecture for better understanding:
    """)

    # Image of System Architecture
    st.image("system_architecture.png", caption="System Architecture Diagram")

    # Activity Log Section
    st.markdown("### 📊 Project Activity Log")
    st.markdown("""
        Throughout my internship, I engaged in various key activities to contribute to the **Loan Prediction System** project:
        
        1. **Data Collection**: Gathered relevant data from past loan applicants, including financial history, loan amounts, and approval outcomes.
        2. **Data Cleaning**: Handled missing values, outliers, and transformed categorical data to ensure compatibility with machine learning algorithms.
        3. **Model Selection**: Experimented with various machine learning algorithms such as **Logistic Regression**, **Random Forest**, and **XGBoost** to find the best-performing model.
        4. **Model Training & Optimization**: Trained the model on historical data, fine-tuned hyperparameters, and evaluated performance metrics like **accuracy**, **precision**, and **recall**.
        5. **Deployment & Testing**: Deployed 
        the trained model into the Streamlit application, tested the prediction system with real user inputs, and optimized its performance.

        This project has provided me with hands-on experience in **data preprocessing**, **model training**, and **AI deployment**, which are essential skills for any AI professional.
    """)

    # Project Activity Image
    st.image("Project Activity.png", caption="Project Activity Diagram")

# Streamlit Layout for Prediction Page
def prediction_page():
    st.title("🚀 Loan Prediction System")
    st.markdown("### 📋 Enter Loan Application Details to Predict Your Loan Status!")

    # User input fields for prediction
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    married = st.selectbox("💍 Marital Status", ["Yes", "No"])
    dependents = st.selectbox("👨‍👩‍👧 Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("🎓 Education", ["Graduate", "Not Graduate"])
    employed = st.selectbox("💼 Self Employed", ["Yes", "No"])
    credit = st.slider("📊 Credit score", min_value=300, max_value=850, step=1, value=750)
    area = st.selectbox("🏠 Property Area", ["Urban", "Semiurban", "Rural"])
    ApplicantIncome = st.slider("💰 Applicant Income", min_value=1000, max_value=100000, step=1000, value=5000)
    CoapplicantIncome = st.slider("🤝 Coapplicant Income", min_value=0, max_value=100000, step=1000, value=0)
    LoanAmount = st.slider("🏦 Loan Amount", min_value=1, max_value=100000, step=10, value=100)
    Loan_Amount_Term = st.select_slider("📅 Loan Amount Term (in days)", options=[360, 180, 240, 120], value=360)

    # Preprocess input data and make predictions
    def preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term):
        male = 1 if gender == "Male" else 0
        married_yes = 1 if married == "Yes" else 0
        if dependents == '1':
            dependents_1, dependents_2, dependents_3 = 1, 0, 0
        elif dependents == '2':
            dependents_1, dependents_2, dependents_3 = 0, 1, 0
        elif dependents == "3+":
            dependents_1, dependents_2, dependents_3 = 0, 0, 1
        else:
            dependents_1, dependents_2, dependents_3 = 0, 0, 0

        not_graduate = 1 if education == "Not Graduate" else 0
        employed_yes = 1 if employed == "Yes" else 0
        semiurban = 1 if area == "Semiurban" else 0
        urban = 1 if area == "Urban" else 0

        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome + CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)
        if credit <= 1000 and credit >= 800:
            credit = 1
        else :
            credit = 0
            

        return [
            credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog, totalincomelog,
            male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban
        ]

    if st.button("🔮 Predict Loan Status"):
        features = preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term)

        # Prediction
        prediction = model.predict([features])

        # Convert prediction to human-readable format
        if prediction == "N":
            prediction = "No"
            st.error("⚠️ Loan Status: **Rejected**")
            st.markdown("### ☠️ Danger! Your loan application has been **rejected**.")
            st.markdown("""
            **Possible reasons:**
            - Low credit history score
            - Insufficient income for the loan amount requested
            - High debt-to-income ratio
            - Other potential risk factors

            **Critical suggestions:**
            - **Immediate action:** Improve your credit score by paying off existing debts.
            - Consider **reducing your loan amount** or opting for a longer repayment term.
            - **Reassess your finances** and improve your overall financial health before reapplying.

            *Take care to address these issues before trying again!*
            """)
        else:
            prediction = "Yes"
            st.success("✅ Loan Status: **Approved**")
            st.markdown("### 🎉 Congratulations! Your loan application is likely approved!")
            st.balloons()
            st.markdown("""
            **Key highlights of your application:**
            - Good credit history score
            - Sufficient income to cover loan repayment
            - Positive factors supporting your loan approval

            Enjoy your financial journey with the new loan!
            """)
def show_chatbot_page():
    # Link the chatbot to the chatbot page
    show_chatbot()

# Footer for About Us Page
def footer():
    st.markdown("---")
    st.markdown("### 🌐 Connect with us")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/sivanandini-saravanakumar-313287259/)")
    st.markdown("[GitHub](https://github.com/Sivanandinisaravanakumar )")
    st.markdown("📧 Email: sivanandini.sk@gmail.com")

# Sidebar Layout Design Enhancement
def sidebar_layout():
    st.sidebar.title("🔧 Menu")
    st.sidebar.markdown("### Choose a Page")
    
    menu = st.sidebar.radio(
        "Go to", ["Home", "About Us", "Prediction", "Chatbot"]
    )
    
    if menu == "Home":
        home_page()
    elif menu == "Prediction":
        prediction_page()
    elif menu == "Chatbot":
        show_chatbot_page()
    else:
        about_us_page()
        footer()

# Set initial page state if not defined
sidebar_layout()
