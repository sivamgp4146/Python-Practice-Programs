#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Create sample data
data = {
    'ID': [101, 102, 103, 104, 105, 105, 106, 107],
    'Name': ['John', 'Alice', 'Bob', 'John', None, 'Bob', 'Eve', 'ALICE'],
    'Age': [25, 30, None, 22, 28, 28, None, 30],
    'City': ['New York', 'Los Angeles', 'New York', None, 'Chicago', 'Chicago', 'Miami', 'los angeles']
}


# In[3]:


# Create DataFrame
df = pd.DataFrame(data)
print("Original Dataset:\n", df)


# In[4]:


print("\nChecking for Missing Values:")
print(df.isnull().sum())


# In[5]:


df_dropped = df.dropna()
print("\nAfter Dropping Missing Values:\n", df_dropped)


# In[6]:


# Fill missing names with 'Unknown' and ages with mean age
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)

print("\nAfter Filling Missing Values:\n", df)


# In[7]:


print("\nDuplicate Rows:")
print(df[df.duplicated()])


# In[8]:


df = df.drop_duplicates()
print("\nAfter Removing Duplicates:\n", df)


# In[9]:


# Convert all city names and names to title case
df['Name'] = df['Name'].str.title()
df['City'] = df['City'].str.title()

print("\nAfter Correcting Text Case:\n", df)


# In[10]:


print("\nUnique Names:", df['Name'].unique())
print("Unique Cities:", df['City'].unique())


# In[11]:


print("\n✅ Final Cleaned Dataset:\n", df)


# In[ ]:




