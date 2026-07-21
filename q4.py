def even_odd(lst):
    n=len(lst)
    new_even=[]
    new_odd=[]

    for i in range(0,n):
        if lst[i]%2==0:
            new_even.append(lst[i])
        else:
            new_odd.append(lst[i])

    print(f"even list is {new_even}")
    print(f"odd list is {new_odd}")

num1=[1,2,3,4,5,6,7,8,9]
even_odd(num1)
