import streamlit as st
import requests 
st.title("Disease prediction")

disease=st.selectbox("select disease",["Heart","diabetes"])
if disease=="Heart":
    age=st.slider("age",20,80)
    sex=st.selectbox("sex",[0,1])
    cp=st.select_slider("chestpain type",[0,1,2,3])
    trestbps=st.slider("Resting BP",90,200)
    chol=st.slider("cholestrol",100,400)
    fbs=st.selectbox("fasting blood sugar>120",[0,1])
    restecg=st.selectbox("rest ecg",[0,1,2])
    thalach=st.slider("Max heart rate",70,200)
    exang=st.selectbox("exercise induced angina",[0,1])
    oldpeak=st.slider("oldpeak",0.6,6.0)
    slope=st.selectbox("slope",[0,1,2])
    ca=st.selectbox("CA",[0,1,2,3,4])
    thal=st.selectbox("thal",[0,1,2])
    features=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    endpoint="http://localhost:8000/heart_pred"
elif disease=="diabetes":
    Pregnancies=st.slider("Pregnancies",0,12)
    Glucose=st.slider("Glucose",40,200)
    BloodPressure=st.slider("BloodPressure",0,100)
    SkinThickness=st.slider("SkinThickness",0,40)
    Insulin=st.slider("Insulin",0,200)
    BMI=st.slider("BMI",0.0,40.0)
    DiabetesPedigreeFunction=st.slider("DiabetesPedigreeFunction",0.0,1.15)
    Age=st.slider("Age",25,80)
    features=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    endpoint="http://localhost:8000/diabetes_pred"



if st.button("predict"):
    response=requests.post(endpoint,json=features)
    if response.status_code==200:
        risk=response.json()['risk_score']
        st.success(f"Risk score:{risk:.2f}")
    else:
        st.error(f"Error:{response.text}")