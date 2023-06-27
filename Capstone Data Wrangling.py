#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First, import files and packages, both the dataset and pandas and numpy
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Ian's Second PC\Downloads\train.csv")
df.head()


# In[2]:


#Drop columns with large numbers of null values and measures that cannot be properly quantified.
df = df.drop("Alley", axis ='columns')
df = df.drop("Id", axis = 'columns')
df = df.drop("LandContour", axis = 'columns')
df = df.drop("MiscFeature", axis = 'columns') 
df = df.drop("MiscVal", axis = 'columns')
df = df.drop("PoolQC", axis = 'columns')
df = df.drop("Utilities", axis = 'columns')
df = df.drop("Fence", axis = 'columns')
#This column will be dropped due to having fewer observations than the rest of the data
df = df.drop("LotFrontage", axis = 'columns')
df.head()


# In[3]:


#drop all rows with null values to normalize data.
df.dropna(axis='rows')
df.head()


# In[4]:


#Investigate the data to determine outliers; in this particular case, outliers may require further investigation
#as there may be a relationship other than linear with land, square footage, etc.
df.describe()


# In[ ]:




