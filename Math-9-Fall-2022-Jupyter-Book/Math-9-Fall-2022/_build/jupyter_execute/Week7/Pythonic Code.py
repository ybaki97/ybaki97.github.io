#!/usr/bin/env python
# coding: utf-8

# # Pythonic Code

# ## List Comprehension

#  - Length 8 list of all 7s

#  - Let `mylist = [-1,4,2,3,-10,2,4]`. Square each element in `mylist`

#  - Get the sublist of `mylist` containing only even numbers

#  - Replace each negative number in `mylist` with 0

#  - Make the length 8 list of lists `[[0,1,2],[0,1,2], ...,[0,1,2]]`

#  - Make the length 24 list `[0,1,2,0,1,2,0,1,2,...,0,1,2]`

#   - Capitalize each word in the catalogue description of Math 9
#       
#       Introduction to computers and programming using Matlab and Python. Representation of numbers and precision, input/output, functions, custom data types, testing/debugging, reading exceptions, plotting data, numerical differentiation, basics of algorithms. Analysis of random processes using computer simulations.

# ## f-strings

# In[2]:


name = "yasmeen"
n = 13


# ## Lambda Functions

#  - Write a function `cap` that takes as input a string `s` and as output returns the same string `s` capitalized.

#  - Write a function `plus` that takes two inputs and adds them together.

#  - Make a $20 \times 3$ NumPy array of random letters, then concatenate each row of three letters into a single length-3 string using `np.apply_along_axis`.

#  - Let `tuplist` be the following list of tuples. Sort the list so that the numbers are increasing.

# In[3]:


import numpy as np


# In[6]:


A = np.ones((10,3))


# In[7]:


A


# In[9]:


B = np.array([4,5,6])


# In[12]:


B.shape


# In[14]:


(A + B).shape


# A: 10 x 3
# 
# B:  1 x 3
# 
# A+B:10 x 3

# 1.) If it's broadcastable, what are the dimensions of the resulting array?
# 
# 2.) Given an array of certain dimensions, can it be added,e.g., to an array of different dimensions

# In[17]:


A = np.ones(6)
A


# In[18]:


A + 6


# In[45]:


A = np.ones((3,4))
A


# In[46]:


B = np.array([1,2,3]).reshape(3,1)


# In[47]:


B


# In[48]:


A + B


# A : 3 x 4
# 
# B : 3 x 1
# 
# A + B: 3 x 4

# In[30]:


A + B


# A: 3 x 4
# 
# B: 1 x 4
# 
# A + B: 3 x 4

# In[ ]:


A + B


# In[41]:


A = np.arange(1,13).reshape(4,3)
A


# In[44]:


B = np.arange(1,5).reshape(1,4)
B


# A: 4 x 3 
# 
# B: 1 x 4
