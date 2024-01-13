#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# 
# **Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.**

# 'Ecommerce Purchases.csv'

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


ecom=pd.read_csv(r"C:\Users\shrid\Downloads\Day 4 Files\Ecommerce Purchases.csv")


# In[ ]:





# **Check the head of the DataFrame.**

# In[4]:


ecom.head()


# **How many rows and columns are there?**

# In[12]:


rows=len(ecom.axes[0])
column=len(ecom.axes[1])
print(f'nof of rows is {rows} and no of column is {column}')


# **What is the average Purchase Price?**

# In[14]:


ecom['Purchase Price'].mean()


# **What were the highest and lowest purchase prices?**

# In[16]:


ecom['Purchase Price'].agg([max,min])


# In[ ]:





# **How many people have English 'en' as their Language of choice on the website?**

# In[20]:


(ecom['Language']=='en').sum()


# **How many people have the job title of "Lawyer" ?**
# 

# In[21]:


ecom.head()


# In[22]:


(ecom['Job']=='Lawyer').sum()


# **How many people made the purchase during the AM and how many people made the purchase during PM ?**
# 
# **(Hint: Check out [value_counts()]**

# In[23]:


ecom['AM or PM'].value_counts()


# In[ ]:





# In[ ]:





# **What are the 5 most common Job Titles?**

# In[28]:


ecom['Job'].value_counts().head(5)


# **Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?**

# In[29]:


ecom.head()


# In[41]:


ecom.loc[ecom['Lot']=='90 WT','Purchase Price']


# **What is the email of the person with the following Credit Card Number: 4926535242672853**

# In[40]:


ecom.loc[ecom['Credit Card']==4926535242672853,'Email']


# **How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[49]:


len(ecom[(ecom['CC Provider']=='American Express')& (ecom['Purchase Price']>95)])


# In[56]:


result = ecom.query("`CC Provider` == 'American Express' and `Purchase Price` > 95")
print(result.shape[0])


# In[57]:


ecom.head()


# In[ ]:





# **Hard: How many people have a credit card that expires in 2025?**

# In[98]:


ecom['CC Exp Date']=pd.to_datetime(ecom['CC Exp Date'],format='%m/%Y')


# In[18]:


ecom['CC Exp Date'] = ecom['CC Exp Date'].apply(lambda x: x.replace('/','/20'))


# In[23]:


ecom_exp = pd.to_datetime(ecom['CC Exp Date'],format='%m/%Y')
len(ecom[ecom_exp.dt.year == 2025])


# In[99]:


len(ecom[ecom['CC Exp Date'].dt.year==2025])


# In[5]:


ecom[ecom['CC Exp Date'].apply(lambda x:x[3:])=='25'].count()


# In[6]:


ecom.info()


# **Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)** 

# In[101]:


ecom['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()


# In[ ]:





# # Great Job!
