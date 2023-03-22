try:
    age = int(input("enter age: "))
    print(f"{age} years old")
except Exception as e:
    print(e)
print("execution continues")
