# import packages
from cmath import log
from matplotlib.pyplot import figure, title
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')

%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12, 8)

pd.options.mode.chained_assignment = None

plt1 = plt2 = plt3 = plt4 = plt

# read the data
df = pd.read_csv('Salary_Dataset.csv')
# print(df.describe())
# print(df.head())
print(df.dtypes)
# evaluate and drop unneeded features
# df = df.drop(columns=(['Salaries Reported', 'Job Title', 'Company Name', ]))

# shape and data types of the data
# print("Shape", df.shape)
#print(df.dtypes)
# print("Value Counts", df.dtypes.value_counts())
# print(df.describe())

#separate numeric from object columns

# num_cols = df.columns[df.dtypes != 'object']
# cat_cols = df.columns[df.dtypes == 'object']

#print("numeric:", num_cols, "non-numeric:", cat_cols)

#Find missing values in numeric columns
#print("NULL in Numeric Columns", df[num_cols].isnull().sum())
# Find missing values in object columns
#print("NULL in ojbect Columns", df[cat_cols].isnull().sum())


#Find outliers in salary
#print(df.describe()[['Salary','Rating']])

plt.figure(figsize=(5, 4))
plt.suptitle('Salary Boxplot - Outliers')
plt.boxplot(df['Salary'])

#Salary outlier found with value of 90,000,000 Rupees
#Remove outlier 
df2 = df[df.Salary == 90000000].index
print("Dropping...", df2)
df = df.drop(df2)

plt.figure(figsize=(5, 4))
plt.suptitle('Salary Boxplot - Removed Outlier')
plt.boxplot(df['Salary'])

# Rating outliers
# plt.figure(figsize=(5, 4))
# plt.suptitle('Rating Boxplot - Outliers')
# plt.boxplot(df['Rating'])

# Add US Salary to dataset based on Salary for Rupee
# Conversion rate is .012
rcr = 0.012
df = df.assign(USSalary=lambda x: (x['Salary']*rcr))

print("After USSalary Added")
print(df.describe())

plt.figure(figsize=(5, 4))
plt.suptitle('US Salary Boxplot - Removed Outlier')
plt.boxplot(df['USSalary'])


print("Post Cleansing", df.shape)
num_cols = df.columns[df.dtypes != 'object']
cat_cols = df.columns[df.dtypes == 'object']




df.describe(include='all')

df.isnull().sum()


# Rating distribution
plt.figure(figsize=(10,4))
plt.hist( df["Rating"], bins=[1, 2, 3, 4, 5])
plt.suptitle('Rating Distribution')
plt.savefig("./img/rating_distribution.png", dpi=100)

#Location distribution
plt2.figure(figsize=(15,4))
plt2.hist(df["Location"])
plt2.suptitle('Location Distribution')
plt2.savefig("./img/location_distribution.png", dpi=100)


#print(df["Location"].unique())

# Job Role Distribution
plt2.figure(figsize=(10, 5))
plt2.hist(df["Job Roles"])
plt2.suptitle('Job Role Distribution')
plt2.savefig("./img/job_role_distribution.png", dpi=100)

#print(df["Job Roles"].unique())
print(df["Employment Status"].unique())

sns.displot(df['USSalary'])
sns.displot(df['Rating'])


# sns.relplot(x='Location', y='USSalary', hue='Location', data=df)


# calculate correlation matrix
corr = df.corr()  # plot the heatmap
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
            annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

# Scatter Plot looking at instance of Job roles in different locations
# Job roles are not evenly distributed in each locatoin. Several locations only use one job role.
df.plot(kind='scatter', x='Location', y='Job Roles')

# Scatter Plot looking at instance of Job roles in different locations
# Job roles are not evenly distributed in each locatoin. Several locations only use one job role.
df.plot(kind='scatter', x='Location', y='USSalary')



# plt3.figure(figsize=(15,4))
# plt3.bar(df["Location"], df["Salary"], log=True)


# plt4.figure(figsize=(15,4))
# plt4.bar(df["Location"], df["Salary"], log=False)
# plt4.suptitle('Salary by Location')

#fig, ax1 = plt3.subplots()

#x = df['Salary']
#y1 = df['Location']
#y2 = df['Ctrv']

#ax2 = ax1.twinx()

#ax1.plot(x, y1, 'g-')
#ax2.plot(x, y2, 'b-')
#plt3.bar(x, 10)

# LowSalary = df[['Salary','Location']].query("Salary < 80000") 

# for x in LowSalary:
#     print(LowSalary['Salary'], LowSalary['Location'])

# Save the dataset to a pickle file
df.to_pickle("cleaned_salary_dataset.pkl")