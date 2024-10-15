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




## 📊 Dataset

The dataset used for this project contains customer details, including:

- 🌍 **Geography** (countries)
- 👥 **Gender**
- 📊 **Age**, **Balance**, **Credit Score**
- 💰 **Estimated Salary**
- 📅 **Tenure** (number of years as a customer)
- 🛍️ **Number of Products**
- 💳 **Has Credit Card** (binary flag)
- 📈 **Is Active Member** (binary flag)
- 🔄 **Churn** (target variable)

## 🧹 Preprocessing

The following steps were applied to the data before feeding it to the ANN model:

1. **Label Encoding**: Categorical variables such as gender were label encoded using `LabelEncoder`.
2. **One-Hot Encoding**: Geography was one-hot encoded using `OneHotEncoder` to avoid any ordinal relationship.
3. **Feature Scaling**: Continuous variables like balance and credit score were scaled using `StandardScaler`.

## 🤖 Modeling

The project uses an **Artificial Neural Network (ANN)**, implemented in TensorFlow. Key aspects of the model:

- **Architecture**: A simple feed-forward neural network with fully connected layers
- **Activation Functions**: ReLU for hidden layers, sigmoid for the output layer (binary classification)
- **Loss Function**: Binary Cross-Entropy
- **Optimizer**: Adam

The model was trained on the customer dataset to classify whether a customer will churn (1) or not (0).

## 🚀 Usage

### Running the App Locally

You can run the Streamlit app locally by following these steps:
git clone https://github.com/venkatsubash2003/Churn_prediction_Using_ANN
cd Churn_prediction_Using_ANN
pip install -r requirements.txt
streamlit run main.py

