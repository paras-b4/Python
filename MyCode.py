
'''
python is one of the fastest growing language in term of:
 1.Numbers of developers using it
 2.Numbers of libraries present in python
 3.Number of Companies using it
 4.it is used in many areas
 -Machine Learning
 -GUI
 -Software Development
 -Web Development
 5. Python is also Known as General purpose programing language
 Yes, Python is a general-purpose programming language.
  This means it is not limited to a specific domain and can be used for various types of applications, including:

 6.Python supports Procedure-oriented-programing ,Object-oriented-programing ,Functional programing .
 7.Python Language was introduced by Guido van Rossum.

# In python print is a built-in function just we have to call it . it is use to display the output
print(2+3) # Addition
print(9-8) # Subtraction
print(4*6) # Multiplication
print(8/2) # Division give us quotient with float
print(5/3) #  Division give us quotient
print(5//3) # Floor Division or int division gives us a quotient without float
print(5%2) # Modulus gives us Remainder
print(4%2)
print(8+9-10*0) # Expression
print((8+9)-10*0) # Expression
print(2 ** 3) # Power of two .


# string is a sequence of character enclosed inside a single or double quotes . strings are immutable .
print('paras')
print("paras's mobile") # we cannot use same quotes inside it .
print("paras 'laptop' ")
print ("paras\"s 'PC'")
print("paras\"s \"laptop")
print('paras ' + 'yadav')
print('paras'*10)
print('c:\docs\paras')
print('c:\docs\navin') # backslash(\n) means newline end=' ' means add string at the end or same line . we can use r before the string
print(r'c:\docs\navin') # r means Raw .

x=2
print(x+3)
y=3
print(x+y)
x=9
print(x+y)

name='paras Yadav'
print(name)
print(name + " yadav")
print(name[-1])# minus indexing starts from last
print(name[: :-1]) # print values in reverse order
print(name[: :2]) # print values with difference of 2
print(name[-4:-5]) # it will give nothing because it will go out of range
print(name[4:5])
print(len(name)) # gives us the length of the variable

# List are used to store multiple items in a single variable .items are enclosed inside the square brackets . List are mutable or changeable
nums=[9,8,6,7,2,1,3,5,10]
nums[0]=90  # we can change the value using index in List
print(nums)
print(nums[2:])
print(nums[::-1])
print(nums[-1])


names=['paras','john','krish','krian','parker','peter']
mil=[nums + names]
print(mil)

nums.append(100) # it will add the single element at the end of the list .
nums.insert(0,1000) # it will insert the element in between or at specific index in a list .
nums.extend([5,10,20,30]) #it will add multiple element at the end of the list .
nums.remove(1000) # it will remove the specific element from a list .
nums.pop(2) # it will remove the element from the specific index in a list .
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))

# Tuple are used to store multiple items in a single variable .items are enclosed inside the round brackets. Tuples are Immutable
# Tuple is like List but we cannot change the value of it . Execution of tuple is faster than the List .
nums=(10,20,30,5,9,8,6,4,3,1)
# nums[0]=0  In Tuple we cannot change the value
print(nums.count(10)) # gives the no of time a particular element repeate in the tuple .
print(nums.index(9)) # gives the index of the particular item .
print(max(nums))
print(len(nums))
print(nums[-1])
names=('paras','john','peter','parker','steve')
mils=(nums + names)
print(mils)


# Set is used to store multiple items in a single variable . it does not allow duplicate value . it does not supports indexing
# Set stored items in an unordered form .
s={9,30,52,6,42,7,11,100,12,11,8,25}
Set={22,25,14,21,5}
print(s.intersection(Set))

print(Set.union(s))
// in python we use discard and remove for deleting the element but in case if an element is not present in the list then discard not thorw error but remove throw exception .
s.discard(100)
print(s.pop()) # pop does not take any index because set does not support indexing so it pop the random elements from the set .
s.remove(25)
s.update(Set)  # if we want to add to set we use update function
print(s)
print(Set)
s.add(99)
s.union(Set)
nums= s.copy() # if we want to copy one set from another set we use copy() .
print(nums)
print(s)
# print(s[0]) set does not supports indexing so we cannot fetch the elements from the set .

nums=[9,5,4,6,3,8,7,0]
print(set(nums)) # Converting Lists to a set.

nums1=[95,'paras',99,'disha',[5,25,35,45,50]]
print('this is a List ',str(nums1))
print(tuple(nums1)) # Converting List to a Tuple.

nums=[1,6,8,9,4,4,5,6,1,8,5]
lst=[]
for i in nums:
    print(i,end=' ')

    if i not in lst:
        lst.append(i)
for j in lst:
    print()
    print(j,end=' ')

# Dictionary is a group/Collection of key-value pairs.where keys are unique and immutable and values can be duplicate and mutable .
# In Dictionary we can fetch values with the help of keys .

data={1:"paras",2:'kiran',3:'harsh',4:'navin'}
print(data[4])
print(data.get(5)) # gives None. if fetch the value that does not exist using get method then it will give us None otherwise error .
# print(data[5])  gives error
keys=['paras','kiran','harsh','james']
values=['java','python','Ruby','c']
data=dict(zip(keys,values))
data['Monika']='kotlin' # this is how we add key and values in dictionary
del data["james"]  # here we delete the key and value automatically deletes
print(data)

prog={'js':'Atom','cs':'vs','python':['pycharm','sublime'],'java':{'JEE':'eclipse','JSE':'intellij'}}
print(prog['java']['JSE'])
print(prog['python'][0])
print(prog.keys())
print(prog.values())
# DataType simple describes the type of the variable .
in python we use none instead of null .
# Built-in data type are 1.Numeric (integer,float,complex) 2.Boolean(bool) 3.String 4.collection (Range,List,Tuple,Set,Dictionary)
# User-define data type are 1.graph ,tree ,LinkedList ,Stack ,Queue .
nums= 2.4
print(type(nums))
nums=5
print(type(nums))
nums=2+5j
print(type(nums))
nums='paras'
print(type(nums))
nums=(8,9,5,4,7,6,2,3,1,0,10,8,9,5,6)
print(type(nums))
a=4
b=5
print(type(a<b)) # gives true
print(int(True)) # gives 1
print(range(10,-1))
print(type(range(10)))
print(list(range(2,10,2)))

# Types of Operators 1.Arithmatic 2.Assignment 3.Logical 4.Relational/comparison 5.Unary
# Arithmatic operator are used to perform mathematical operation like addition ,subtraction ,multiplication ,division
print("Arithmetic Operator")
a=20
b=15
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b)
a+=1
print(a)
b+=5
print(b)
# Assignment operator are used to assign a value to a variable . with the help of equal(=)
print("Assignment Operator")
a=10
a+=5
print(a)
a-=2
print(a)
a*=2
print(a)
a/=3
print(a)
a**=2
print(a)
b=32
b >>= 4 # right shift
print(b)
b <<=2 # left shift
print(b)
# Comparison is performed with the help of Relational operator . Comparison operator return a boolean value either true ofs false .
print(" Relational operator ")
a,b=10,15
c=a==b
print(c)
c=a!=b
print(c)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# Unary operator takes a single operand as a statement or expression .
print("unary operator")
a=10
print(-a)
# if you want to combine two or more condition and then check the relation between them .then logical operator are used .
# Logical operator include AND, OR and NOT .
print("Logical operator")
a,b=5,4
print( a>2 and b<5)
print( a>2 or b<5)
print( not(a>2) )
# Identity Operator checks/Compare the variable on the bases of their id .
print("Identity Operator")
a=[1,2,3]
b=[1,2,3]
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a is not b)
# Membership Operator are used to check weather the element is present in the sequence or not .
print("Membership operator")
a=['apple','banana','mango','melon']
b=['melon']
print(b in a)
print(b not in a)
# Bitwise operator
print("Bitwise operator")
x=9
x&=3
print(x)
x|=5
print(x)
x^=6
print(x)
y=10
print(~y)
y>>2
print(y)
y<<3
print(y)

# Import Math function .
import math as m
x=m.sqrt(99)
print(x)
x=8.1
x=m.ceil(x)
print(x)
x=6.9
x=m.floor(x)
print(x)
from math  import pow
x=pow(3,2)
print(x)

# Swap two no in different ways .
# with using third variable
a=5
b=6
print("before swapping no are ","a =",a ," ",'b = ', b)
temp=a
a=b
b= temp
print("after swapping no are ","a =",a ," ",'b = ', b)

# without using third variable
a=9
b=7
print("before swapping no are ","a =",a ," ",'b = ', b)
a=a+b # 9+7=16
b=a-b # 16-7=9
a=a-b # 16-9=7
print("after swapping no are ","a =",a ," ",'b = ', b)

# Assignment operator
a,b=10,20
print("before swapping no are ","a =",a ," ",'b = ', b)
a,b=b,a
print("after swapping no are ","a =",a ," ",'b = ', b)

# using xor function
a=19
b=72
print("before swapping no are ","a =",a ," ",'b = ', b)
a=a^b
b=a^b
a=a^b
print("after swapping no are ","a =",a ," ",'b = ', b)



# user input
x= int(input("enter first no"))
y= int(input("enter second no "))
z=x+y
print("sum of two number is : "+ z)

result =eval(input("enter an expression")) # we can evaluate expression by using eval function .
print(result)
'''
from tkinter.font import names
from traceback import print_tb

