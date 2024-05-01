import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import requests as re

st.title("Credit Card Fraud Detection Web App")

st.image("image.png")

st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning API in order to detect fraudulent credit card  based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Credit-Card-Fraud-Detection)

**Made by Group 3 Zummit Africa AI/ML Team**
**Contributors:**
- **Hilary Ifezue(Group Lead)**
- **Nneji Ifeanyi**
- **Somtochukwu Ogechi**
- **ThankGod Omieje**
""")


st.sidebar.header('User Input Features of The Transaction')

sender_name = st.text_input("Input Sender ID")
receiver_name = st.text_input("")
step = st.sidebar.slider('Number of Hours it took the Transaction to complete: ')
types = st.sidebar.selectbox("Type of Transfer Made: Enter 0 for Cash In Transaction\n 1 for Cash Out Transaction\n 2 for Debit Transaction\n 3 for Payment Transaction\n  4 for Transfer Transaction.",(0,1,2,3,4))
amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input('Original Balance Before Transaction was made',min_value=0, max_value=110000)
newbalanceorg= st.sidebar.number_input('New Balance After Transaction was made',min_value=0, max_value=110000)
oldbalancedest= st.sidebar.number_input('Old Balance',min_value=0, max_value=110000)
newbalancedest= st.sidebar.number_input('New Balance',min_value=0, max_value=110000)
isflaggedfraud = st.sidebar.selectbox('Specify if this was flagged as Fraud by your System: ',(0,1))

if st.button("Detection Result"):
    values = {
            'Hours': step,
                'type_of_transfer': types,
                'amount': amount,
                'old_balance_original': oldbalanceorg,
                'new_balance_original': newbalanceorg,
                'old_balance_dest': oldbalancedest,
                'new_balance_dest': newbalancedest,
                'is_flagged_fraud': isflaggedfraud}

    #res = re.post(f"https://credit-fraud-ml-api.herokuapp.com/predict",json=values)
    #json_str = json.dumps(res.json())
    #resp = json.loads(json_str)
    st.write("The transaction that took place between { and  is ")









