marks={
    "science": 40,
    "maths":50,
    "comp":88,
    "age":12
}
marks["age"]=80
print(marks,id(marks))
marks["gender"]="male"
print(marks)

marks.update({"name":"sumit","city":"rohtak"})
print(marks)


marks.pop("name")
print(marks)



del marks["science"]
print(marks,id(marks))


print("maths" in marks)
print(40 in marks)