from IPython.core.ultratb import ListTB
from django.db.models.fields import return_None
# import sys
# x=int(sys.argv[1])
# y=int(sys.argv[2])
# z=x+y
# print(z)
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
#
# i=0
# for i in range(5):
#     j = 0
#     for j in range(5):
#
#             print("* ",end="")
#     print()


# @ @ @ @ @
# @ @ @ @
# @ @ @
# @ @
# @
# i=5
# j=5
# while(i>0):
#     j=i
#     while(j>0):
#         print("@ ",end="")
#         j-=1
#     i-=1
#     print()

# ******
#  *****
#   ****
#    ***
#     **
#      *
#
# for i in range(0,6):
#     print(" "*i,end="")
#     for j in range(6-i):
#
#         print("*",end="")
#
#     print()

#
# #####
#  ####
#   ###
#    ##
#     #
# i=0
# while(i<5):
#     print(" "*i,end="")
#     j=5-i
#     while(j>0):
#         print("#",end="")
#         j-=1
#     i += 1
#     print()

# # # # #
 # # # #
  # # #
   # #
    #
# i=0
# while(i<5):
#     print(" "*i,end="")
#     j=5-i
#     while(j>0):
#         print("# ",end="")
#         j-=1
#     i += 1
#     print()

# check a no is prime or not .
# num =int(input("Enter a no "))
# for i in range(2,num-1):
#     if((num%i)==0):
#         print(num,"is not prime")
#         break
# else:
#     print(i,"prime")

