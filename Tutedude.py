
# coding: utf-8

# # Task 1: Perform Basic Mathematical Operations

# In[ ]:


# 1.  Takes two numbers as input from the user.


# In[1]:


Number_1 = int(input('Enter the first number :'))
Number_2 = int(input('Enter the second number :')) 
addition = Number_1 + Number_2
print(addition)


# In[6]:


Number_1 = int(input('Enter the first number :'))
Number_2 = int(input('Enter the second number :')) 
subtraction = Number_1 - Number_2
print(subtraction)


# In[9]:


Number_1 = int(input('Enter the first number :'))
Number_2 = int(input('Enter the second number :')) 
multiplication= Number_1 * Number_2
print(multiplication)


# In[12]:


Number_1 = float(input('Enter the first number :'))
Number_2 = float(input('Enter the second number :')) 
division = Number_1 / Number_2
print(division)


# # Task 2: Create a Personalized Greeting

# In[ ]:


First_name = str(input('Enter your first name:'))
Last_name = str(input('Enter last name:'))
Full_name = ( First_name + " " +Last_name )
print('Hello', Full_name +"! "+ 'Welcome to the python program.')

