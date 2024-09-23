'''a=float(input("Please enter your name :- "))
b=float(input("please enter your age :- "))

    
      
if  a==b or a>b :
  print(a+b)
elif a<b or a!=b :
  print(a-b)
elif a>b or a!=b :
  print(a*b)
else:
  print("this function is not define by the user and very lenth of the system")
  

#simple function

def simplefunction():
    print("welcome to adhyan tech for learning the AI and Machine")
simplefunction()
simplefunction()

#function with argument

def sum(a,b):
    print(a+b)

sum(20,50)
sum(200,100) 


#function with argument

def sum(a,b=1):
  print(a+b)

sum(30)
sum(30,50)
'''
'''
#user define function

def square(x):
   return x*x,x*2

  
s=square(5)
print(s)


#module is the library of the function ,class and all in all and its we used any time form your code because its look like used a library
def sum (a,b)
  c=a+b
  return c
def mul (a,b):
  c=a*b
  return c

'''
#module name is also called file name (module name=file name)
'''
#module function define

def sum(a,b)
 c=a+b
 return c

def mul(a,b)
   c=a+b
   return c

#module function used
   import 



#call the module for this way
import module2
   print(module2.sum(10,20))
   print(module.mul(10,20))

  # note = #making Alias with because you will be the shor name of the module
   
   
#with the help of =from call the module

from module2 import sum
   print(sum(10,20))

from module2 import *  # with the help of * you will call all module of the pages
   print(sum(10,20))

'''

#import the math module
'''
x=-10.25

import math
print(math.ceil(x))

a=-10
print(math.fabs(a))

b=5
print(math.factorial(b))

c=10.5
print(math.floor(c))

d=[20,30,40]
print(math.fsum(d))

e=25
print(math.sqrt(e))

'''

#random module

import random

a=["apple","banana","cherry"]
print(random.choice(a))

n=random.randint(2,8)
print(n)

v=random.randrange(2,4)
print(v)

e=[10,20,30,40]
print(random.choice(e))

f=random.random()
print(f)


z=[10,20,30,40]
random.shuffle(z)
print(z)

u=random.uniform(3,9)
print(u)





































