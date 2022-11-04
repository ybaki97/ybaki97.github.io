#!/usr/bin/env python
# coding: utf-8

# # Python Worksheet 1
# 
# Prerequisites: The videos from "Python data types".

# ## Question
# 
# Evaluate 3.3 divided by 1.1, and in the same line, convert the result to an integer (using `int`).  What is strange about the result?  Can you figure out why that happened?  What would you say is a lesson you can take away from this example?  (Answer these short answer questions in a markdown cell.)

# ## Question

# For each of the following data types, define `x` and `y` to be two objects of that data type, and try to combine them together using `+`. If they can be combined using `+`, try to explain what `x+y` represents in a markdown cell.  The first data type, `int`, has been done for you.

# * `int`

# In[1]:


x = 5
y = 3


# In[2]:


type(x)


# In[3]:


x+y


# **Explanation**.  In the case that `x` and `y` are integers, `x+y` represents ordinary addition of integers.

# * `float`
# * `bool`
# * `set`
# * `tuple`
# * `list`
# * `str`
# * `range`
# * `dict`

# ## Question

# The usual way to convert to a string is by using `str`.  For example, try to convert the integers 123 and -10 to strings using `str`.  (Be sure your inputs to the `str` functions are integers and not themselves strings.)

# There are also some special built-in functions in Python that can be used to convert from an integer to a string, such as `bin`, `format`, and `chr`.  Each one has its own purpose. 

# Try converting those same integers, 123 and -10, into strings using the function `bin`.  Explain briefly the result.  (Use `help(bin)` to get information about this function.)

# Try converting those same integers, 123 and -10, into strings using `chr`.  (Hint.  One of the two will raise a `ValueError`.)

# Can you figure out what is the maximum integer `n` for which `chr(n)` is defined?  The weird number in the error message is written neither in the usual decimal notation, nor in binary notation.

# ## Question

# Define `n=100`.  In that case, `chr(n)` will be the letter `d`.  Check this.

# Find a value of ???, using `n` but not using the letter `d`, so that `print(???)` displays the string "100: d". (Hint: Combine two strings using `+` as in an earlier question.

# For each integer `i` from 0 (inclusive) to 255 (inclusive), print `i` and `chr(i)` on the same line, as you just did for `n=100`.  Use a `for` loop.  (Don't worry if 0 through 32 look blank.  That is correct; they all represent whitespace, I believe.  For example, newline `"\n"` corresponds to 10; can you recognize that in the for loop?)

# ## Question
# 
# It also makes sense to go the other direction, from strings to integers.  Try evaluating `int("1101")`, `int("1101", 2)`, `int("1120", 2)`, and `int("1120", 3)`.  Using a markdown cell, explain in your own words the meaning of the results, for example, why does `int("1120", 3)` produce the number `42`?  (Hints.  One of these will again raise an error.  Like usual, you can use `help(int)` to get information.)

# For what value of `m` is `int("1120", m)` the same as `int("1120")`?

# What is a value of `x` such that the following produces the letter "d"? `chr(int(x,2))`
