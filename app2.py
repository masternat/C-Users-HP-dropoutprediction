import streamlit as st
from dropoutPrediction import show_dropoutPrediction
from explore_page import show_explore
from first_semesterPredict import show_firstSemesterPredict

page = st.sidebar.selectbox("Predict, First Semester, Explore", ("Predict", "First Semester Prediction", "Expore"))
if page == "Predict":
    show_dropoutPrediction()
elif page == "First Semester Prediction":
    show_firstSemesterPredict()
else:
    show_explore()
