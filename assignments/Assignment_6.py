with open("1.txt", "r") as file:
    a = int(file.readline())

    b = int(file.readline())

    c = int(file.readline())

d = a*b
eq = d-c

with open("1.txt", "a") as file:
    file.write(str(eq))