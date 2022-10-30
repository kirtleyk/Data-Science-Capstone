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

# evaluate and drop unneeded features
df = df.drop(columns=(['Salaries Reported', 'Job Title', 'Company Name', ]))

# shape and data types of the data
print("Shape", df.shape)
#print(df.dtypes)
print("Value Counts", df.dtypes.value_counts())
print(df.describe())

#separate numeric from object columns

num_cols = df.columns[df.dtypes != 'object']
cat_cols = df.columns[df.dtypes == 'object']

print("numeric:", num_cols, "non-numeric:", cat_cols)

#Find missing values in numeric columns
print("NULL in Numeric Columns", df[num_cols].isnull().sum())
# Find missing values in object columns
print("NULL in ojbect Columns", df[cat_cols].isnull().sum())


#Find outliers
print(df.describe()[['Salary','Rating']])

plt.figure(figsize=(5, 4))
plt.suptitle('Salary Boxplot - Outliers')
plt.boxplot(df['Salary'])

#fig.subplots_adjust(top=0.8)
# Creating axes instance
# ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
# bp = ax.boxplot(df['Salary'])

# show plot
plt.show()


# find missing data - yellow is missing. blue is not missing.
# plt.figure(figsize=(10,4))
# sns.heatmap(df.isna().transpose(), 
#             cmap="YlGnBu",
#             cbar_kws={'label': 'Missing Data'})
# save heatmap to project - no missing data
#plt.savefig(".\img\missing_data_heatmap.png", dpi=100)
# if it's a larger dataset and the visualization takes too long can do this.
# % of missing.
# for col in df.columns:
#     pct_missing = np.mean(df[col].isna())
#     print('{} - {}%'.format(col, round(pct_missing*100)))

# Rating distribution
# plt.figure(figsize=(10,4))
# plt.hist( df["Rating"], bins=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], log=True)
# plt.suptitle('Rating Distribution')
# plt.savefig("./img/rating_distribution.png", dpi=100)

#Location distribution
# plt1.figure(figsize=(15,4))
# plt1.hist(df["Location"], log=True)
# plt1.suptitle('Location Distribution')
# plt1.savefig("./img/location_distribution.png", dpi=100)


#print(df["Location"].unique())

# Job Role Distribution
# plt2.figure(figsize=(10, 5))
# plt2.hist(df["Job Roles"])
# plt2.suptitle('Job Role Distribution')
# plt2.savefig("./img/job_role_distribution.png", dpi=100)

# print(df["Job Roles"].unique())


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