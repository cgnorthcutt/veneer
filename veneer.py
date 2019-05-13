#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import random
import os


# In[ ]:


fn = 'veneer.txt'
sunday_write_frac = 0.75

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
months = dict(zip(range(1, 1 + len(months)), months))

t = datetime.datetime.today()


# In[ ]:


if not os.path.isfile(fn):
    # Set-up file if it does not exist.
    with open(fn, 'w') as wf:
        print("{}".format(t.year), file = wf)
        print("{} ".format(months[t.month]), end = "", file = wf)
        for i in range(1, 1 + t.day):
            print("|" if i % 5 == 0 else "_", end = "", file = wf)
else:
    # Append to file if it does exist
    with open(fn, 'a') as wf:
    if t.month == 1 and t.day == 1:
        print("\n{}".format(t.year), end = "", file = wf)
    if t.day == 1:
        print("\n{} ".format(months[t.month]), end = "", file = wf)
    if t.weekday() != 6 or random.random() < sunday_write_frac: # Only write on Sundays some fraction of the time.
        print("|" if t.day == 5 else "-", end = "", file = wf)

