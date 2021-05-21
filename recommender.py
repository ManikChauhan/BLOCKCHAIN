#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


columns = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('file.tsv', sep='\t', names=columns)
df.head()


# In[4]:


titles = pd.read_csv('Movie_Id_Titles.csv')
titles.head()


# In[5]:


df = pd.merge(df,titles,on='item_id')
df.head()


# In[6]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[7]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[8]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()


# In[9]:


ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# In[10]:


plt.figure(figsize=(10,5))
ratings['num of ratings'].hist(bins=100)


# In[11]:


plt.figure(figsize=(10,5))
ratings['rating'].hist(bins=100)


# In[12]:


sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)


# In[13]:


table = df.pivot_table(index='user_id',columns='title',values='rating')
table.head()


# In[14]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# In[15]:


ratings.head()


# In[18]:


rating1 = table['Scream (1996)']
rating2 = table['Mask, The (1994)']
rating3 = table['Braveheart (1995)']
rating1.head()


# In[19]:


similar1 = table.corrwith(rating1)
similar2 = table.corrwith(rating2)
similar3 = table.corrwith(rating3)


# In[20]:


corr1 = pd.DataFrame(similar1,columns=['Correlation'])
corr1.dropna(inplace=True)
corr1.head()


# In[21]:


corr1.sort_values('Correlation',ascending=False).head(10)


# In[22]:


corr1 = corr1.join(ratings['num of ratings'])
corr1.head()


# In[23]:


corr1[corr1['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[24]:


corr2 = pd.DataFrame(similar2,columns=['Correlation'])
corr2.dropna(inplace=True)
corr2 = corr2.join(ratings['num of ratings'])
corr2[corr2['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[25]:


corr3 = pd.DataFrame(similar3,columns=['Correlation'])
corr3.dropna(inplace=True)
corr3 = corr3.join(ratings['num of ratings'])
corr3[corr3['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:




