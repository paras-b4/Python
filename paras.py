#!/usr/bin/env python
# coding: utf-8
'''


# In[2]:


#addition
8+9


# In[3]:


#substraction 
5-3


# In[4]:


#multiplication
8*3


# In[5]:


#division give quocient
8/4


# In[6]:


#floor division
8//4


# In[7]:


#modulus to get remainder
8%4


# In[8]:


#power
2**4


# In[9]:


# Hash symbol can be use to comment single line in python 
# multiline comment using string literals 
#ex
""" paras is good boy and disha is good girl
    they study in same college name KEC """
print("hello")





# In[9]:





# In[10]:


# print(" paras "laptop"")


# In[ ]:


print('paras "laptop"')


# In[3]:


# print('paras's "laptop"'')


# In[2]:


print('paras\'s "laptop"')


# In[ ]:


# concatination is use to combine string 
'paras' + 'paras'+'disha'


# In[4]:


# repetition is use to print a string multiple time

10 * 'paras'


# In[7]:


# (\n) back slash n is used to enter a new line 
print('paras \n yadav')


# In[5]:


print(r'paras \n yadav')


# In[9]:


# here x is a variable and 2 is a value asssign to variable x
x=2
x=x+4
x
# now x is update from 2 to 6
# here y is a variable and 3 is a value asssign to variable y
y=3
x+y




# In[10]:


# if i want to use output of previous operation so we use underscore 
_+x


# In[ ]:


# assign string to a variable
name = 'paras yadav'
name


# In[11]:


# slicing :- slicing return a range of characters
name = "paras yadav"
name[0]


# In[12]:


name [0:8]


# In[15]:


name [-7:-4]


# In[16]:


name [-4:-7]


# In[14]:


name[:]


# In[ ]:


# lists in python


# In[ ]:


name= 'paras yadav'
name[-1]
name[-2]


# In[ ]:


name[-2:-1]


# In[ ]:


nums=[1,3,5,3,7]
name=["paras",'disha']
loves=[nums,name]
loves[-1]
  loves[:]
loves


# # Lists in python
# # several oeration can be performed using it
# 1.APPEND 
# 2.REMOVE
# 3.INSERT
# 4.DELETE
# 5.CLEAR
# 6.REVERSE
# 7.SORT
# 8.MIN
# 9.MAX
# 10.SUM
# 11.POP
# 12.EXTEND
# 
# 

# In[7]:


list1=[12,45,23,35,18,34]
list1.append(10)
list1


# In[16]:


import itertools
'list=[2,12,45,23,35,18,34]'

print(list(itertools.repeat(2, 4)))


# In[ ]:


list1.insert(3,45)
list1


# In[ ]:


list1.remove(45)
list1


# In[ ]:


list1.pop(3)


# In[ ]:


list1.pop()


# In[ ]:


list2=[23,56,43,21,34,21]
del list2[2:3]
list2


# In[ ]:


list2.extend([76,45,33,38])
list2


# In[ ]:


# replace value in list using indexing
list2=[23,56,43,21,34,21]
list2[0]=35
list2


# In[ ]:


# reverse method in python
list2.reverse()
list2


# In[ ]:


min(list2)


# In[ ]:


max(list2)


# In[ ]:


sum(list2)


# In[ ]:


list2.sort()
list2


# In[ ]:


list1=[23,5,6,4,5]
list1


# In[ ]:


list1.remove(6)
list1


# In[ ]:


del list1[1:3]
list1


# In[ ]:


list1.pop(1)


# In[ ]:


abcd=[23,43,54,34,1,2,3,43,43,54,'paras','paras']
abcd.count('paras')


# In[ ]:


abcd=[23,43,54,34,1,2,3,43,43,54]
abcd.clear()
abcd


# # Tuple in python
# 1.tuples are immutable (we cannot change/modify the tuple like :- (insert ,append,del,extend,pop,remove,clear,sort))

# In[ ]:


nums = (12,32,24,11,54,34,28,32)
nums.count("paras")


# In[ ]:


nums[0]


# In[ ]:


min(nums)


# In[ ]:


max(nums)


# # Sets in python 
# 1.set is a collection of unique elements
# 2.set never follow sequence 
# 3.when we print the set then the sequence of values in output will be different form the input
# 4.we cannot fetch the value in set using indexing it does not follow any sequence
# 5.duplicate values are present in set will be printed only once in set
# 6.OPERATION IN SET POP,REMOVE,UPDATE,UNION,INSERTION,SYMENTIC_DIFFERNCE,DISCARD

# In[17]:


box={'paras','disha',4.0,5,23,34,18,35,18,35}
box


# In[18]:


box.remove(18)
box


# In[19]:


box[0]=23
box


# In[26]:


box1={"grapes","apple",'banana','mango'}
box.update(box1)
box


# In[25]:


box2={'apple','mango',"peanut butter",'rice cake'}
Z=box.union(box2)
Z


# In[21]:


x={'a','b','c'}
y={'f','d','a'}
z={'c','d','e'}
m={'w'}
result = x.union(y,z,m)
print(result)


# In[22]:


x.discard('a')
print(x)


# In[27]:


Z.discard('disha')
Z


# In[28]:


# in set pop does not take any argument like :- (pop(1)) as its does not follow any sequence pop randomly pop any element
Z.pop()


# # Dictionary in python
# 1.dictionary is a kind of data structure that is use to store items in key value pairs
# 2.we can access the value using keys only like data[4] (data is dictionary and 4 is a key) if key is not present in dic then it will give an error
# 3.key are immutable and unique(value of key cannot be repeat)
# 4.aad the value in dic 
#   data['monika']= 'cs '
# 5.delete the value in dic
#   del data['harsh']
# 6.we can store dictionary inside dictionary 
# 7.zip method is use to combine two list it will return the tuple 
# 8.we can convert the tuple into dictionary by usinfg dict() method
# 

# In[ ]:


data ={1:'paras',2:'disha',4:'loves'}
data[1]


# In[ ]:


data[3] # 3 is key not present in dictionary


# In[ ]:


# use of get() method
data.get(1)


# In[ ]:


data.get(3) # if key is not present in dic then get method gives blank but we printing it will give none 
print(data.get(3))


# In[ ]:


data.get(2,'not found')


# In[ ]:


data.get(3,'not found')


# In[ ]:


# Add the value in dictionary
data[3]='Disha'
data


# In[ ]:


# delete the value in dictionary
del data[3]
data


# In[ ]:


# use of zip() method
we can combine two list using zip() method
it will return the tuple
key = [ 12,43,23,56,47,35,18]
value = [13,44,22,29,33,34,8]
z=dict(zip(key,value))
z


# In[ ]:


# nested dictionary 
prog={'js':'atom','cs':'vs','python':['pycham','sublime'],'java':{'jse':"netbean","jee":'eclipse'}}
prog


# In[ ]:


prog={'js':'atom','cs':'vs','python':['pycham','sublime'],'java':{'jse':"netbean","jee":'eclipse'}}
prog.items() # item keywoed does not take any agrgument inside it


# In[ ]:


prog['js']


# In[ ]:


prog['python']


# In[ ]:


prog['python'][0]


# In[ ]:


prog['java']['jee']


# # range (data type) are commenly use to iterate over a sequence of number in a for loop

# In[11]:


range(10)


# In[12]:


list(range(10))


# In[13]:


set(range(2,10,2))


# In[14]:


tuple(range(10))


# # data type :- it describe the type of value 
# # -> python have several built in data type hera are some of the most common one

# In[15]:


# none type 
a = None
type(a)


# In[16]:


a = 5
type(a)


# In[17]:


num= 5.6
type(num)


# In[18]:


num= 2+5j
type(num)


# In[19]:


a= True
type(a)


# In[20]:


bool = 3 < 5
type(bool)



# # type conversion :- if you want to convert one data type to another data type

# In[21]:


a=5
b=float(a)
b


# In[22]:


a = 5.6
k = int(a)
print(k)


# In[23]:


c = complex(b,k)
c


# # operator in python
# 1. ARITHMETIC OPERATOR
# 2. Assignment operator
# 3. RELATIONAL OPERATOR
# 4. LOGICAL OPERATOR
# 5. UNARY OPERATOR

# In[30]:


# arithmetic apertor
a=2
b=6
a+b


# In[31]:


a-b


# In[35]:


a%b


# In[36]:


_+b


# In[37]:


b%a


# In[28]:


# assignment operator
a+=4
a


# In[29]:


a-=4
a


# In[30]:


a*=3
a


# In[31]:


a%=6 
a


# In[40]:


a=2
b=5
a^=b
a


# In[39]:


a=7
a/=5
a


# In[40]:


a=7
a//=5
a


# # we can also assign the value in one line for two variable
# 

# In[32]:


a,b=5,6
b


# In[33]:


a


# In[34]:


# unary opertor :- take single operand in an expression or a statement


# In[35]:


n=7
n


# In[36]:


-n


# In[37]:


n=-n
n


# In[38]:


# Relational operator (comparison operator)
# its return boolean value true or false

a<b


# In[41]:


a=5
b=5
a<=b


# In[40]:


a>=b


# In[41]:


a==b


# In[42]:


a!=b


# In[42]:


# logical operator
# if you want to combine two or more condition and then check the relation b\w them 
And
a<8 and b<6


# In[44]:


a<8 or b<5


# In[45]:


x= True
x


# In[46]:


not x


# # Bitwise operator the integer is first converted into binary and then operation are performed by bitwise operator on each bit oe correspondinf pairs
# 1.complement (~)
# 2.And (&)
# 3.Or (|)
# 4.Xor (^)
# 5.Left shift
# 6.Right shift

# In[45]:


~12 # compliment


# In[47]:


~1234


# In[48]:


12&13 # And


# In[49]:


12|13 # OR


# In[50]:


25^30 #Xor


# In[51]:


10 << 3 #Left shift


# In[52]:


10>>2 # Right shift


# # NUMBER SYSTEM CONVERSION 
# 

# In[53]:


# decimal to binary
bin(25)


# In[54]:


# binary to decimal
0b11001


# In[55]:


# decimal to octal
oct(25)


# In[48]:


oct(0x19)


# In[56]:


hex(25)


# # swap two number in python
# 

# In[57]:


# using third variable
a=5
b=6
temp = a
a=b
b=temp
a


# In[58]:


b


# In[59]:


# using operator
a=5
b=6
a = a+b #11
b= a-b #5
a= a-b #6
a


# In[60]:


b


# In[61]:


# using xor
a=5 #101
b=6 #110
a=a^b
b=a^b
a=a^b
a


# In[62]:


b


# In[63]:


# using assignment in one line 
a=5
b=6
a,b=b,a
a


# In[64]:


b


# # import math function provide a wide range of mathematical function it is use to perform mathematical operation like:- sqrt,pow,floor,ceil,exp,log(x[base]),trignomatric functions
# # math is a built in module in python
# # math.nan :- return a floating point "not a number" like :- 0/0, sqrt(-ve),log(-ve),

# In[65]:


import math 
x = math.sqrt(25)
print(x)


# In[49]:


import math as m
x = m.pow(2,10)
print(x)


# In[52]:


import math
print(math.log(100,(10)))


# In[68]:


print(math.exp(10))


# In[69]:


x= math.floor(99.99) # return smaller integer smaller or equals to x
print(x)


# In[70]:


x= math.ceil(99.99)
print(x)


# In[71]:


print(math.sin(90))


# In[72]:


print(math.cos(0))


# # while loop in python
# # we can execute a statement multiple time by using the loop
# # syntax :- counter variable
#                   while(condition)
#                   statement
#                   incrementer/decrementer
#  # Nested while loops simply means that a loop inside another loop
#  # To print the value in the same line we use(end=" ") the value will not come in the new line after using it

# In[73]:


i=1
while (i<=5): # suite means a block comes under a condition/loops 
    print("paras and disha")
    i+=1


# In[74]:


i=5
while (i>=1): # suite means a block comes under a condition/loops 
    print("paras and disha")
    i-=1


# In[75]:


# while inside a while
i=1
#j=1
while(i<=5):
    print("paras",end=" ")
    j=1
    while(j<=5):
        print("disha",end=" ")
        j+=1
    i+=1
    print()


# In[76]:


for i in range(0,10,2):
    print(i)
    


# In[77]:


for i in range(1,101):
    if(i%3)!=0 and (i%5)!=0 :
        print(i)


# # break , continue , pass are control flow statement that are used to alter the normal flow of execution in a loop
# 
# 

# In[78]:


Available = 10
x=int(input("enter no of candy you want"))
i=1
while(i<=x):
    if(i>Available):
        print('out of stock')
        break
    print("candy")
    i+=1


# In[ ]:


for i in range (0,101):
    if(i%3)==0 or(i%5)==0 :
        continue
    print(i)


# In[ ]:


for i in range(1,101):
    if(i%3)==0 or (i%5)==0 :
        pass
    else:
        print(i)


# In[ ]:


for i in range (1,101):
    if (i%2!=0):
        pass
    else:
        print(i)


# In[ ]:


# Prime number
num=7
for i in range(2,num):
    if num % i == 0 :
        break
        print("not prime")
else:
    print("prime")
    


# In[ ]:


# prime number
num=int(input ("enter a number"))
if num==1:
    print("not a prime")
for i in range(2,num):
    if num%i==0:
            print("not a prime")
            break 
else:
    print("prime number")
        


# In[ ]:


num = int(input('enter a number'))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


# In[ ]:


num=int(input('enter a number'))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


# In[ ]:


num=4
for i in range(num):
    for j in range(num):
        print('*',end=" ")
    print()


# In[ ]:


num=4
for i in range(num):
    for j in range(i+1):
        print('*',end=" ")
    print()


# In[ ]:


num=5
for i in range(num,-1,-1):
    for j in range(i):
        print('*',end=" ")
    print()


# In[ ]:


num=5
for i in range(num):
    for j in range(num-i):
        print('*',end=" ")
    print()


# In[ ]:


# Factorial of a number
num= int(input('enter a number'))
fact=1
for i in range (1,num+1):
    fact=fact*i
print(fact)


# In[ ]:


# Fibonachi series
num= int(input('enter a number'))
a=0
b=1
print(a)
print(b)
for i in range (2,num):
    
    c=a+b
    a=b
    b=c
    print(a+b)
    


# In[ ]:


# Leap year
year= int(input('enter a year'))
if year%400==0 and year%100==0:
    print('not a leap year')
elif year%4==0 and year%100!=0:
        print('leap year')
else:
    print('not a leap year')


# In[ ]:


year= int(input('enter a year'))
if year%400==0 and year%100==0:
    print('not a leap year')
elif year%4==0 and year%100!=0:
        print('leap year')
else:
    print('not a leap year')


# In[ ]:


year= int(input('enter a year'))
if year%400==0 and year%100==0:
    print('not a leap year')
elif year%4==0 and year%100!=0:
        print('leap year')
else:
    print('not a leap year')


# # Array in python is similar to list but here all the values are of same type in array
# # operation in array                                                                                    1.buffer_info()                                                                                                      2.append                                                                                                               3.reverse                                                                                                                  4.remove                                                                                                                 5.typecode                                                                                                         6.itemsize                                                                                                          7.extend                                                                                                                      8.count                                                                                                                            9.index                                                                                                                              10. sort()
# 
# 

# In[ ]:


from numpy import *
arr= array([1,2,3,6,7,8,9])
print(arr)


# In[ ]:


import array as arr
arr = array('i',[1,4,3,5,6,2])
print(arr)


# In[ ]:


import array as arr


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
print(value)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])

print((value.buffer_info()))


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
print(value.typecode)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
value.reverse()
print(value)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
value.append(2)
print(value)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
value.remove(1)
print(value)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
print(value.itemsize)


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
print(value.index(5))


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
valuefrom array import *
value = array('i',[1,4,3,5,3])
value.pop(4)


# # way of creating an array in numpy
# # 1. array() 2. arrange() 3.linespace() 4. logspace() 5. zeros() 6. ones()

# In[2]:


from numpy import *
value = ones(5)
print(value)


# In[3]:


from numpy import *
value= arange(0,10,12) # out of range but this problem is solved by using linspace()
print(value.dtype)
value


# In[ ]:


from numpy import *
value= arange(1,10,2.5) 
value


# In[ ]:


from numpy import *
value = ones(5)
print(value)


# In[ ]:


value=array([1,2,3,4,5])
value


# In[ ]:


value= linspace(0,15,20) # if we donot specify the range it will go up to 50 
value


# In[ ]:


value=logspace(0,10,20)
value


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
#value.count(1)
print(value.count(3))


# In[ ]:


from array import *
value = array('i',[1,4,3,5,3])
for i in range(len(value)):
    print(value[i],end=" ")


# # copy array element into new array 
# 

# In[ ]:


from array import *
value = array('i',[1,2,3,4,5])
new_array= array(value.typecode, (a*a for a in value))
print(new_array)


# In[ ]:


from array import *
value = array('i',[1,2,3,4,5])
new_array= array(value.typecode, (a*a for a in value))
for j in new_array:
    print(j)
#print(new_array)


# In[ ]:


# program for user defined array
import numpy
from array import *
arr=array('i',[])
n=int(input('enter the length if an array'))
for i in range(n):
    x=int(input('enter a the elements in array'))
    arr.append(x)
print(arr)
print(type(arr))


# In[ ]:


import array as arr
value=arr.array('i',[1,2,-3,4])
value



# In[ ]:


# program for search an element in an array
import numpy
arr=array('i',[])
n=int(input('enter the length if an array'))
for i in range(n):
    x=int(input('enter a the elements in array'))
    arr.append(x)
print(arr)
value=int(input('enter a number'))
k=0
for j in arr:
    if j==value:
        print(k)
        break
    k+=1
    


# # if you want to work with multidimension array(2d)
# # different fuction can be performed on array same as list
# 

# In[ ]:


from numpy import *
value=array([2,3,4,5,6,0],bool) # here  
print(value.dtype)
value


# In[ ]:


value=array([2,3,4,5,6,0],complex) # here  
print(value.dtype)
value


# In[ ]:


value=array([2,3,4,5,6,0],str) #here (u1) 1 represent bits   
print(value.dtype)
value


# In[ ]:


# To Add VALUES OF TWO ARRAY
import numpy
x=array([1,3,2,4,5])
y=array([6,6,7,8,7])
c=x+y
print(c)


# In[ ]:


x=x+5
x


# In[ ]:


x=x*2
x


# In[ ]:


x[0]


# In[ ]:


sum(x)



# In[ ]:


log(y)


# In[ ]:


cos(x)


# In[ ]:


sin(y)


# In[ ]:


max(y)


# In[ ]:


# list w cannot count item repitition
x=[2,3,42,2,3,2,2,2,2,2]
print(x.count(2))



# In[ ]:


concatenate([x,y])


# # COPYING AN ARRAY IN PYTHON
# # Two techniques are available                                                                                  1. shallow :- In this technique both array are dependent on each other AND if we update an element in one array then the change would also be reflected in another array ,                                                                                                             2. deep :- In deep copy two different array are not linked with each other in any way

# In[ ]:


# COPYING AN ARRAY IN PYTHON
arr1=array([1,2,3,4])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


# In[ ]:


arr1=array([1,2,3,4])
arr2=arr1.copy() # deep copy
arr1[0]=10
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


# In[ ]:


arr1=array([1,2,3,4])
arr2=arr1.view() # shallow copy
arr1[0]=10
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


# In[ ]:


from numpy import *
value= array([1,2,3,4,5,6])
print(value.reshape(3,2))


# In[ ]:


value.shape


# In[ ]:


value.shape


# In[ ]:


value.flatten()


# In[ ]:


value.reshape(2,3)


# In[ ]:


print(value.size)
print(value.shape)


# In[ ]:


value1= array([[[1,2,3],[4,5,6],[7,8,9]]])
print(value1.shape)
print(value1.ndim)


# In[ ]:


value1.diagonal()


# In[ ]:


x=matrix(value)
x


# In[ ]:


x=matrix(value1)
x


# In[ ]:





# # Function

# In[ ]:


def calcsum(x,y):
    s=x+y
    return s
    
    
n1=1
n2=2
c=calcsum(n1,n2)
print('sum of two given number is :',c)


# In[ ]:


x= int(input('enter a no'))
def increment(x):
    
    x=x+1
    return x

print(x)
c=increment(x)
print(c)


# In[ ]:


def person(name,*data):
    
    print(name)
    print(data)
person('paras',1,2,3,4,"abcd",4.0)
    


# In[ ]:


def person(name,**data):
    print(name)
    print(data)
person("paras",age='21',dob='2002',mob=987456321)


# In[ ]:


# Pass list to a function
def count(lst):
    even=0
    odd=0
    for i in range (len(lst)):
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[25,24,36,47,48,99,100]

even,odd=count(lst)
print(even)
print(odd)


# In[ ]:


# program to count even ,odd no in list
lst=[1,2,3,4,5,6,7,8,10]
even=0
odd=0
for i in lst:
    if i%2==0 :
        even+=1
    else :
        odd+=1
print(even)
print(odd)
        


# # factorial of a no with and without using recursion

# In[ ]:


n= int (input ('enter a no'))

fact=1
for i in range (2,n+1):
    fact=fact*i
print(fact)


# In[5]:


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n= int (input('enter a number'))
c=fact(n)

print(c)
        


# # fibonachi series using recursion

# In[ ]:


n=int(input('enter a number'))
a=0
b=1
if n==1:
    print(a)
elif n==0:
    print('incorrect input')
else:
    print(a)
    print(b)

for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(a+b)


# In[ ]:


def fib(n):
    
    a=0
    b=1
    n=int(input('enter a number'))
    
    if n==1:
        print(a)
    elif n==0:
        print('invalid')
    
    else:
   
        print(a)
        print(b) 
        
        for i in range(2,n):
            c=a+b
            a=b
            
            b=c
           
            print(c)
        
fib(1)


    




# In[ ]:


def fib(n):
    if n<=0:
        print('incorrect input')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))


# In[ ]:


import sys
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
i=1
def func():
    global i # if you want to change the value of global variable inside the function you cannot cange it directly use global keyword
    i+=1
    print("hello",i)
    func() # for infinite iteration

func() # far calling


# # Anonymous number (lambda function)
# # normal function are defined by using def keyword and function name
# # A function without a function name is known as Anonymous function
# # Anonymous function is called a lambda function
# # Instead of defining a function ,we can directly use it whenever it is required to use
# # we have to use the lambda keyword to directly define the function in one line 
# 

# In[ ]:


def square(n):
    return n**n
c=square(n)
n=int(input ('enter a number'))
print(c)


# In[ ]:


f= lambda b:b**b
f(2)


# In[ ]:


f= lambda a,b:a+b
c=f(12,13)
print(c)


# # 1 filter() , 2 map() , 3 reduce()

# In[ ]:


def is_even(n):
    return n%2==0
num =[1,2,3,4,5,6,7,8,9,10]
values=list(filter(is_even,num))
print(values)


# In[ ]:


num = [1,2,3,4,5,6,7,8,9,10]
values = list(filter(lambda a:a%2==0,num))
values


# In[ ]:


num =[1,2,3,4,5,6,7,8,9,10]
values =list(filter(lambda a:a%2==0,num))
double=list(map(lambda a:a*2,values))
print(double)


# In[ ]:


class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    #def config(self):
     #   print('config is ',self.CPU,self.RAM)
com1= computer('i5',16)
com2= computer('Ryzen',8)
#com1.config()
#com2.config()
print(com1.cpu,com1.ram)
print(com2.cpu,com2.ram)


# In[ ]:


class vehicle:
    wheels=4 # class variable or static variable
    def __init__(self): # constructor 
        self.mil=10    # instance variable are defined inside consructor
        self.com='bmw'
# namespace is an area where you create and store object and variable 1.class namespace 2.instance namespace 
obj1=vehicle()
obj2=vehicle()
obj1.mil=20
#obj2.wheels=6
vehicle.wheels=10
print(obj1.mil,obj1.com,obj1.wheels)
print(obj2.mil,obj2.com,obj2.wheels)


# In[ ]:





# # class is a blueprint to create objects                                                                        A class can be defined by using the class keyword and everyclass must have a name to it                                                                                                                        A class consist of two things 1.data 2.methods 
# # 1 Attribute-variable
# # 2 Behaviour-methods(function)
# 
# # An object of a class can be defined by a variable and assigned its value with the type of the class A class can have multiple object 
# # object variable = class_name()                                                                                 
# 
# # we can call any method from a class 
# # the behaviour of each object is different from each other so need to define for which object , you are calling a method
# # syntax for calling a method
# # class_name.method_name(object variable)
# # we can also call a method in another way
# # object_variable.method_name()
# 
# 
# 

# In[ ]:


class computer:
    def config(self):
        print('i5',' 16gb','1tb')
obj1=computer()
obj2=computer()
obj1.config()
obj2.config()



# In[ ]:


class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print('config is',self.cpu,self.ram )
obj1=computer('ryzen',16)
obj2=computer('i5',8)
obj1.config()
obj2.config()

        


# In[ ]:


class person:
    def __init__(self):
        self.name= 'paras'
        self.age=21
    def update(self):
        self.age=22
    def compare(self,abc):
        if self.age==abc.age:
            return True
        else:
            return False
obj1=person() # constructor 
obj2=person()
obj1.name= 'disha'
obj1.age=21

if obj1.compare(obj2):
    print('they are same')
else:
    print('they are different')


#obj1.update()


print(obj1.name,obj1.age)
print(obj2.name,obj2.age)


# # inner class

# In[1]:


class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()# inner class object is inside outer class
    def show(self):
        print(self.name,self.rollno)
    class laptop:
        def __init__(self):
            self.brand='Dell'
            self.cpu='ryzen5'
            self.ram=16
                
o1=student('paras',35)
#print(o1.name,o1.rollno)
o1.show()
lap1=student.laptop()
print(lap1.brand,lap1.cpu,lap1.ram)


# In[ ]:


class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()# inner class object is inside outer class
    def show(self):
        print(self.name,self.rollno)
    class laptop:
        def __init__(self):
            self.brand='Dell'
            self.cpu='ryzen5'
            self.ram=16
                
o1=student('paras',35)
#print(o1.name,o1.rollno)
o1.show()
o1.lap.brand,o1.lap.ram,o1.lap.cpu


# In[ ]:


class student:
    def __init__(self,name,rollno): # constructor 
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop() # inner class object is inside outer class
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='Dell'
            self.cpu='ryzen5'
            self.ram=16
        def show(self):
            print(self.brand,self.ram,self.cpu)
                
o1=student('paras',35)
#print(o1.name,o1.rollno)
o1.show()




# # constructor in python is a special method that is defined inside a class which run/execute automatically when an object of class is created
# 

# In[24]:


class computer:
    def __init__(self): # constructor is execute automatically when an object of a class is created
        print('this is a class')
c1=computer()


# # Inheritance in python 
# # 1.single level inheritance  2.multilevel inheritance 3.multiple inheritance

# In[15]:


# single level inheritance
class A:
    def feature1(self):
        print('feature 1 working')
    def feature2(self):
        print('feature 2 working')
class B(A):
    def feature3(self):
        print('feature 3 working')
    def feature4(self):
        print('feature 4 working')
a=A()
a.feature1()
a.feature2()
b=B()
b.feature1()
b.feature2()
b.feature3()


# In[19]:


# multilevel inheritance
class A:
    def feature1(self):
        print('feature 1 working')
    def feature2(self):
        print('feature 2 working')
class B(A):
    def feature3(self):
        print('feature 3 working')
    def feature4(self):
        print('feature 4 working')
class C(B):
    def feature5(self):
        print('feature 5 working')
a=A()
a.feature1()
a.feature2()
b=B()
b.feature1()
b.feature2()
b.feature3()
c=C()
c.feature5()
c.feature1()
c.feature2()
c.feature3()


# In[21]:


# multiple inheritance
class A:
    def feature1(self):
        print('feature 1 working')
    def feature2(self):
        print('feature 2 working')#
class B:
    def feature3(self):
        print('feature 3 working')
    def feature4(self):
        print('feature 4 working')
class C(A,B):
    def feature5(self):
        print('feature 5 working')
a=A()
a.feature1()
a.feature2()
b=B()
b.feature3()
c=C()
c.feature5()
c.feature1()
c.feature2()
c.feature3()


# # Polymorphism 
# # 1.Duck Typing
# # 2.Operator overloading
# # 3.Method overloading
# # 4.Method overriding

# In[12]:


# method overloading
class student :
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None , b=None , c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
            return s
        elif a!=None and b!=None:
            s=a+b
            return s
       
        else:
            s=a
            return s 
       
s1=student(5,7)
print(s1.sum(5,9,4))
    


# In[16]:


# function(method) overriding
class A:
    def show(self):
        print("in A show")
class B(A):
    pass
a=B()
a.show()


# In[17]:


class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in b show")
a=B()
a.show()


# In[34]:


# Operator overloading 
 + ==__add__(self,other)
    - == __sub__(self,other)
    * == __mul__(self,other)
    / == __truediv__(self,other)
    // == __floordiv(self,other)
    % ==__mod(self,other)

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a + other.a
ob1=A(5)
ob2=A(9)
ob3=A("Greeks")
ob4=A('For')
print(ob3+ob4)
print(A.__add__(ob1,ob2))
print(ob1.__add__(ob2))


# In[36]:


class A:
    def __init__(self,a):
        self.a=a
    def __rshift__(self,other):
        return self.a  other.a
ob1=A(5)
ob2=A(9)
ob3=A("Greeks")
ob4=A('For')

print(A.__rshift__(ob1,ob2))
print(ob1.__rshift__(ob2))


# In[ ]:


class complex:
    
'''