# num=100
# for i in range(2,num-1):
#     if(num%i==0):
#         pass
#     else:
#         print(i,"prime")

# * * * * *
# * * * *
# * * *
# * *
# *

# num=5
# for i in range(num,-1,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()


# num=5
# for i in range(num):
#     for j in range(num-i):
#         print('*',end=" ")
#     print()

# arrays are used to store multiple value of the same type or array is a collection of similar type of data .

# from array import *
# val=array('i',[1,8,6,4,23,4])
# for i in val:
#     print(i,end=" ")
#

# from array import *
# val=array('i',[1,8,6,4,23,4])
# val1=array(val.typecode,(a for a in val))
# print(id(val)) # 2761233690080
# print(id(val1)) # 2761233690560
# val1.append(12)
#
# print(val1.index(23))
# val1.remove(8)
# print(max(val1))
# val1.extend([10,15,19])
# for i in val:
#     print(i,end=" ")
# print()
# for i in val1:
#     print(i,end=" ")


# from array import *
#
# num=int(input("enter the length of an array"))
# val=array("i",[])
#
# print(type(val))
# for i in range(num):
#     n=int(input("enter the next element "))
#     val.append(n)
# for e in val:
#     print(e,end=" ")
# print()
# temp=int(input("enter the element you want to search "))
# for i in val:
#     if temp==i:
#         print("element found at ",val.index(i))
#         break
# print("bye")

# numpy is used to implement multi dimentional array

# from numpy import *
# val=array([1,2,34,56,7j])
# print(type(val.dtype))
# for i in val:
#     print(i,end=" ")

# from array import *
# vals=array("i",[1,2,3,4,5,6,7,8])
#
# from numpy import *
# val=array([[1,2,3,4],[2,4,6,8]])
# print(val)
# for e in val:
#     print(e)
#
# print(val.dtype)
#

# from numpy import *
# val=array([1,2,3,4,5,6,7])
# val1=val
# for e in val1:
#     print(e,end=" ")
# print()
# for e in val:
#     print(e,end=" ")

# we have 2 methods for copying the array
# 1.shallow copy in which we use .view() // if we change the element in original array then it will reflect in the copied array as well
# 2.deep copy in which we use
from numpy import *
# val=array([1,2,3,4,5,6,7])
# vals=val.view()
# val[0]=100
# val.flatten()
# for e in vals:
#    print(e,end=" ")
# print()
# for e in val:
#    print(e,end=" ")

