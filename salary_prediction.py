import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

with open('model.pkl','rb') as f:
    model = pickle.load(f)

with open('encoding_directory.pkl','rb') as l:
    encoding_directory = pickle.load(l)

st.title('Salary Prediction Model')
st.write("About Model:-")
st.caption("A salary prediction model utilizes data on factors like education, experience, job title, and "
           "location to estimate an individuals salary. By preprocessing and engineering features, selecting a"
            "suitable regression model, and training it with historical data, the model aims to accurately" 
            "forecast salaries, aiding in HR decisions and compensation planning")

list =        ['None','Software Engineer', 'Data Scientist', 'Software Engineer Manager', 'Data Analyst', 'Senior Project Engineer',
              'Product Manager', 'Full Stack Engineer', 'Marketing Manager', 'Back end Developer', 'Senior Software Engineer',
              'Front end Developer', 'Marketing Coordinator', 'Junior Sales Associate', 'Financial Manager', 'Marketing Analyst',
              'Software Developer', 'Operations Manager', 'Human Resources Manager', 'Director of Marketing', 'Web Developer',
              'Research Director', 'Product Designer', 'Content Marketing Manager', 'Sales Associate',
              'Senior Product Marketing Manager', 'Director of HR', 'Research Scientist', 'Marketing Director', 'Sales Director',
              'Senior Data Scientist', 'Junior HR Generalist', 'Junior Software Developer', 'Receptionist', 'Director of Data Science',
              'Sales Manager', 'Digital Marketing Manager', 'Junior Marketing Manager', 'Junior Software Engineer',
              'Human Resources Coordinator', 'Senior Research Scientist', 'Senior Human Resources Manager', 'Senior HR Generalist',
              'Junior Web Developer', 'Junior Sales Representative', 'Financial Analyst', 'Sales Executive', 'Sales Representative',
              'Front End Developer', 'Junior HR Coordinator', 'Junior Data Analyst', 'Graphic Designer', 'Project Manager']
a = b = c = d = x = y = z = 0
def match_country(country):
    global a ,b, c, d
    match country:
        case "USA":
            d = 1
            a = 0
            b = 0
            c = 0
        case "Australia":
            a = 0
            b = 0
            c = 0
            d = 0.

        case "Canada":
            a = 1
            b = 0
            c = 0
            d = 0
        case "China":
            a = 0
            b = 1
            c = 0
            d = 0
        case "UK":
            a = 0
            b = 0
            c = 1
            d = 0

def match_Education(education):
    global x, y, z
    match education:
        case "Bachelor's":
            x = 0
            y = 0
            z = 0
        case "Master's":
            x = 0
            y = 1
            z = 0
        case 'High School':
            x = 1
            y = 0
            z = 0
        case 'PhD':
            x = 0
            y = 0
            z = 1



def label_encoding(Gender, Job_Title):
    cols_to_encode = ['Gender', 'Job Title']
    new_data = {
        'Gender': [Gender],
        'Job Title': [Job_Title]
    }
    df_new = pd.DataFrame(new_data)

    for col in cols_to_encode:
        le = encoding_directory[col]
        df_new[col] = le.transform(df_new[col])

    return df_new["Gender"].iloc[0], df_new["Job Title"].iloc[0]

#UI
country = st.selectbox("Enter Country",["None","USA", "China", "Australia", "UK", "Canada"])
match_country(country)
Education = st.selectbox("Enter Education Level",["None","Bachelor's", "Master's", 'PhD', 'High School'])
match_Education(Education)
Job_Title = st.selectbox("Enter Job Title",list)
Gender = st.radio("Select Gender",["Male","Female"])
Age = st.slider("Enter Age",0,100)
Experience = st.slider("Enter your Experience",0,35)

#Model prediction
button_clicked = st.button("Submit")
if button_clicked:
    try:
        result1, result2 = label_encoding(Gender, Job_Title)
        prediction = abs(model.predict([[Age, result1, result2, Experience, a, b, c, d, x, y, z]]))
        st.success(f"Expected Salary in RS {prediction[0]}")
    except ValueError as e:
        st.error(e)


