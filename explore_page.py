import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.cache_resource
def load_data():
    studentRecord = pd.read_csv('studentRecord2.csv')
    studentRecord = studentRecord[
        ["Gender", "Year", "1-TCE", "1-CE", "1-GPA", "2-TCE", "2-CE", "2-GPA", "TCP", "TCF", "TCR", "GPA",
         "Status"]]
    studentRecord['Gender'] = studentRecord['Gender'].astype('category')
    studentRecord['Gender'] = studentRecord['Gender'].cat.codes
    return studentRecord

studentRecord = load_data()

def show_explore():
    st.title("Explore Student Success/Dropout Rates")

    st.write(
        """
        ### University of Benin Computer Science Year 1 Survey 2016 - 2022
        """
    )
    st.caption("Female : 0 and Male : 1 comparisons between 2016 - 2020")
    ax = sns.displot(data=studentRecord, x="Gender",col="Year", color="#FF004F")
    fig = plt.gcf()
    fig.set_size_inches(5, 3)
    st.pyplot(ax)

    st.divider()
    st.caption("Failure: 0 and Success: 0 rates comparisons between 2016 - 2020")
    ay = sns.displot(data=studentRecord, x="Status",col="Year", color="#5AFF54")
    fig = plt.gcf()
    fig.set_size_inches(5, 3)
    st.pyplot(ay)

    st.divider()

    st.caption("Failure: 0 and Success: 0 rates comparisons by Gender")
    az = sns.displot(data=studentRecord, x="Status", col="Gender", color="#ffaa00")
    fig = plt.gcf()
    fig.set_size_inches(5, 3)
    st.pyplot(az)

