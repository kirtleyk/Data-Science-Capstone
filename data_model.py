import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from regression_function import regr

def _distplot(columns):
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.distplot(df[col])
        plt.show()
        
# Read in pickle file into data frame
df = pd.read_pickle("cleaned_salary_dataset.pkl")

# Use one hot encoding to convert unique values to columns for model
dummy = pd.get_dummies(df.Location)
dummy2 = pd.get_dummies(df['Job Roles'])

dummy3 = pd.get_dummies(df['Employment Status'])
# print(dummy3)
# Concatenate dummies with dataset together into one dataframe
merged = pd.concat([df, dummy, dummy2, dummy3], axis='columns')

#remove unneeded columns and those used in onehot encoding 
# Job Roles, Location and Employment status were converted using One-hot encoding so original fields must be dropped
merged = merged.drop(['Location', 'Job Roles', 'Employment Status'], axis='columns')

# train/test split 
train_set, test_set = train_test_split(merged, test_size=.2, random_state=123)

print('Train size: ', len(train_set), 'Test size: ', len(test_set))

# Define the dependent column values to use in the training and testing
test_train_columns = ['Bangalore', 'Chennai', 'Hyderabad', 'Jaipur', 'Kerala', 'Kolkata', 'Madhya Pradesh', 'Mumbai', 'New Delhi', 'Pune', 'Android', 'Backend', 'Database', 'Frontend',
                      'IOS', 'Java', 'Mobile', 'Python', 'SDE', 'Testing', 'Web', 'Rating', 'Contractor', 'Intern', 'Full Time', 'Trainee']

# 'Bangalore', 'Chennai', 'Hyderabad', 'Jaipur', 'Kerala', 'Kolkata', 'Madhya Pradesh', 'Mumbai', 'New Delhi', 'Pune', 
# 'Android', 'Backend', 'Database', 'Frontend', 'IOS', 'Java', 'Mobile', 'Python', 'SDE', 'Testing', 'Web'
#Define the training set
X = train_set[test_train_columns]
# Define dependent/target column
y = train_set['USSalary']

# Define the test set
X_test = test_set[test_train_columns]
y_test = test_set['USSalary']

####################### Excecute Models and get Results #################################
print()
print('****** Training Set Evaluation Scores ******')
train, test = regr(X,y,X_test,y_test)

print(train)
print()

print('****** Test Set Evaluation Scores ******')
print(test)

sns.barplot(data=train)