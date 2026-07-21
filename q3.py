def remove_duplicate(lst):
    n=len(lst)
    new_lst=[]
    for i in range(0,n):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
            i+=1
        
    return new_lst
    
num=[1,2,2,3,3,4,4,5,5,6,6,7,8,77,6,5,4,3]
print(remove_duplicate(num))