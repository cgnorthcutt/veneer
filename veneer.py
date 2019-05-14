#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3


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

# Only set this variable if you are running the crontab job multiple times per day
# In this example, this script will do nothing 40% of the time.
# This will make your activity appear more random if you run the crontab a few times a day.
do_nothing_prob = 0.3


# In[ ]:


if not os.path.isfile(fn):
    # Set-up file if it does not exist.
    with open(fn, 'w') as wf:
        print("{}".format(t.year), file = wf)
        print("{} ".format(months[t.month]), end = "", file = wf)
        for i in range(1, 1 + t.day):
            print("|" if i % 5 == 0 else "-", end = "", file = wf)
else if do_nothing_prob < random.random():
    # Append to file if it does exist
    with open(fn, 'a') as wf:
        if t.month == 1 and t.day == 1:
            print("\n{}".format(t.year), end = "", file = wf)
        if t.day == 1:
            print("\n{} ".format(months[t.month]), end = "", file = wf)
        if t.weekday() != 6 or random.random() < sunday_write_frac: # Only write on Sundays some fraction of the time.
            print("|" if t.day == 5 else "-", end = "", file = wf)

