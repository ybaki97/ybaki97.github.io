#!/usr/bin/env python
# coding: utf-8

# # Week 7, Monday Lecture

# The focus on this week will be on NumPy. We have already seen this library during Week 6, but let us know if you are having any trouble getting it installed.

# __Reminders:__
# 
#  - No lecture on Friday, November 11th. 
#  - Python Homework #2 will be assigned during Wednesday this week. It will be due Friday of Week 8, so you have a little extra time to work on it.
#  
# __Today:__
#  
#  - Creating regular arrays in NumPy
#  - Random numbers in NumPy
#  
#  ***

# In[1]:


import numpy as np


# ## Regular Arrays

# What do we mean by regular? We mean that the arrays follow some kind of pattern.
# 
# How could we make the following NumPy arrays?

#  - `[0,0,...]` total length 13

# In[2]:


np.zeros(13)


# In[4]:


np.zeros(13).shape


# In[5]:


np.zeros(13, int)


# In[8]:


arr = np.zeros(13, dtype=np.int8)


# In[9]:


type(arr)


# In[10]:


[0 for _ in range(13)] #list comprehension


# In[12]:


np.array([x for x in range(13)])


# In[13]:


[0]+[0]


# In[14]:


[0] + [0] + [0]


# In[17]:


[0]*13


#  - A $3 \times 5$ array of all 7's

# In[23]:


np.zeros((3,5), int)+7 #shape needs to be a tuple


# In[27]:


np.ones((3,5),int)*7


# In[26]:


np.array([7]).shape


# In[20]:


help(np.zeros)


#  - An array of the form `[0,...,50]` of 6 evenly spaced points.

# In[28]:


np.linspace(0,50,6)


# We probably won't ever use linspace again for this class, but I just wanted you to see how many MATLAB functions are available in NumPy.

#  - The $4 \times 4$ array 
#  $$
#  \begin{pmatrix}
#  0 & 0 & 0 & 0 \\
#  1 & 1 & 1 & 1 \\
#  2 & 2 & 2 & 2 \\
#  3 & 3 & 3 & 3
#  \end{pmatrix}
#  $$

# Let's first practice with some indexing before we try making this array with a for-loop...

# In[48]:


A = np.zeros((4,4),int) #Initializing A to be all zeros
for x in range(4):
    A[x] = x


# In[49]:


A


# In[36]:


A = np.arange(16).reshape(4,4)
A


# In[37]:


#Some special indexing notation! 
A[0] #Returns the entire 0th row!


# In[38]:


A[1]


# In[39]:


A[2]


# In[41]:


A[-1]


# In[42]:


A[3]


# What if I wanted to get an entire column instead?

# In[43]:


A


# In[44]:


A[:,0]


# In[30]:


np.arange(16) #notice how similar this is to regular range(16)!


# In[32]:


np.arange(16).reshape(4,4)


# In[33]:


np.arange(16).reshape(2,8)


# In[34]:


np.arange(16).reshape(8,2)


# In[35]:


np.arange(16).reshape(3,5)


# In[31]:


list(range(16))


#  - The $2 \times 5$ array 
#  $$
#  \begin{pmatrix}
#  1 & 3 & 5 & 7 & 9 \\
#  11 & 13 & 15 & 17 & 19
#  \end{pmatrix}
#  $$

# In[56]:


np.arange(1,20,2)


# In[58]:


np.arange(1,20,2).reshape(2,5)


# In[57]:


np.arange(1,19,2)


# In[50]:


np.arange(10)


# In[51]:


help(np.arange)


# In[54]:


range(1,10,0.5)


# In[55]:


np.arange(1,10,0.5) #Here is one difference using arange! Non-integer step size! 


# ***

# ## Random Numbers!
# ... and a small introduction to object-oriented programming.

#  - Instantiate a random number generator in NumPy

# In[2]:


rng = np.random.default_rng()


# In[60]:


type(rng)


# In[61]:


rng.random()


# __We didn't get to the material below during the lecture, but here are some ways you could solve the problems__

#  - Make a length 13 array of random integers between 3 (inclusive) and 29 (exclusive).

# In[4]:


arr = rng.integers(3,29,13)


#  - Choose 10 of the numbers from the above array (with replacement) and put them into a new array.

# In[6]:


rng.choice(arr,10)


#  - Make a $3 \times 5$ array of random real numbers between -13 and 24.

# In[17]:


A = 37*rng.random((3,5))-13
A


# In[18]:


A.max()


# In[19]:


A.min()


# In[20]:


A.shape

