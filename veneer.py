#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import random


# In[2]:


sunday_write_frac = 0.75

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
months = dict(zip(range(1, 1 + len(months)), months))

t = datetime.datetime.today()
y = t.year
m = t.month
d = t.day
w = t.weekday() # Saturday is 5, Sunday is 6


# In[3]:


with open('README.md', 'a') as wf:
    if t.month == 1 and t.day == 1:
        print("\n{}".format(t.year), end = "", file = wf)
    if t.day == 1:
        print("\n{} ".format(months[t.month]), end = "", file = wf)
    if t.day != 6 or random.random() < sunday_write_frac: # Only write on Sundays some fraction of the time.
        print("|" if t.day == 5 else "*", end = "", file = wf)

