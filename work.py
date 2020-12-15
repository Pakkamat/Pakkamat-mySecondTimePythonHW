#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
aaa = ["hangman", "teacher", "helloworld"]
n = random.randint(0, (len(aaa) - 1))
word = aaa[n]
y = ''
turns = 8
while turns > 0:
    failed = 0
    # Print the words that contain in word put in y
    for i in word:
        if i in y:
            print(i, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    # If u have all word == Win
    if failed == 0:
        print(">> You survived !")
        break
    x = input("Input a letter: > ")
    # put x in y
    y += x
    # x not in word turns or times -1
    if x not in word:
        turns -= 1
        print("No such letter in the word")
    #print("You have", + turns, 'lives')
    # if turn = 0 >>> lose
    if turns == 0:
        print("You hanged")


# In[19]:


a = int(input())
x = int(input())
#a = x | ex a = 3 , x = 3
while True:
    y = (x+ a/x) / 2
    if y == x:
        print(x)
        break
    x = y


# In[35]:


import math  
x = int(input())
print(math.sqrt(x))  


# In[34]:


import numpy as geek  
arr = geek.array([1, 3, 4, 7, 9]) 
   
print("Input array  : ", arr) 
print("First order difference  : ", geek.diff(arr)) 
print("Second order difference : ", geek.diff(arr, n = 2)) 
print("Third order difference  : ", geek.diff(arr, n = 3)) 


# In[ ]:




