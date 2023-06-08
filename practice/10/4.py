with open("b.txt", "r") as b:
    f=input()

    if f=='name':
        print(b.readlines()[0][:-1])
    elif f=='age':
        print(*b.readlines(2))
    elif f=='super':
        print(*b.readlines(3))
    else:
        print(*b.readlines(4))