def addition(a,b,c):
    ans=a+b+c
    print(f"total: {ans}")

addition(1,2,3)

def greet(name,age,gender):
    print(f"hey {name}! your age is {age} and gender is {gender}")

n=input("enter your name : ")
a=int(input("enter your age :"))
g=input("enter your gender: ")
greet(n,a,g)