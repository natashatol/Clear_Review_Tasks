#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# creating the data to work with


# In[1]:


L = {'03/01/2020':   [('Check-in', 6), ('Wellbeing Conversation', 2), ('One-2-One', 2), ('Wellbeing Conversation1', 21), ('One-2-One2', 6)]}


# In[ ]:


#  returning dictionary


# In[2]:


L


# In[ ]:


# returning value from key as a list, creating loop to ensure if key is changed function still works


# In[3]:


for i in L:
    print(L[i])


# In[ ]:


# creating dictionary from list of values from key


# In[4]:


dict(L[i])


# In[5]:


# checking that if key is changed, the above still works


# In[6]:


L['04/20'] = L.pop('03/01/2020')
for i in L:
    print(L[i])
dict(L[i])


# In[ ]:




