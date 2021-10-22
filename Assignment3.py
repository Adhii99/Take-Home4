#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


with open("input.txt", encoding="utf8") as file:  
    data = file.read() 


# In[3]:


data


# In[4]:


q_3_1 = data.find("is")


# In[5]:


print("Number of is in data : "+ str(q_3_1))


# In[6]:


string = data

q_3_2 = [int(i) for i in string.split() if i.isdigit()]


# In[7]:


print(str(q_3_2))


# In[8]:


# Program to find most frequent used Numbe
# element in a list
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
q_3_3 = most_frequent(q_3_2)
print("The Most Frequently Used Number : "+ str(q_3_3))


# In[9]:


import re
[m.start() for m in re.finditer('1603', data)]


# In[10]:


q_3_4 = "Year"
print("The Most frequent Number is used first time in the text is : "+ q_3_4)


# In[11]:


print(data[44008:44750])
print(data[47070:47257])
q_3_5 = "Cervantes"


# In[12]:


print("Number of is in data : "+ str(q_3_1))
print("The Number of Instances of Continues Numbers in Data is : " + str(len(q_3_2)))
print("The Most Frequently Used Number : "+ str(q_3_3))
print("The Most frequent Number is used first time in the text is : "+ q_3_4)
print("The Number close to Event is Describing about : "+ q_3_5)

