with open("b.txt", "w") as b:
    name=input()
    age=input()
    super=input()
    weakness=input()

    b.write(name)
    b.write(age)
    b.write(super)
    b.write(weakness)

