import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:\\Users\\devan\\student_score.csv')

# Display the first few rows of the dataframe
print(df.head())

# Display the descriptive statistics of the dataframe
print(df.describe())

# Display information about the dataframe
df.info()

# Drop the unnecessary 'Unnamed: 0' column
df = df.drop('Unnamed: 0', axis=1)
print(df.head())

# Plot the count of genders
plt.figure(figsize=(5, 5))
ax = sns.countplot(data=df, x="Gender")
ax.bar_label(ax.containers[0])
plt.title("GENDER DISTRIBUTION ")

plt.show()


gb = df.groupby("ParentEduc").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore": 'mean'})
print(gb)
plt.figure(figsize=(5,5))
sns.heatmap(gb,annot=True)
plt.title("PARENTS  EDUCATION ")
plt.show()# from thi swe can conclude that the education of the parents have a good impact 
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore": 'mean'})
print(gb1)
plt.figure(figsize=(5,5))
sns.heatmap(gb,annot=True)
plt.title("PARENTS MARITIAL STATUS")
plt.show() #from this we can conclude that the MaritalStatus of the parents have a neglizible  impact 
sns.boxplot(data=df, x="MathScore")
plt.title("Math_Score")
plt.show()
sns.boxplot(data=df,x="ReadingScore")
plt.title("Reading_Score")
plt.show()
sns.boxplot(data=df, x="WritingScore")
plt.title("Writing_Score")
plt.show()
print(df["EthnicGroup"].unique())
groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()
l=[groupA,groupB,groupC,groupD,groupE]
mylist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(mylist)
plt.pie(mylist,labels=l,autopct="%1.2f%%")
plt.title("DISTRIBUTION OF ETHNICV GROUPS")
plt.show()
ax=sns.countplot(data=df,x="EthnicGroup")
plt.show()
ax.bar_label(ax.containers[0])
plt.show()





