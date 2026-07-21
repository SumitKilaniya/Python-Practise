marks = {
    "Sumit": 95,
    "Rahul": 88,
    "Priya": 91,
    "Aman": 76,
    "Neha": 84
}

# print(marks.keys())

# for sub in marks.keys():
#     print(sub,marks[sub],sep="/")

# for mark in marks.values():
#     print(mark)

#     print(marks.items())

for detail in marks.items():
    name=detail[0]
    mark=detail[1]
    print(name,mark)

for k,v in marks.items():
    print(k,v)


