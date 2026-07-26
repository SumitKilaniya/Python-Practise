# # x=[21,22,23,24,25,26,67,1,2,12,2,313,29]
# # # # print(len(x))
# # # # print(sum(x))
# # # # print(min(x))
# # # # print(max(x))
# # # # print(sorted(x))


# # # # ans=sum(x)/len(x)
# # # # print(f"average marks= {ans:.2f}")

# # n=len(x)
# # i=0
# # max=0
# # for i in range(0,n):
# #     if max<x[i]:
# #         max=x[i]
    

# # print(max)

# # # num=[21,22,23,24,25,26,67,1,2,12,2,313,29]
# # # # print(num[0])

# # # n=len(num)
# # # # i=0
# # # # # while i<=n-1:
# # # # #     print(num[i],end=" ")
# # # # #     i+=1

# # # # count=0
# # # # while i<=n-1:
# # # #     if num[i]%2==0:
# # # #         count+=1
# # # #     i+=1

# # # # print(count)

# # # # for i in range(0,n):
# # # #     print(num[i],end=" ")

# # # total=0
# # # for i in range(0,n):
# # #     total+=num[i]
# # # print(total)

# def add_element(lst1,lst2):
#     new_lst=[]
#     n=len(lst1)
#     for i in range(0,n):
#         total=lst1[i]+lst2[i]
#         new_lst.append(total)

#     return new_lst
    

# num1=[1,2,3,4,5]
# num2=[10,10,10,10,10]
# ans=add_element(num1,num2)
# print(ans)



def check_sorted(lst):
    new_lst=sorted(lst)
    if new_lst==lst:
        return True
    return False

num=[1,2,3,4,5,6,7,34,23,34,9]
num2=[1,2,3,4,5,6]
num3=[]
ans=check_sorted(num3)
print(ans)


    