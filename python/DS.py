#DATA STRUCTURE
#list indexing
# a=[12,13,14,15,16,17,18,19]
# print(a[6])

# #list slicing

# print(a[1:6])

#traversing
# a=[12,13,14,15,16,17,18,19]
# for i in range(len(a)):
#     print(a[i])
    
# for i in a:
#     print(i)
    
# print(dir(list))


# #append --- insert element at last
# l=[1,2,3,4,5,67,4]
# l.append(6)
# print(l)

# #insert ----- used to insert at particular index -(index,element)
# #extend --- add multiple element at last (complete list)
# #remove --- remove first occurrence of element 


# l.extend([0,2,34,5])
# l.insert(2,678)
# l.remove(2)
# print(l)

#pop----remove at index and store in var
# l=[1,2,3,4,5,67,4]
# popped=l.pop(5)
# print(popped)

#index----give index

# indexx=l.index(3)
# print(indexx)

#count--occurrence of element
# count=l.count(4)
# print(count)

# l.sort()
# print(l)

# l.reverse()
# print(l)

# newlist=l.copy()
# print(l)
# print(newlist)
# l.clear()
# print(l)

# l=[-1,-2,-3,-4,3,4,5,566,66,8]
# for i in l:
#     if i>=0:
#         print(f"this {i} is positive")
#     else:
#         print(f"this {i} is negative")
        
# l=[-1,-2,-3,-4,3,4,5,566,66,8] 
# sum=0
# for i in l:
#     sum+=i
# print(sum/len(l))

# l=[12,36,56,78,2,3,44,98]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print(largest,index)
    
# l=[12,36,56,78,2,3,44,98,89]
# largest=l[0]
# second=l[0]
# for i in l:
#     if i>largest:
#         second=largest
#         largest=i
#     elif i>second:
#         second=i
# print(second)

# l=[12,36,56,78,2,3,44,98]

# for i in range(len(l)):
#     if l[i]<l[i+1]:
#       continue
#     else:
#         print("not sorted")
#         break
# else:
#     print("your list is sorted")

# a=(1,2,3,4,5,6)
# print(type(a))


#####tuple
#only have 2 methods like index and count
# a=(1,2,3,4,5,6,2,2,2)
# index=a.index(5)
# print(index)
# count=a.count(2)

# print(count)

# ##tuple unpacking

# a,b,c,d=(1,2,3,4)
# print(b)

#set --{}
#no duplicate values,mutable,unordered,-cant accesss by index- dont have index value

# s={1,2,3,4,5,6}

# s = {"Geeks", "For", "Geeks5"}
# for i in s:
#     print(i)

#dictionary

# d={"name":"sumit","age":20,"state":"haryana"}
# d={1:"hello",2:"sumit",3:20}
# d[1]="sumit"
# d.update({50:5000})#updating value
# d[33]=34#can directly add key value pair
# del d[1]
# print(d)


# d={10:100,20:200,30:300}
# for i in d:
#     print(d[i])


# help(dict)

# d={10:100,20:200,30:300}
# d.clear()
# print(d)

# a=[1,2,3,4,5]
# b=a.copy()#shallow copy
# b=a#deep copy

# b[0]=100
# print(a)

# d={10:100,20:200,30:300,60:400}
# d2={60:600,70:700,80:800}
# # d2=d.get(20)
# # print(d2)
# # print(d.values())
# for i in d2:
#     d[i]=d2[i]

# print(d)

# a=[1,2,3,4,5,4,3,2,2,1,1,1,2,2,33,3,3,34,4,4,5,5,5,55,]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
     
# d={10:100,20:200,30:300,60:400}
# d2={60:600,70:700,80:800}  
# for i in d2:
#     if i in d.keys():
#         d[i]+=d2[i] 
#     else:
#         d[i]=d2[i]
        
# print(d)

#exception handling
"""
try
except
else---runs code only if there is no exception
finally ---runs code no matter what 
raise---manually through an error
"""

# a=int(input("enter your no:--"))

# try:
#     print(10/a)
# # except ZeroDivisionError:
# except Exception as err:
#     print(f"sorry division by 0 not possible bc ther is an errro as {err}")
# else:
#     print("good there is no exception")
# finally:
#     print("i will run no matter what")
    
    
# print("i have done deicivdion")

# age=int(input("tell ur age--"))
# if age<10 or age>18:
#     raise ValueError("your age must be between 10 and 18")
# else:
#     print("welcome to the club")
    
# print("the club will sart soon")



# exception handling
# p=open(r'main.py')
# print(p.read())
# r=open("supereman.txt",'a')
# r.write("hello this is sumit and i am learnig pythjhgjkhkjhkjkjhon")
# r.close()