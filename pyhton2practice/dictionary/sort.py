# marks={'science': 99, 
#          'maths': 78, 
#          'comp': 99, 
#          'hindi': 56, 
#          'history': 69
# }

# # print(marks.items())
# ans=sorted(marks.items(), key= lambda x: x[0])
# print(dict(ans))

# my_lst=[("maths",66),("eng",32)]
# print(dict(my_lst))

marks={
    "sumit":[34,67,98,98],
    "hiimesh":[34,56,78,96,56,87]
  }
ans=dict(sorted(marks.items(), key=lambda x : x[0][-1]))
print(ans)

anss=dict(sorted(marks.items(),key=lambda x: sum(x[1])))
print(anss)