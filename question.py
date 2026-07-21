# # # # num=[12,-45,23,1,-6,7,8,34]
# # # # maxi=float("-inf")
# # # # for n in num:
# # # #     if n>maxi:
# # # #         maxi=n
# # # # print(f"maximum number = {maxi}")

# # # def does_exist(lst,target):
# # #     for num in lst:
# # #         if num==target:
# # #             return True
# # #     return False


# # # print(does_exist(nums,34))

# # def calculate_avg(nums):
# #     n = len(nums)
# #     total=0
# #     for num in nums:
# #         total=total+num
# #     return total/n

# # nums=[1,2,34,5,6,8,9,0,23,45,45,12,32.34]
# # print(calculate_avg(nums))     
# def sum_two_lst(lst1,lst2):
#     new_list=[]
#     n=len(lst1)
#     for i in range(0,n):
#         total=lst1[i]+lst2[i]
#         new_list.append(total)
#     return new_list


# num1=[1,2,3,4,5,6]
# num2=[1,2,3,4,5,6]
# ans=sum_two_lst(num1,num2)
# print(ans)


def is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if lst[i]<lst[i+1]:
            return False
    return True

num1=[1,7,6,5,6,7,8,9,3,2,1,23,4,5,7,]
ans=is_sorted(num1)
print(ans)