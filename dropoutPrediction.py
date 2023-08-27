import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('save2.plk', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

logreg = data['model']


def show_dropoutPrediction():
    st.title("Student Dropout Prediction")
    st.write("""### We need some information to predict the student dropout""")
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

    tce2 = st.number_input('Enter 2nd Semester Total Credit Enrolled', min_value=0.0, max_value=25.0)
    st.write('The 2nd Semester Total Credit Enrolled is: ', tce2)

    ce2 = st.number_input('Enter 2nd Semester Number of Courses Enrolled', min_value=0.0, max_value=9.0)
    st.write('2nd Semester Courses Enrolled is: ', ce2)

    gpa2 = st.number_input('Enter 2nd Semester GPA', min_value=0.0, max_value=5.0)
    st.write('2nd Semester GPA is: ', gpa2)

    tcp = st.number_input('Enter Total Credit Passed', min_value=0.0, max_value=50.0)
    st.write('Total credit passed is: ', tcp)

    gpa = st.number_input('Enter GPA for the Session', min_value=0.0, max_value=5.0)
    st.write('GPA obtained is: ', gpa)

    tcr = tce1 + tce2
    tcf = tcr - tcp

    ok = st.button("Check for dropout Prediction")
    if ok:
        X = np.array([[gender, tce1, ce1, gpa1, tce2, ce2, gpa2, tcp, tcf, tcr, gpa]])
        X
        dropout = logreg.predict(X)
        st.divider()
        st.subheader(f"Prediction is : {dropout}")
