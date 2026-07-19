num=int(input("enter ur np.:"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
print(count)