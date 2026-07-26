# # for i in range(1,11):
# #     print(i)

# for i in range(10,0,-1):
#     print(i)

total=0
while True:
    num=int(input("enter your no.: "))
    if num == 0:
        break
    if num<0:
        continue
    total+=num
print(total)