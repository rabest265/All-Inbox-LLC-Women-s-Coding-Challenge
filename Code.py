#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import os
import pandas as pd


# In[2]:


# Create location of the input and output files
in_path = os.path.join("Resources","mbox.full")
# in_path = os.path.join("Resources","mbox_example")
out_path = os.path.join("Output","output.full")


# In[3]:


# Read the mbox.full file and save it into a list labeled full_text
text_file = open(in_path, "r")
full_text = text_file.readlines()
text_file.close()


# In[4]:


# Count the number of emails
email_numb = 0
for row in full_text:
    if "From " in row:
        email_numb += 1
print (email_numb)


# In[5]:


# Create an empty dictionary of the current emails and the new version of the emails
emails = {}
for email in range (0,email_numb):
    emails[email] = []
print (emails)


# In[6]:


# Create the dictionary of emails using the rows of the full_text
email_count = -1
for row in full_text:
    if "From " in row:
        email_count += 1
    emails[email_count].append (row)
print(emails [0])


# In[7]:


# Create an empty list to store the # of header rows
headers = []
# go through each email and return the row number of the row with the Subject line
for email in emails:
    header_count = 0
    # Added a check to make sure it is the first blank line in the email
    check = False 
    #Iterate through every row of the email
    for row in emails[email]:
        header_count += 1
        if row == '\n' and check == False:
            headers.append (header_count)
            check = True
print (headers)


# In[8]:


# Set up the new_full_text to hold the backwards text
new_full_text =[]
# Create some empty lists to temporarily store the emails both forward and backward
email_forw = []

# Run through the emails and store them forwards in the email_forw temporarily and then print them back backwards
for email in emails:
    # First we need the number of rows in each email
    length = len(emails[email])    # If the it is the last email (email = email numb the ending is 2 rows instead of three)
    # So we will set up conditional ending range
    if email == email_numb-1:
        end = 2
    else:
        end = 3
    

    # Go through each row of the email and put it into the temporary list
    for row in emails[email]:
        email_forw.append (row)
    # First append all the header lines of code
    for counter in range (0, headers[email]):
        new_full_text.append (emails[email][counter])
        
    # Next append all the remaining lines of code backwards except the last three lines
    for counter2 in range (end + 1, length - headers[email] + 1):
        back_count = (length - counter2) # This will get us the backwards count
        new_full_text.append (emails[email][back_count])
    # Next append the last three lines
    if end == 3: new_full_text.append (emails[email][length - 3])
    new_full_text.append (emails[email][length - 2])
    new_full_text.append (emails[email][length - 1])
    # Reset the temp email list
    email_forw = []
    
print (new_full_text)


# In[9]:


# Export the new_full_text and save it
new_text_file = open(out_path, "w")
for row in new_full_text:
    new_text_file.write (row)
new_text_file.close()


# In[ ]:




