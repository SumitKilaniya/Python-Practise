# listt=[i+7 for i in range(1,11) ]
# print(listt)

# list=[i for i in range(10,-1,-1) ]
# print(list)

def is_prime(num):
    factor=0
    for i in range(1,num+1):
        if num%i==0:
            factor+=1
    if factor==2:
        return True
    return False


new_list=[i for i in range(2,101) if is_prime(i)==True]
print(new_list)