# val=array([1,2,3,4,5,6,7])
# vals=val.copy() # change in the original array not reflected in the copied array .no link between original and copy array .
# val[0]=100
# val.flatten()
# for e in vals:
#    print(e,end=" ")
# print()
# for e in val:
#    print(e,end=" ")

# matrix
from numpy import *
# val=array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(val.shape)
# print(val.ndim)
# print(val.reshape(3,2,2))
# print(val.flatten())
# print(val.shape)

# c=matrix('1,2,3 ; 4,5,6 ; 7,8,9 ')
# d=matrix('11,21,13 ; 14,15,16 ; 17,18,19')
# print(c+d)
# print(c*d)

# print(c)
# print(c.diagonal())
# print(c.reshape(3,3))

# functions
# def name(n):
#     print(n)
#
# name("paras")
#
# def sum(a,b):
#     c=a+b
#     d=a-b
#     return c, d
# # name("disha")
# r,s=sum(20,16)
# print("r is : {} s is : {}".format(r,s))
#
# print(r)
#

# types of arguments
# 1 positional
# 2 default
# 3 variable length
# 4 keyword

# def person(name,age):
#     print(name)
#     print(age-2)
# person(age=22,name='paras')# this is keyword argument
#
# def person(name,age=21): # default arguments
#     print(age-2)
#     print(name)
# person('paras yadav')

# def person(name,* data): # variable length arguments
#     print(name)
#     for i in data:
#         print(i,end=" ")
# person('paras','mumbai',23,'java & python',98)

# def person(name,** data): # variable length arguments with keywords known as KWARGS
#     print(name)
#     for i  in data.items():
#         print(i ,end=" ")
# person('paras',city='mumbai',age=23,field='java & python',marks=98)

# a=10 # global variable
# def something():
#     x=globals()['a'] # using globals we get all global variables and we can access one also
#     globals()['a']=20
#    # global a #  the global keyword is used to declare a variable as global inside a function,
#     a=15  # local variables
#     print("in local ",a)
# something()
# print("in global ",a)


# def find(list):
#     even = 0
#     odd = 0
#     for i in list:
#         if(i%2==0):
#             even+=1
#             # print(i," is even ")
#         else:
#             odd+=1
#             # print(i," is odd")
#     return even,odd
# lst=[1,4,7,3,9,8,6,10,14,11,13]
# r,s=find(lst)
# print("no of even no is : {} ,no of odd no is : {} ".format(r,s))


# def fib(n):
#     a=0
#     b=1
#     if(n==1):
#         print(a,end=" ")
#     else:
#         print(a, end=" ")
#         print(b,end=" ")
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
#
# fib(10)

# factorial of a number
# def fact(n):
#     if(n==0 ):
#         print(1)
#
#     else:
#         fact = 1
#         for i in range(1,n+1):
#
#             fact=fact*(i)
#         print(fact)
#
# fact(0)
#
# def fact(n):
#
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# result=fact(5)
# print(result)

# decorators are used to adding extra features to the existing function without altering the existing function .
# def div(a,b):
#     c=a/b
#     print(c)
#
# def smart_div(fun):
#     def inner(a,b):
#         if(a<b):
#             a,b=b,a
#         return fun(a,b)
#     return inner
# dix=smart_div(div)
#
# dix(2,5)

#
# def reduce(n):
#     if n%2==0:
#         return n
#
# nums=[10,12,15,18,24,27,8,6,9]
# # val=list(filter(lambda a:a%2==0 ,nums))
# val=list(filter(reduce,nums))
#
# print(val)


# lambda expression
# from functools import reduce
# def reduce1(n):
#     if n%2==0:
#         return n
# def mul(a):
#     a=a*2
#     return a
# def sum(a,b):
#     return a+b
# nums=[10,12,15,18,24,27,8,6,9]
# # val=list(filter(lambda a:a%2==0 ,nums))
# val=list(filter(reduce1,nums))
#
# # val1=list(map(lambda a:a*2,val))
# val1=list(map(mul,val))
#
# # val2= reduce(lambda a,b : a+b,val1)
# val2=(reduce(sum,val1))
# print(val2)
# print(val1)
# print(val)
#


# def sum(n):
#     c=1
#     for i in n:
#         c=c+i
#     print(c,end=" ")
#
# nums=[10,12,15,18,24,27,8,6,9]
# f= lambda list:[i*2 for i in nums  ]
# result=f(nums)
# print(result)
# sum(nums)

