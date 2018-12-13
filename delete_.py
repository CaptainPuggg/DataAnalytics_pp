
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


bigdf=pd.read_csv('Big.csv')
smalldf=pd.read_csv('Small.csv')


# In[22]:


for item in bigdf.columns:
    if item not in smalldf.columns:
        bigdf.drop(str(item), axis=1, inplace=True)

