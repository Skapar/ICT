d = {}

print("What do you want to do: add/delete/exit?")
a = input()
while a!='exit':

    if a == "add":
        k = input("Enter key:\n")
        v = input("Enter value:\n")

        d[k] = v
        
        print("here is the dictionary:")
        for x,y in d.items():
            print(f"- {x} : {y}")

    elif a == "delete":
        k = input("Enter key\n")

        if k in d:
            del d[k]

            print("here is the dictionary:")
            for x,y in d.items():
                print(f"- {x} : {y}")

        else:
            print(f"{k} not found in dictionary")

    print("What do you want to do: add/delete/exit?")
    a = input()