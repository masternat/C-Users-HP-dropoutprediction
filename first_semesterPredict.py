import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('save3.plk', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

logreg2 = data['model']


def show_firstSemesterPredict():
    st.title("Student Dropout Prediction")
    st.write("""### We need some information to predict the student dropout in First Semester""")
    st.caption('For the output of Prediction, 0 means DROPOUT & 1 means SUCCESSFUL')
    st.divider()
    genders = (0, 1)
    gender = st.selectbox('Select Gender 0 - Female, 1 - Male ', genders)

    tce1 = st.number_input('Enter 1st Semester Total Credit Enrolled', min_value=0.0, max_value=25.0)
    st.write('The 1st Semester Total Credit Enrolled is: ', tce1)

    ce1 = st.number_input('Enter 1st Semester Number of Courses Enrolled', min_value=0.0, max_value=9.0)
    st.write('1st Semester Courses Enrolled is: ', ce1)

    gpa1 = st.number_input('Enter 1st Semester GPA', min_value=0.0, max_value=5.0)
    st.write('1st Semester GPA is: ', gpa1)

    ok = st.button("Check for dropout Prediction")
    if ok:
        X = np.array([[gender, tce1, ce1, gpa1]])
        X
        dropout = logreg2.predict(X)
        st.divider()
        st.subheader(f"Prediction is : {dropout}")
