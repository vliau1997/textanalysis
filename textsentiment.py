#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install textblob')


# In[4]:


from textblob import TextBlob


# In[5]:


f = open("News.txt")


# In[8]:


d = f.read()


# In[10]:


print(d)


# In[11]:


TextBlob(d).sentiment


# In[ ]:




