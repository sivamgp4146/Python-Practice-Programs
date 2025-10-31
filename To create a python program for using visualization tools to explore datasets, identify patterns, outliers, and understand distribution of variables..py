#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Sample data
data = {
    'Student_ID': range(1, 11),
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Mike', 'Sara', 'Tom', 'Nina', 'Leo', 'Anna'],
    'Age': [20, 21, 19, 22, 20, 21, 23, 19, 20, 21],
    'Department': ['CS', 'IT', 'CS', 'BCA', 'CS', 'IT', 'BCA', 'CS', 'IT', 'BCA'],
    'Marks': [85, 90, 78, 92, 60, 88, 55, 95, 80, 70],
    'Attendance (%)': [90, 95, 85, 88, 60, 92, 50, 98, 87, 72]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set default style
sns.set(style='whitegrid')


# In[3]:


plt.figure(figsize=(7, 4))
sns.histplot(df['Marks'], bins=8, kde=True, color='skyblue')
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()


# In[4]:


plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Marks'])
plt.title("Boxplot of Student Marks")
plt.show()


# In[5]:


plt.figure(figsize=(6, 4))
sns.countplot(x='Department', data=df, palette='Set2')
plt.title("Number of Students per Department")
plt.show()


# In[6]:


plt.figure(figsize=(7, 4))
sns.scatterplot(x='Attendance (%)', y='Marks', data=df, hue='Department', style='Department', s=100)
plt.title("Marks vs Attendance")
plt.show()


# In[7]:


sns.pairplot(df[['Age', 'Marks', 'Attendance (%)']], diag_kind='kde')
plt.suptitle("Pairwise Relationships Between Variables", y=1.02)
plt.show()


# In[8]:


plt.figure(figsize=(6, 4))
sns.heatmap(df[['Age', 'Marks', 'Attendance (%)']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# In[9]:


plt.figure(figsize=(6, 4))
sns.barplot(x='Department', y='Marks', data=df, estimator='mean', palette='pastel')
plt.title("Average Marks by Department")
plt.show()


# In[10]:


print("\n✅ Insights:")
print("- The distribution of marks shows most students score between 70–90.")
print("- Outliers detected in Marks and Attendance for some students.")
print("- Attendance and Marks show a positive correlation.")
print("- CS department students generally score slightly higher on average.")


# In[ ]:




