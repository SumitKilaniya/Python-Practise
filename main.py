'''
print("hello Aiml")
#i am starting my aiml journey
"""doc string for multiline comment"""



"""VARIABLES"""

python_intro="hello"
print(python_intro)
print(type(python_intro))

python_intro1=22j
print(type(python_intro1))

"""data types"""
string1='h e ee ele '

print(type(string1))
#boolean
bol=True
print(type(bol))


"""input/output"""
name='sumit'
age=20
print(name,age)
print("hello my name is ",name,"and my age is ",age)
print(f"my name is {name} and my age is {age}")
age1=int(input("what is your age"))
print(age1)

'''
'''a=12
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)#float value because its p/q form 
print(a//b) #remove the zero od decimal or convert it into int--flow division
c=5
d=2
print(c//d)
print(c**d)
print(32%5)#remainder'''
#print(12+4/2)


#assignment operator
#a=10
#assign value to the variable 


#compound assignment operator
'''
a=20
a+=20 
a+=40#(a=a+20)  #we can reassign the value in python
a+=80

a-=50
print(a)
a*=2
print(a)
a**=2
print(a)
a/=5

print(a)
'''

#comparison operator provide boolean result
'''
==
>
<
<=
>=
!=
'''
'''
a=12
b=12.2
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a>b,a<b)

'''
'''
#logical operator
#AND logical operator-- give true if both comparisons are true

print(125>120 and 123<124 and 12==13)

#OR logical operator --give true if any one of the comparison is true --- false only if all comparison are false

print(123==124 or 123==123 or 123!=123)

#not logical operator -reverse
print(not 12==12)
'''

#conditional statement
'''Marks = 90
if Marks>90:
    print("U Got a+")
else:
    print("u got")
'''

'''money =int(input("give me money:"))
if money==10:
    print("i will take dairy milk chocolate")
elif money==20:
    print("i will have cone ice-cream")
elif money == 30:
    print("i will have mango ice-cream")
else:#else doesn't contain any condition 
    print("i will get something else")'''
    
'''num1=int(input("Enter your first no.:"))
num2=int(input("Enter your second no.:"))
if num1>num2:
    print(f" {num1} is greater than {num2}")
elif num1<num2:
    print(f" {num2} is greater than {num1}")
else:
    print("both no. are equal")'''
    
# gen=input("please tell ur gender(M OR F): ")
# if gen=='M'or gen=='m':
#     print("Good morning sir")
# elif gen =='F'or gen=='f':
#     print("good morning mam")
# else:
#     print("pls enter valid gender")


# num=int(input("pls tell ur no."))
# if num%2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")
# name=input("Pls enter ur name :")
# age=int(input("pls enter ur age:"))
# if age>=18:
#     print(f"hello {name},You are a valid voter")
# else:
#     print(f"{name},you are not a valid voter")
# a=0.1
# b=0.3
# z=a+b
# if z==0.4:
#     print("true")
# else:
#     print("false")
# x,y=input("enter no. separated by coma's:").split()
# print(x)
# print(y)

# a=0.1
# b=0.2
# z=0.3
# print(a+b==z)

# import keyword
# print("The list of keywords are:")
# print(keyword.kwlist)

# s='python'
# ans=s[0:1]+s[-1:0:-1]
# print(ans)

# a=range(2,21,2)
# for i in a:
#     print(i)

# for i in range(20,51):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)
# a='SHERYIANS'
# for i in range(9):
#     print(a[i])


# a='SHERYIANS TEACHERS INDUSTRY THINGS'
# n=len(a)
# print(n)
# for i in range(n):
#     print(a[i])
# a='SHERYIANS'
# for i in a:
#     print(i)

# for i in range(1,21):
#     if i==15:
#         continue
#     print(i)

# for i in range(1,10):
#     if i==5:
#         print("break statement is executed")
#         break
#     print(i)
# else:
#         print("else statement executed")

# 
# n=int(input("pls tell ur n0."))
# for i in range(n,0,-1):
#     print(i)
# n=int(input("pls tell no. for ur table:"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
# n=int(input("pls tell ur n0."))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"your fact is {fact}")

# n=int(input("Enter your number:-"))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"sum of even no. is {even} and sum of odd np. is {odd}")


# n=int(input("Enter your number:-"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n=int(input("enter ur no. :-"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
#         print(i)
# if sum==n:
#     print("Number is perfect")
# else:
#     print("Number is not perfect")

# n=int(input("Enter your number:-"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#         count+=1
# if count==2:
#     print("NUMBER IS PRIME")
# else:
#     print("Number is not prime")

# a="SHERYIANS"
# print(a[::-1])
# b="SHERYIANSh"
# print(b[-1:-9:-1])
# a="naman"
# print(len(a))
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
    
# print(b)

# if b==a:
#     print("palindrome")
# else:
#     print("not palindrome")

# n="ng4sdrg45%$#^%$&^ahdgfke"
# char=0
# dig=0
# spchr=0
# for i in n:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1
        
# print(f"your digit are{dig}and char are{char}and your special character are {spchr}")


# a=1
# while a<=30:
#     print(a)

# a=int(input("enter your no."))
# # while a>0:
# #     print(a%10)
# #     a=a//10
# copy=a
# rev=0
# while a>0:
#     rev=rev*10 +a%10
#     a=a//10
# print(rev)

# if rev==copy:
#     print("palindrome")
# else:
#     print("not palindrome")

# import random
# num=random.randint(1,100)
# tries=0
# while True:
#     guess=int(input("please guess a number: "))
    
#     if num == guess:
#         tries+=1
#         print(f"u guessed right in {tries}")
#         break
    
#     elif num<guess:
#         tries+=1
#         print("smaller")
#     elif num>guess:
#         tries+=1
#         print("greater")
#     else:
#         tries+=1
#         print("u  r wrong")

# n=int(input("enter your no."))
# if n in range(1,100):
#     print("no. is in the list")
# else:
#     print("no. is not in the list")


#function

# def hello():
#     print("this is the hello function so i am doing hello")
    
# if 2+2!=4:
#     hello()
# else:
#     print("kuch bhi")

# def sum(a,b=45):
#     print(f"Sum of two no. is {a+b}")
    
# sum(12,12)
# sum(123,1)
# sum(12)

# def detail(name,age):
#     print(f"your name is {name} and your age is {age}")
    
# detail("Sumit",45)
# detail(age=34,name="aakarsh")

# def palindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]
        
#     if st==rev:
#         print("palindrome")
#     else:
#         print("not a palindrome")
        
# palindrome("naman")
# palindrome("sumit")
# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)

# def sum(a,b=10):
#     return a+b

# print(sum(10))
# print(sum(10,50))