# from calc import add
# print("hello")
#
# add(2,3)


# import calc
# print("in MyCode ")

# class computer:
#     laptop="dell" # class variable only used in class method
#
#     def __init__(self,cpu,ram):
#         print("object is created ")
#         self.name='paras'  # instance variables used in instance methods
#         self.age=22
#         self.ram=ram
#         self.cpu=cpu
#     def lap(self):
#         print("16 gb ram","1 Tb ssd ","ryzen 7")
#     def cpu1(self):
#         print("configuration is ",self.ram ,self.cpu)
#     @classmethod
#     def info(cls): # class method
#         print(cls.laptop)
#     @staticmethod # static method
#     def s():
#         print("static method")
# com=computer("i5",16)
#
# com.cpu1()
# com.name="paras yadav"
# com.laptop="MacBook Pro"
# print(com.laptop)
# print(com.name ," : ",com.age)
#
# computer.info()
# computer.s()
#
# com1=computer("i7",32)
# com1.cpu1()
# print(com1.laptop)
# print(com1.name ," : ",com1.age)
#
# com.lap()
# com1.lap()

# inner class
#
# class Student:
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.marks=marks
#         self.age=age
#         self.Lap=self.Laptop(12,32)
#     def show(self):
#         print("student info : ",self.name,self.marks,self.age)
#         self.Lap.show()
#     class Laptop:
#             def __init__(self,ram,screen):
#                 self.name="dell"
#                 self.price=60000
#                 self.ram=ram
#                 self.screen=screen
#
#             def show(self):
#                 print("laptop is : ",self.name,self.price,self.ram,self.screen)
#
# s1=Student("paras",98,22)
# s2=Student("dev",85,22)
#
# # l1=Student.Laptop("32GB","15.3 inches")
# # l2=Student.Laptop("16GB","12 inches")
# # l1.show()
# # l2.show()
#
# # s1.Laptop(100,100).show()
# # s2.Laptop(1,1).show()
#
# s1.show()
# s2.show()


# Inheritance
# class A:
#     def __init__(self):
#         print("default constructor of A")
#     def feature1(self):
#         print("feature1 loading ")
#     def feature2(self):
#         print("feature2 loading ")
# class B(A):
#     def __init__(self,x):
#
#         super().__init__()
#         print("default constructor of B",x)
#     def feature3(self):
#         print("feature3 Loading ")
#     def feature4(self):
#         print("feature4 loading ")
# class C(B):
#
#     def __init__(self,x):
#         super().__init__(x)
#         print("default constructor of C",x)
#     def feature5(self):
#         super().feature1()
#         print("feature5 loading ")
#     def feature6(self):
#         print("feature6 loading ")
# c=C(10)
# c.feature5()


# class pycharm:
#     def execute(self):
#         print("testing")
#         print("spell check")
# class vscode:
#     def execute(self):
#         print("awsome code")
#         print("auto generated")
# class python:
#     def code(self,ide):
#         ide.execute()
#
# ide=pycharm()
#
# c=python()
# c.code(ide)


# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         # print("default constructor")
#
#     def __add__(self, other):
#         x=self.x+other.x
#         y=self.y+other.y
#         m3=A(x,y)
#         return m3
# a=A(10,20)
# b=A(30,40)
#
# c=a+b
# print(c.x)
# print(c.y)

# Operator overloading
# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         # print("default constructor")
#
#     def __add__(self, other):
#         x=self.x+self.y
#         y=other.y+other.x
#         m3=A(x,y)
#         return m3
#
# a=A(10,20)
# b=A(30,40)
#
# c=a+b
# print(c.x)
# print(c.y)

# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#     def __add__(self, other):
#         x=self.x+self.y
#         y=other.x+other.y
#         m=A(x,y)
#         return m
# a=A(10,20)
# b=A(30,40)
# c=a+b
# print(c.x)
# print(c.y)

# method overloading
# class A:
#     def __init__(self):
#         pass
#     def sum(self,a=None,b=None,c=None):
#         if(a!=None and b!=None and c!=None):
#             print("sum is : ",a+b+c)
#         elif(a!=None and b!=None):
#             print("sum is : ",a+b)
#         else:
#             print("sum is : ",a)
#
#     def sum(self,a,b,c,d):
#         print("sum is : ",a+b+c+d)
#
# a=A()
# a.sum(10,20,30,40)

