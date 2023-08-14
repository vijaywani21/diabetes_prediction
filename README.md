# diabetes_prediction

## 1. Problem Statement:
To predict the diabetes charges based on following parameters:

1. Pregnancies	
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BIM
7. DiabetesPedigreeFunction
8. Age

## 2. Dataset:
The dataset required was downloaded from Kaggle website.

Download the dataset from [Diabetes_Data](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)

## 3. Package Required:
All the packages required for model building are mentioned in requirement.txt file

## 4. Dataset Reading:
Done using pandas library as follows:

df = pd.read_csv(' Concrete_data.csv')

df

## 5. Model Building:

Algorithm used : Linear Regression

Steps: Following stpes invoved in model building.

1. Problem Statement
2. Data Gathering
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Assumptions Check
8. Single Row Check
9. Pickle File Creation

## 6. API Writing:
API writing for builded model was done in VS Code with help of flask web framework, along with HTML code.

Model data required for writing api importted through pickle file

It was then tested using Postman app.

command to run flask app in vs code:

flask run

or

python app.py

## 7. Deployment On Cloud:
Build model was deployed on cloud using Amazon web services's EC2 instance and Git Bash terminal

command to run app in Git Bash

python3 app.py
