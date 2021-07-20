from joblib import load
import numpy as np
model = load('model_final.joblib')

def predict(gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status):
    """

    gender  [0 - 'Male' 1 - 'Female']
    hypertension [ 0 - 'No' , 1 - 'No']
    heart disease [ 0 - 'No' , 1 - 'No']
    ever_married [0- 'No' 1 - 'Yes']
    work_type [0- 'Private' 1-'Self-employed' 2-'Govt_job' 3-'children' 4-'Never_worked']
    Residence_type [0 - 'Urban' 1 - 'Rural']
    smoking_status [0 - 'formerly smoked' 1-'never smoked' 2-'smokes' 3-'Unknown']
    """
    values = np.array([[gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status]])
    result = model.predict(values)
    return result[0]