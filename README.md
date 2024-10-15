# 📊 Customer Churn Prediction Using ANN 🤖

This project aims to predict customer churn using an **Artificial Neural Network (ANN)**. The model classifies whether a customer is likely to churn based on their demographic and transactional details. The project includes preprocessing, model training, and deployment via **Streamlit** for an interactive user interface.

## 🚀 Streamlit Web Application

Check out the live demo of the churn prediction model here:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://github.com/venkatsubash2003/Churn_prediction_Using_ANN)

### Key Features:
- Real-time churn prediction based on user inputs
- Feature scaling and encoding integrated into the prediction pipeline
- User-friendly web interface

## 📚 Table of Contents
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Preprocessing](#-preprocessing)
- [Modeling](#-modeling)
- [Evaluation](#-evaluation)
- [Usage](#-usage)

## 📂 Project Structure

📂 Churn_Prediction_ANN/
├── 📁 Models/
│   ├── model.h5                    # Trained ANN model
│   ├── label_encoder_gender.pkl     # Label encoder for gender
│   ├── one_hot_encoder_geo.pkl      # One-hot encoder for geography
│   └── scaler.pkl                   # StandardScaler for feature scaling
├── app.py                           # Streamlit app source code
├── README.md                        # Project documentation
├── requirements.txt                 # Required Python libraries
└── 📂 Data/
    └── customer_data.csv            # Dataset used for training and testing


