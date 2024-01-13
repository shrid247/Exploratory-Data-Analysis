#!/usr/bin/env python
# coding: utf-8

# # 911 Calls Capstone Project

# For this capstone project we will be analyzing some 911 call data. The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)
# 
# Just go along with this notebook and try to complete the instructions or answer the questions in bold using your Python and Data Science skills!

# ## Data and Setup

# **Import numpy and pandas**

# In[1]:


import numpy as np
import pandas as pd


# **Import visualization libraries and set %matplotlib inline.**

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# **Read in the csv file as a dataframe called df**

# In[5]:


df=pd.read_csv(r"C:\Users\shrid\Downloads\911.csv")
df.head()


# **Check the info() of the df**

# In[7]:


df.info()


# **Check the head of df**

# In[8]:


df.head()


# ## Basic Questions

# **What are the top 5 zipcodes for 911 calls?**

# In[20]:


df['zip'].value_counts().head()


# **What are the top 5 townships (twp) for 911 calls?**

# In[21]:


df['twp'].value_counts().head()


# In[ ]:





# **Take a look at the 'title' column, how many unique title codes are there?**

# In[23]:


df['title'].nunique()


# ## Creating new features

# **In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS.**

# In[27]:


df['Reason']=df['title'].apply(lambda x:x.split(':')[0])
df.head()


# **What is the most common Reason for a 911 call based off of this new column?**

# In[29]:


df['Reason'].value_counts()


# **Now use seaborn to create a countplot of 911 calls by Reason.**

# In[30]:


sns.countplot(data=df,x='Reason')


# **Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?**

# In[32]:


df['timeStamp'].info()


# **You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects.**

# In[33]:


df.head(2)


# In[34]:


df['timeStamp']=pd.to_datetime(df['timeStamp'],format='%Y-%m-%d  %H:%M:%S')


# In[35]:


df['timeStamp'].info()


# **You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# **You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

# In[64]:


df[['Hour','Month','Day of week']]=  df['timeStamp'].apply(lambda x:pd.Series([x.hour,x.month,x.day_of_week]))
df.head()


# **Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week:**
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[66]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[67]:


df['Day of week']=df['Day of week'].map(dmap)
df.head()


# **Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.**

# In[69]:


sns.countplot(data=df,x='Day of week',hue='Reason')


# **Now do the same for Month:**

# In[71]:


sns.countplot(data=df,x='Month',hue='Reason')


# **Did you notice something strange about the Plot?**

# In[ ]:





# **You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas...**

# **Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame.**

# In[73]:


a=pd.DataFrame({'Month':range(1,13)})
m_df=pd.merge(a,df,on='Month',how='left')
sns.countplot(data=m_df,x='Month',hue='Reason')


# In[ ]:





# **Now create a simple plot off of the dataframe indicating the count of calls per month.**

# In[78]:


m_df.head()


# In[108]:


dmonth=m_df.groupby('Month').count()
dmonth.reset_index(inplace=True)


# In[110]:


sns.lineplot(x=dmonth['Month'],y=dmonth['lat'])


# In[99]:


sns.countplot(x=df['Month'])


# **Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column.**

# In[114]:


sns.lmplot(x='Month',y='lat',data=dmonth)


# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method.** 

# In[115]:


df.head(2)


# In[116]:


m_df.head(2)


# In[122]:


df['Date']=df['timeStamp'].dt.date


# In[123]:


df.head(2)


# **Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[124]:


a=df.groupby('Date').count()


# In[128]:


a['lat'].plot()


# **Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

# In[138]:


df['Reason'].value_counts()


# In[139]:


sns.lmplot(data=df, x='Month', y='lat', col='Reason', hue='Reason', col_wrap=3)


# In[ ]:





# **Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

# In[140]:


df.head(2)


# In[151]:


a=df.groupby(['Day of week','Hour']).count().unstack()['Reason']


# In[152]:


a


# **Now create a HeatMap using this new DataFrame.**

# In[156]:


sns.heatmap(a.corr())


# **Now create a clustermap using this DataFrame.**

# In[157]:


sns.clustermap(a.corr())


# **Now repeat these same plots and operations, for a DataFrame that shows the Month as the column.**

# In[ ]:





# In[ ]:





# In[ ]:





# 
# # Great Job!
