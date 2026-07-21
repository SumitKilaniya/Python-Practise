marks={
    "science": 40,
    "maths":50,
    "comp":88
}

print(marks)
print(type(marks))

print(marks["maths"])
print(marks["science"])
print(marks.get("mathse",-1))
ans=marks.get("history",0)
if ans==0:
    print("subjevct doesnt exoist")