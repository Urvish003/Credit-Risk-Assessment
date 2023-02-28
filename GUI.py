import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib
import warnings
warnings.filterwarnings("ignore")


# Load the pre-trained model
model = joblib.load('model.joblib')


# Define a function to make predictions
def predict_loan_risk(age, income, emp_length, loan_amnt, loan_int_rate, loan_status, cb_person_cred_hist_length,
                      mortgage, other, own, rent, debtconsolidation, education, homeimprovement, medical, personal,
                      venture):
    # Create a dataframe with the user input data
    data = pd.DataFrame({
        'person_age': [age],
        'person_income': [income],
        'person_emp_length': [emp_length],
        'loan_amnt': [loan_amnt],
        'loan_int_rate': [loan_int_rate],
        'loan_status': [loan_status],
        'loan_percent_income': [loan_amnt / income],
        'cb_person_cred_hist_length': [cb_person_cred_hist_length],
        'MORTGAGE': [mortgage],
        'OTHER': [other],
        'OWN': [own],
        'RENT': [rent],
        'DEBTCONSOLIDATION': [debtconsolidation],
        'EDUCATION': [education],
        'HOMEIMPROVEMENT': [homeimprovement],
        'MEDICAL': [medical],
        'PERSONAL': [personal],
        'VENTURE': [venture]
    })

    # Make the prediction
    pred = model.predict(data)

    # Return the prediction
    return pred[0]



 # Set the app title
st.title('Credit Risk Analysis')

# Get the user input
age = st.slider('Enter your age:', 18, 55)
income = st.number_input('Enter your income:', min_value=0)
emp_length = st.slider('Enter your employment length:', 0, 50)
loan_amnt = st.number_input('Enter the loan amount:', min_value=0)
loan_int_rate = st.slider('Enter the interest rate:', 5.0, 50.0)
loan_status = st.radio('Enter your current loan status:', ['Non-Active', 'Active'])
a=0
if income>0:
    a = loan_amnt / income
    st.write('loan_percent_income: {:.2f} '.format(a))
if loan_status == 'Non-Active':
    loan_status = 0
else:
    loan_status = 1
cb_person_cred_hist_length = st.slider('Enter the credit account age:', 0, 60)
# House ownership information
st.subheader('House ownership')
col1, col2, col3, col4 = st.columns(4)
mortgage = col1.radio('Mortgage', ['No', 'Yes'])
other = col2.radio('Other', ['Yes', 'No'])
own = col3.radio('Own', ['Yes', 'No'])
rent = col4.radio('Rent', ['Yes', 'No'])

# Purpose of loan information
st.subheader('Purpose of loan')
col1, col2, col3, col4, col5, col6 = st.columns(6)
debtconsolidation = col1.radio('Debt Consolidation', ['Yes', 'No'])
education = col2.radio('Education', ['Yes', 'No'])
homeimprovement = col3.radio('Home Improvement', ['Yes', 'No'])
medical = col4.radio('Medical', ['Yes', 'No'])
personal = col5.radio('Personal', ['Yes', 'No'])
venture = col6.radio('Venture', ['Yes', 'No'])


data = pd.DataFrame({
    'person_age': [age],
    'person_income': [income],
    'person_emp_length': [emp_length],
    'loan_amnt': [loan_amnt],
    f'loan_int_rate': [loan_int_rate],
    'loan_status': [loan_status],
    f'loan_percent_income': [a],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length],
    'MORTGAGE': [1 if mortgage == 'Yes' else 0],
    'OTHER': [1 if other == 'Yes' else 0],
    'OWN': [1 if own == 'Yes' else 0],
    'RENT': [1 if rent == 'Yes' else 0],
    'DEBTCONSOLIDATION': [1 if debtconsolidation == 'Yes' else 0],
    'EDUCATION': [1 if education == 'Yes' else 0],
    'HOMEIMPROVEMENT': [1 if homeimprovement == 'Yes' else 0],
    'MEDICAL': [1 if medical == 'Yes' else 0],
    'PERSONAL': [1 if personal == 'Yes' else 0],
    'VENTURE': [1 if venture == 'Yes' else 0]
})


if st.button("Predict"):
    pred = model.predict(data)
    if pred[0] == 1:
        st.write("You are a credit default risk.")
    else:
        st.write("You are not a credit default risk.")

