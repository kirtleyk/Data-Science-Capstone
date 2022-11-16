from sklearn.ensemble import RandomForestClassifier
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from regression_function import regr

def _distplot(columns):
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.distplot(df[col])
        plt.show()
        
# Read in pickle file into data frame
df = pd.read_pickle("cleaned_salary_dataset.pkl")
_distplot(['USSalary'])
outliers = df.quantile(.97)
print(outliers)

df = df[(df['USSalary'] < outliers['USSalary'])]
_distplot(['USSalary'])

# Use one hot encoding to convert unique values to columns for model
dummy = pd.get_dummies(df.Location)
dummy2 = pd.get_dummies(df['Job Roles'])
dummy3 = pd.get_dummies(df['Employment Status'])

# Concatenate dummies with dataset together into one dataframe
merged = pd.concat([df, dummy, dummy2, dummy3], axis='columns')

#remove unneeded columns and those used in onehot encoding 
# removed USSalary as it is target variable
# Job Roles, Location and Employment status were converted using One-hot encoding so original fields must be dropped
merged = merged.drop(['Location', 'Job Roles', 'Employment Status'], axis='columns')

# train/test split 
train_set, test_set = train_test_split(merged, test_size=.2, random_state=123)

print('Train size: ', len(train_set), 'Test size: ', len(test_set))

X = train_set[['Bangalore', 'Chennai', 'Hyderabad', 'Jaipur', 'Kerala', 'Kolkata',
               'Madhya Pradesh', 'Mumbai', 'New Delhi', 'Pune', 'Android', 'Backend',
               'Database', 'Frontend', 'IOS', 'Java', 'Mobile', 'Python', 'SDE',
               'Testing', 'Web', 'Contractor', 'Full Time', 'Intern', 'Trainee', 'Rating']]

y = train_set['USSalary']

X_test = test_set[['Bangalore', 'Chennai', 'Hyderabad', 'Jaipur', 'Kerala', 'Kolkata',
               'Madhya Pradesh', 'Mumbai', 'New Delhi', 'Pune', 'Android', 'Backend',
               'Database', 'Frontend', 'IOS', 'Java', 'Mobile', 'Python', 'SDE',
               'Testing', 'Web', 'Contractor', 'Full Time', 'Intern', 'Trainee', 'Rating']]
y_test = test_set['USSalary']

####################### Excecute Models and get Results #################################
print()
print('****** Training Set Evaluation Scores ******')
print(regr(X,y))
print()
print('****** Test Set Evaluation Scores ******')
print(regr(X_test, y_test))

