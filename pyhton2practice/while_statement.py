# # # # i=5
# # # # while i<=10:
# # # #     print("hello")
# # # #     i+=1
# # # #     print("done")
# # # i=0
# # # while i<11:
# # #     print(i)
# # #     i+=1

# # start=int(input("enter start point: "))
# # end=int(input("enter end point: "))
# # i=start
# # count=0
# # while i<=end:
# #     count+=i
# #     i+=1

# # print(count)
# n=int(input("enter ur table no.: "))
# i=0
# while i<=10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1
n=int(input("enter no.: "))
i=1
count=0
while i<=n:
    if n%i ==0:
        count+=i
        print(i,count)
    i+=1