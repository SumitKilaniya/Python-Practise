num=int(input("enter your no.:"))
# if num>0:
#     print("your number is positive")
# elif num<0:
#     print("your number is negative")
# else:
#     print("your number is zero")

if (num%4==0 and num%100!=0 )or (num%400==0):
    print("your number is leap year")
else:
    print("your number is not leap year")