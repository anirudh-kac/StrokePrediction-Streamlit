import streamlit as st
from predictor import predict


left_column, right_column = st.beta_columns(2)


with left_column:
    st.title("Stroke Prediction")
    st.image('./stroke.jpg')

with right_column:
    age = st.sidebar.slider('Age', min_value=0, max_value=100,value = 50)
    st.write("Age : " + str(age));
    gender = st.sidebar.radio('Gender', ["Male","Female"])
    st.write("Gender : " + gender); 
    gender = 0 if gender=="Male" else 1

    hypertension = st.sidebar.radio('History of Hypertension',["No","Yes"])
    st.write("History of hypertension : " + hypertension); 
    hypertension = 0 if hypertension == "No" else 1

    heart_disease = st.sidebar.radio('History of Heart Disease',["No","Yes"])
    st.write("History of heart disease : " + heart_disease); 
    heart_disease = 0 if  heart_disease == "No" else 1

    ever_married = st.sidebar.radio('Ever Married',["No","Yes"])
    st.write("Ever married : " + ever_married); 
    ever_married = 0 if ever_married == "No" else  1

    work_type = st.sidebar.radio('Work Type',['Private','Self Employed','Govt Job','Children','Never Worked'])
    st.write("Work Type : " + work_type); 
    d = {
        'Private': 0,
        'Self Employed': 1,
        'Govt Job': 2,
        'Children': 3,
        'Never Worked': 4
    }
    work_type = d[work_type]

    residence_type = st.sidebar.radio('Residence Type',['Rural','Urban'])
    st.write("Residence Type : " + residence_type); 
    residence_type = 0 if residence_type == "Rural" else 1

    avg_glucose_level = st.sidebar.slider('Average glucose level', min_value=50, max_value=300,value=150)
    st.write("Average Glucose Level : " + str(avg_glucose_level)); 

    bmi = st.sidebar.slider('BMI', min_value=10, max_value=40,value = 22)
    st.write("Body Mass Index (BMI) : " + str(bmi)); 
    smokes = st.sidebar.radio('Smoking',['Formerly smoked','Never smoked','Smokes'])
    st.write("Smoking Status :  " + smokes)
    d = {
        'Formerly smoked': 0,
        'Never smoked': 1,
        'Smokes': 2
    }
    smokes = d[smokes]


result = predict(gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smokes)


st.subheader("Result : ")
if result == 1:
    st.subheader("The person is likely to have a stroke in future")
else:
    st.subheader("The person looks healthy and won't have a stroke in future")


