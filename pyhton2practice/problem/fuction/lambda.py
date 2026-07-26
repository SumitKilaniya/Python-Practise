count=0
print(f"before everything count value {count} ")
def increase():
    global count
    count=1
    print(f"inside count value {count}")

increase()
increase()
increase()
print(f"outside function count value {count}")