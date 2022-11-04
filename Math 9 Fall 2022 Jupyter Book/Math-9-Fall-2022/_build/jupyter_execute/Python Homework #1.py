#!/usr/bin/env python
# coding: utf-8

# # Python Homework #1

# ## Instructions
# In a group of 1-3 students, work on answering the following questions in a Jupyter notebook. Submit the ipynb file with your solutions to Canvas. You and your group members can submit the same assignment, but all of you should upload it individually to Canvas.

# ## Group Information
#  - Group Member 1:
#  - Group Member 2:
#  - Group Member 3:

# ## Question 1
# The following function `make_array` is supposed to take as input a positive integer `n` and as output return a length `n` NumPy array in which every value is `n`.  What is the major problem with the following definition?  (The answer is not something like, "it does not check that n is really a positive integer".)

# In[1]:


import numpy as np


# In[2]:


def make_array(n):
    print(np.zeros(n)+n)


# In[3]:


make_array(4)


# ## Question 2
# 
# * Make two NumPy arrays of length one hundred million, `A` and `B`, with `A` containing the integers 0 through 99,999,999 in order (Hint.  If you know how to make any object with these values in this order, you can then convert it to a NumPy array.), and with `B` containing the number `6.3` repeated one hundred million times.  
# * Using the Jupyter magic function `%%timeit`, time how long it takes to add `A` and `B` together.  (Do not define `A` and `B` in the same cell as where you add `A` and `B`.
# * Make the same computation using `time.time`.  (Don't expect the answers to be identical, but for this particular length, the numbers were pretty close when I tried it.  When I tried it with length one million, the times differed by about a factor of three.)

# ## Question 3
# 
# * Write a function `check_value` that takes as input `x` and as output returns `True` if -1 is in `x` and returns `False` if -1 is not in `x`.  (Hint.  You should not need an if statement... the whole function definition can be done in just two lines.)

# ## Question 4
# 
# * For the same value of `A` as above, convert `A` to a list and name it `listA`, and convert `A` to a set and name it `setA`.
# * Using `check_value`, how long does it take to check if -1 is in `A`?  (Use the Jupyter magic function `%%timeit` rather than the `time` module.)
# * Using `check_value`, how long does it take to check if -1 is in `listA`?
# * Using `check_value`, how long does it take to check if -1 is in `setA`?
# * If you have `listA` and you want to check if -1 is in it as fast as possible, it **does not** make sense to convert `listA` to a set and check in that set.  Do you see why not?
# * Start with `dictA = {}` (an empty dictionary), and using a for loop, put all of the numbers from `A` in as keys to this dictionary, and which has as values 3,8,3,8,... alternating.  For example, `dictA` will begin `{0: 3, 1: 8, 2: 3, ...}`.
# * Using `check_value`, how long does it take to check if `-1` is in `dictA`?
# * What is actually being checked when we ask `-1 in dictA`?  Are we checking if -1 is a key or if -1 is a value?  (Don't look this up.  Just try making a small dictionary to see.)
# * How do the timings compare the NumPy array, the list, the set, and the dictionary?  Are any two of them similar?

# ## Question 5
# 
# Import the `sys` library.  This library comes included with Python, so you do not need to install it (just import it).
# 
# Using `help`, what is the unit for the function `getsizeof` from the `sys` library?  Answer this question in a markdown cell.

# ## Question 6
# 
# Using the `getsizeof` function, check the size of each of the following.  Sort them from taking up the least space to taking up the most space.  Put the sorted list in a markdown cell.  (Don't try to automate the sorting, just sort them by hand, unless you're already a Python expert, then you could maybe use `sorted` together with the `key` keyword argument, but I haven't tried that to see if it actually works.)
# 
# * The integer 0.
# 
# * An empty list (you can create this using square brackets and putting nothing inside of them, or you can create this using the `list` function and not passing any arguments).
# 
# * A list containing the integers 1,2,3.
# 
# * A list containing the strings 1,2,3.
# 
# * The string "1,2,3".
# 
# * A set containing the integers 1,2,3.
# 
# * The dictionary containing keys 1,2,3 and containing only the value 0.
# 
# * A NumPy array containg the integers 1,2,3 (use the `dtype` of `np.int8`).
# 
# * A NumPy array containg the integers 1,2,3 (use the `dtype` of `np.int64`).
# 
# * The range object `range(0,10**100,3)`.
