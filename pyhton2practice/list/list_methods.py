# # # # # # fruits=["mango","kiwi","banana","apple"]
# # # # # # # fruits.append("grapes")
# # # # # # # print(fruits)
# # # # # # # fruits.remove("banana")
# # # # # # # print(fruits)
# # # # # # # fruits.pop(2)
# # # # # # # print(fruits)
# # # # # # # fruits.insert(3,"peach")
# # # # # # # print(fruits)

# # # # # # fruits.sort()
# # # # # # print(fruits)
# # # # # # fruits.sort(reverse=True)
# # # # # # print(fruits)

# # # # # # print(fruits.index("mango"))
# # # # # # print(fruits.count("mango"))


# # # # # num=[1,2,3,4,5,6]
# # # # # n=len(num)
# # # # # new_lst=[]
# # # # # for i in range(n-1,-1,-1):
# # # # #     new_lst.append(num[i])
# # # # # print(new_lst)

# # # # def remove_duplicate(lst):
# # # #     result=[]
# # # #     for i in lst:
# # # #         if i not in result:
# # # #             result.append(i)
# # # #     return result

# # # # nums=[1,2,3,4,2,2,3,3,4,5,1]
# # # # ans=remove_duplicate(nums)
# # # # print(ans)

# # # def even_odd(lst):
# # #     even_lst=[]
# # #     odd_lst=[]
# # #     for num in lst:
# # #         if num%2==0:
# # #             even_lst.append(num)
# # #         else:
# # #             odd_lst.append(num)

# # #     return even_lst,odd_lst


# # # nums=[1,2,3,4,5,6,7,8,9,10]
# # # ans=even_odd(nums)
# # # print(ans)


# # def sq_lst(lst):
# #     new_lst=[]
# #     for num in lst:
# #         new_lst.append(num**2)
# #     return new_lst

# # nums=[1,2,3,4,5,6,7,8,9]
# # ans=sq_lst(nums)
# # print(ans)


# square=[i*i for i in range(1,11,2)]
# print(square)

# reversed=[i for i in range(11,0,-1)]
# print(reversed)


# def is_prime(num):
#     factor=0
#     for i in range(1,num+1):
#         if num%i==0:
#             factor+=1

#     if factor == 2:
#         return True
#     return False


# new_lst=[i for i in range(2,100) if is_prime(i)]
# print(new_lst)


# marks=[1,2,3,4,5,6]
# new_lst=[num for num in marks]
# print(marks,id(marks))
# print(new_lst,id(new_lst))

# if id(marks)==id(new_lst):
#     print(True)
# else:  
#     print(False)