import streamlit as st
import numpy as np 
import pandas as pd 
import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder

model = tf.keras.models.load_model("Models/model.h5")

label_encoder_gender = pickle.load(open("Models/label_encoder_gender.pkl","rb"))
onehotencoder_geo = pickle.load(open("Models/one_hot_encoder_geo.pkl","rb"))
scaler = pickle.load(open("Models/scaler.pkl","rb"))

### Streamlit app 
st.title("Customer Churn Prediction:")

## Taking the inputs for prediction
geography = st.selectbox("Geography",onehotencoder_geo.categories_[0])
gender = st.selectbox("Gender",label_encoder_gender.classes_)
age = st.slider("Age",18,92)
balance = st.number_input("Balance")
credit_score = st.number_input("Credit Score")
estimated_salary = st.number_input("Estimated Salary")
tenure = st.slider("Tenure",0,10)
num_of_products = st.slider("Number of Products",1,4)
has_cr_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])

input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [label_encoder_gender.transform([gender])[0]],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "EstimatedSalary": [estimated_salary]
})

geo_encoded = onehotencoder_geo.transform([[geography]])
df = pd.DataFrame(data=geo_encoded, columns = onehotencoder_geo.get_feature_names_out(["Geography"]))

input_data = pd.concat([input_data.reset_index(drop=True),df],axis=1)

input_data_scaled = scaler.transform(input_data)

prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

if st.button("Predict"):
    if prediction_proba > 0.5:
        st.write("The customer is likely to churn")
    else:
        st.write("The customer is not likely to churn")

