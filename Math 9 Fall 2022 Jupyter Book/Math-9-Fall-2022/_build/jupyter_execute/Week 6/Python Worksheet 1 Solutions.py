#!/usr/bin/env python
# coding: utf-8

# # Python Worksheet 1
# 
# Prerequisites: The videos from "Python data types".

# ## Question
# 
# Evaluate 3.3 divided by 1.1, and in the same line, convert the result to an integer (using `int`).  What is strange about the result?  Can you figure out why that happened?  What would you say is a lesson you can take away from this example?  (Answer these short answer questions in a markdown cell.)

# In[1]:


int(3.3/1.1)


# In[2]:


3.3/1.1


# In[3]:


int(1.1)


# In[4]:


int(1.5)


# In[5]:


int(1.99999)


# __Answer__: We would expect $3.3/1.1 = 3$, but Python returns 2! This is due to precision issues and loss of accuracy when calling `int()`. The takeaway is that we should be very careful with casting to integers, and maybe insteal use floor or ceiling.

# ## Question

# For each of the following data types, define `x` and `y` to be two objects of that data type, and try to combine them together using `+`. If they can be combined using `+`, try to explain what `x+y` represents in a markdown cell.  The first data type, `int`, has been done for you.

# * `int`

# In[6]:


x = 5
y = 3


# In[7]:


type(x)


# In[8]:


x+y


# **Explanation**.  In the case that `x` and `y` are integers, `x+y` represents ordinary addition of integers.

# * `float`

# In[9]:


x = 1.1
y = 2.2


# In[10]:


type(x)


# In[11]:


x + y


# In[12]:


type(x + y)


# __Explanation.__ In the case that `x` and `y` are floats, `x+y` represents floating point arithmetic. It is like regular arithmetic, but liable to precision issues.

# * `bool`

# In[13]:


x = True
y = False


# In[14]:


type(x)


# In[15]:


x + y


# In[16]:


type(x + y)


# In[17]:


y + y


# In[18]:


type(y + y)


# In[19]:


x + x + x


# __Explanation.__ In the case that `x` and `y` are boolean, `x + y` is an integer. The sum counts how many values are true.

# * `set`
# * `tuple`
# * `list`
# * `str`
# * `range`
# * `dict`

# ## Question

# The usual way to convert to a string is by using `str`.  For example, try to convert the integers 123 and -10 to strings using `str`.  (Be sure your inputs to the `str` functions are integers and not themselves strings.)

# In[20]:


str(123)


# In[21]:


str(-10)


# There are also some special built-in functions in Python that can be used to convert from an integer to a string, such as `bin`, `format`, and `chr`.  Each one has its own purpose. 

# Try converting those same integers, 123 and -10, into strings using the function `bin`.  Explain briefly the result.  (Use `help(bin)` to get information about this function.)

# In[22]:


bin(123)


# In[23]:


bin(-10)


# In[24]:


help(bin)


# Try converting those same integers, 123 and -10, into strings using `chr`.  (Hint.  One of the two will raise a `ValueError`.)

# In[25]:


type(chr(123))


# In[26]:


chr(-10)


# Can you figure out what is the maximum integer `n` for which `chr(n)` is defined?  The weird number in the error message is written neither in the usual decimal notation, nor in binary notation.

# In[44]:


def findn():
    n = 123
    while True:
        try:
            chr(n)
            n = n+1
        except:
            print(f"{n} is too large :/")
            return 


# In[45]:


findn()


# In[47]:


int("0x10ffff", base=16)


# In[41]:


help(chr)


# ## Question

# Define `n=100`.  In that case, `chr(n)` will be the letter `d`.  Check this.

# In[48]:


n = 100
chr(n)


# Find a value of ???, using `n` but not using the letter `d`, so that `print(???)` displays the string "100: d". (Hint: Combine two strings using `+` as in an earlier question.

# In[52]:


print("100:"+chr(n))


# For each integer `i` from 0 (inclusive) to 255 (inclusive), print `i` and `chr(i)` on the same line, as you just did for `n=100`.  Use a `for` loop.  (Don't worry if 0 through 32 look blank.  That is correct; they all represent whitespace, I believe.  For example, newline `"\n"` corresponds to 10; can you recognize that in the for loop?)

# In[53]:


for i in range(256):
    print("i:"+chr(i))


# ## Question
# 
# It also makes sense to go the other direction, from strings to integers.  Try evaluating `int("1101")`, `int("1101", 2)`, `int("1120", 2)`, and `int("1120", 3)`.  Using a markdown cell, explain in your own words the meaning of the results, for example, why does `int("1120", 3)` produce the number `42`?  (Hints.  One of these will again raise an error.  Like usual, you can use `help(int)` to get information.)

# __Explanation.__ `int(string, base)` converts the string to the specified base to decimal. For example, to convert 1120 in base 3 to base 10, we compute $0*1 + 2*3 + 1*9 + 1*27 = 42$.

# In[54]:


int("1101")


# In[55]:


int("1101",2)


# In[56]:


int("1120",2)


# In[57]:


int("1120",3)


# For what value of `m` is `int("1120", m)` the same as `int("1120")`?

# In[58]:


int("1120",10)


# In[59]:


int("1120")


# What is a value of `x` such that the following produces the letter "d"? `chr(int(x,2))`

# We know that in base 10, `chr(100)` gives the letter "d". We convert 100 to base 2: $$100 = 64 + 32 + 4 \Rightarrow 1100100$$

# In[61]:


chr(int("1100100",2))

