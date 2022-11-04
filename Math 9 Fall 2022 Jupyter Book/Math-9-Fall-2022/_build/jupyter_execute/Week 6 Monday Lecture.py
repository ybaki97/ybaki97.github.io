#!/usr/bin/env python
# coding: utf-8

# # Week 6, Monday Lecture
# ## Here is a smaller title
# 
# __Today__:
# 
#  - Passed back checkpoint exams
#  - Announcements about Python Unit 1
#  - Getting started with Jupyter notebooks

# This is a markdown cell. I can put text here and format it nicely :)

# Something cool: I can even use LaTeX! $\LaTeX, f(x) = \int_0^1 x^2 dx$.

# In[1]:


This is a code cell. Notice if I try to run it, I get an error :(


# In[5]:


s = "Hello, World"
t = 'Hello, World'


# In[6]:


type(s)
type(t)


# In[7]:


print(type(s))
print(type(t))


# In[8]:


s


# Remember in MATLAB, if we wanted the first element of a vector v, we could do v(1). Here are the two main differences in Python:
#  - We use square brackets []
#  - Indexing starts at 0!

# In[9]:


s[1]


# In[11]:


s[-1]


# In[10]:


len(s)


# We've just seen some examples of strings in python, now let's see a very important data type called "list"

# In[12]:


mylist = [3,1,4,"Yasmeen","Hello","Help :("]


# In[13]:


type(mylist)


# In[14]:


mylist[0]


# In[15]:


type(mylist[0])


# In[16]:


mylist[-1]


# In[17]:


type(mylist[-1])


# In[18]:


mylist[-2]


# In[19]:


mylist.append("Happy Halloween!")


# In[20]:


mylist


# In[21]:


mylist[1] = 5


# In[22]:


mylist


# These next examples show something called "slicing"

# In[23]:


mylist


# In[24]:


mylist[0:4] #In python, we usually do not include the right endpoint


# In[26]:


mylist[:4]

