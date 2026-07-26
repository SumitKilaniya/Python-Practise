def greet(name):
    print(f"hello,{name} ! have a good day")

greet("sumit")


def greet(name, age,gender):
    return f"hello {name}, your age is {age},and gender is {gender}"

ans=greet(name="sumit",gender="male",age=21)
print(ans)