# method overriding
# class A:
#     def __init__(self):
#         pass
#     def show(self):
#         print("in A show")
#     def greet(self):
#         print("good morning ")
# class B(A):
#     def show(self):
#         print("in B show")
# b=B()
# b.show()
# b.greet()


# from time import sleep
# from threading import Thread
# class A(Thread):
#
#     def run(self):
#         for i in range(1000):
#             sleep(0)
#
#             print("hi ",i)
#
# class B(Thread):
#
#     def run(self):
#         c=0
#         for i in range(1000):
#             sleep(0)
#
#             print("hello ",i)
#
# a=A()
# b=B()
# a.start()
# b.start()
#



# from time import sleep
# from threading import Thread
# class A(Thread):
#     def __init__(self):
#         super().__init__()
#         self.c=0
#
#     def run(self):
#         for i in range(1000):
#             sleep(0)
#             self.c+=1
#             #print("hi ",i)
#
# class B(Thread):
#     def __init__(self):
#         super().__init__()
#         self.c=0
#     def run(self):
#         c=0
#         for i in range(1000):
#             sleep(0)
#             self.c+=1
#            # print("hello ",i)
#
# a=A()
# b=B()
# a.start()
# b.start()
# a.join()
# b.join()

# print("bye",(a.c+b.c))

# Duck typing
# class pycharm:
#     def execute(self):
#         print("ide for advance developer")
#         print("spell check")
# class vscode:
#     def execute(self):
#         print("auto suggestion")
#         print("Modern ide")
#
# def code(ide):
#     ide.execute()
#
# i=pycharm()
#
# code(i)

# abstract class

# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def show(self):
#         pass
#     def greet(self):
#         print("Good morning")
# class B(A):
#     def show(self):
#         print("in b show")
# b=B()
# b.greet()
# b.show()

# f=open("paras.txt","r") # we have file name and its mode of opening like read(),readline(),write(),append(),rb,wb,ab .
# print(f.readline())

# f=open("paras.txt","a")
# f.write(" Hello Paras Yadav")


# how to copy 1 file into another
# f=open("paras.txt","r")
# f1=open("paras1.txt","w")
# for data in f:
#     f1.write(data)

# f=open("paras1.txt","r")
# print(f.read())

# f1=open("logo.png","rb")
# f2=open("paras1.png","wb")
# for data in f1:
#     f2.write(data)

# f1=open("paras1.png","rb")
# print(f1.read())
#
#
#
# List=[1,2,3,4,5,6]
# List[5]=10
# print(List)


# L=[1,2,3,4,5,6,2,4]
# t=tuple(L)
# s=set(t)
# print(s)
# print(t)

# s={1,2,3,4,5,6}
# l=list(s)
# del l[0:2]
# print(l)
#
# d={'1':10,'2':20,'3':30,'4':40,'5':50}
#
# # del d[1] # pop will remove the last element if the index is not given to it .
# # del fun is used to remove multiple values by giving range
# del d['1']
# print(d)

# a=10
# b=5
# print("Before swap A : {} , B : {} ".format(a,b))
# # a=a+b # 10+5 = 15
# # b=a-b # 15-5 = 10
# # a=a-b # 15-10 = 5
#
# # a,b=b,a
#
# # a=a^b
# # b=a^b
# # a=a^b
# print("After swap A : {} , B : {} ".format(a,b))


# name="paras"
# print(id(name))
# name="paras yadav"
# print(id(name))


# n = 10
# print(id(n))
# n = 20
# print(id(n))

# import math as m
# n=m.pow(2,3)
# print(m.exp(1))
# print(n)


# prime no

# lower=100
# higher=200
# for data in range(lower,higher+1):
#     for i in range(2,data):
#         if(data%i==0):
#             break
#     else:
#         print(data)

# n=int(input("enter a no"))
# for d in range(n):
#
#     for i in range(2,d):
#         if(d%i==0):
#            # print(d,"not prime")
#             break
#     else:
#        print(d,"prime")
#
# print("bye")

# factorial
# n=int(input("enter a no"))
# if(n==0 or n==1):
#     print(1)
# else:
#     f = 1
#     for i in range(2, n + 1):
#         f = f * i
#     print(f)


# n=int(input("enter a no"))
#
# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)
# f=fact(n)
# print(f)

# factorial of a no
n=int(input("enter a no"))
if(n==0 or n==1):
    print(1)
else:
    f = 1
    for i in range(2, n+1):
        f = f * i
    print(f)



