#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5


# In[2]:


print(x)


# In[3]:


x


# In[4]:


name = 'Ryan'


# In[5]:


type(name)


# In[6]:


type(x)


# In[7]:


T


# In[8]:


T = True


# In[9]:


F = False


# In[10]:


F


# In[12]:


my_list = [1,2,3,4]
print(my_list)


# In[13]:


my_list = ['list','of','strings']


# In[14]:


1+1


# In[15]:


4*5


# In[16]:


5**2


# In[17]:


5^2


# In[18]:


5^4


# In[25]:


a = T
if a: 
    print('It is true!')
    print('Also print this shit.')
    
else:
    print('That is bullshit!')
print('Always print this garbage.')    


# In[26]:


a = T
b = T
if a: 
    print('It is true!')
    print('Also print this shit.')
    if b: 
        print('A and B are True')
else:
    print('That is bullshit!')
print('Always print this garbage.')   


# In[ ]:


print('Hello, World!')


# In[27]:


def multiplyByThree(val):
    return 3 * val

multiplyByThree(4)


# In[31]:


a = [5,12,13,0]

def appendFour(myList):
    myList.append(4)
    
appendFour(a)
print(a)


# In[42]:


class Dog:
    def __init__(self, name): 
        self.name = name
        self.legs = 4
        
    def speak(self):
        print(self.name + '  Says: BARK!')


# In[43]:


my_dog = Dog('Rover')
another_dog = Dog('Missy')


# In[44]:


my_dog.speak()


# In[46]:


another_dog.speak()


# In[48]:


round(1.2-1.0,4)


# In[49]:


14/3


# In[50]:


round(14/3,6)


# In[51]:


14%2


# In[52]:


14%3


# In[ ]:




