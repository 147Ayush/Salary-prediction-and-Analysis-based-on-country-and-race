# Salary Prediction Model Documentation

## Introduction
The Salary Prediction Model is an advanced web-based application designed to estimate an individual's salary based on various input factors such as age, gender, job title, education level, experience, and country. Leveraging a pre-trained machine learning model, this application provides accurate salary predictions and aids in HR decisions and compensation planning. The user-friendly interface, built with Streamlit, ensures an interactive and seamless experience.


## Setup and Installation

### Prerequisites

Clone Repository

```bash
Git clone https://github.com/147Ayush/Salary-prediction-and-Analysis-based-on-country-and-race.git
```

Ensure you have Python and the necessary libraries installed. You can install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Key Features

- **Interactive User Interface**: The application offers an intuitive interface with dropdowns, sliders, and radio buttons for easy data input.
- **Accurate Predictions**: Utilizes a pre-trained linear regression model to predict salaries based on multiple features.
- **Comprehensive Job Titles**: Supports a wide range of job titles, catering to diverse professional backgrounds.
- **Country and Education Level Mapping**: Converts categorical inputs into numerical values for precise model predictions.
- **Real-time Results**: Provides instant salary predictions upon submission of input data.

## User Interface
The interface allows users to input various features that influence salary predictions:
- **Country Selection**: Dropdown menu to select the user's country.
- **Education Level**: Dropdown menu to choose the highest level of education.
- **Job Title**: Extensive dropdown menu listing various job titles.
- **Gender**: Radio buttons to select gender.
- **Age**: Slider to input age.
- **Experience**: Slider to input years of professional experience.

## Input Fields Explained
- **Country**: Options include USA, China, Australia, UK, and Canada.
- **Education Level**: Options include Bachelor's, Master's, PhD, and High School.
- **Job Title**: A comprehensive list covering roles in software engineering, data science, marketing, sales, HR, finance, and more.
- **Gender**: Male or Female.
- **Age**: Range from 0 to 100 years.
- **Experience**: Range from 0 to 35 years. 

## Data Processing
To ensure accurate predictions, the application processes categorical data into numerical values:
- **Country Mapping**: Converts country names into numerical representations.
- **Education Level Mapping**: Converts education levels into numerical representations.
- **Label Encoding**: Uses pre-trained LabelEncoder objects to transform gender and job title into numerical values.

## Prediction Logic
Upon submission of the input data, the model processes the inputs and predicts the expected salary:
- **Submit Button**: Triggers the prediction process.
- **Model Prediction**: The pre-trained model calculates the salary based on the input features.
- **Result Display**: The predicted salary is displayed on the interface.

## About the Model
The model is built using a linear regression algorithm trained on historical salary data. By considering factors such as education, experience, job title, and location, it aims to provide accurate salary predictions.

## Benefits
- **Enhanced HR Decisions**: Helps HR professionals in making informed compensation decisions.
- **Career Planning**: Assists individuals in understanding potential earnings based on their qualifications and experience.
- **Data-Driven Insights**: Provides a quantitative approach to salary estimation. 

## Usage Instructions
Open the Application: Launch the Streamlit application.
- **Input Data**: Enter the required information in the provided fields.
- **Submit**: Click the "Submit" button to generate the salary prediction.
- **View Results**: The predicted salary is displayed on the screen.

## App Deployed link
https://salary-prediction-and-analysis-based-on-country-and-race-diwvs.streamlit.app/

# Conclusion
The Salary Prediction Model is a powerful tool for estimating salaries based on multiple influential factors. Its interactive interface, combined with a robust pre-trained model, makes it an invaluable resource for HR professionals, career advisors, and individuals seeking data-driven salary insights.






