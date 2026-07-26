# marks={
#     "science": 89,
#     "maths":78,
#     "comp":99,
#     "hindi":56,
#     "history":69
# }
# # print(marks["science"])
# # print(marks["history"])
# # # print(type(marks))
# # print(marks.get("sciences",0))


# # ans=marks.get("sciencee")
# # if ans is None:
# #     print("subject not there")
# # else:
# #     print(f"marks ={ans}")

# #update

# marks["science"]=99

# # print(marks)
# # print(marks,id(marks))

# marks["age"]=21
# marks["gender"]="male"
# print(marks)


# marks.update({"city": "rohtak"})
# print(marks)


student={'science': 99, 
         'maths': 78, 
         'comp': 99, 
         'hindi': 56, 
         'history': 69,
        #    'age': 21,
        #    'gender':'male', 
        #      'city': 'rohtak'
        }
# print(student,id(student))
# ans=student.pop("age")
# print(student,id(student))
# print(ans)
# print(student.clear())
# student.clear()
# print(student)
# del student
# print(student)
total=0
# for k in student.keys():
#     print(k)
#     total+=student[k]
#     print(total)
# print(total)

# for k in student.values():
#     print(k)
#     total+=k
# print(total)

# print(student.items())

# for detail in student.items():
#     sub=detail[0]
#     marks=detail[1]
#     print(sub, marks)

for k,v in student.items():
    print(k,v)