a = []
print('Here is the list:')
print(*a)
b=input('What do you want to add:\n')
if b!='nothing':
    a.append(b)
while b!='nothing':
    print('Here is the list:')
        
    for i in a:
        print('        -',i)

    b = input('What do you want to add:\n')
    if b=='nothing':
        break
    else:
        a.append(b)

if not a:
    print('Here is the list:\n')
else:
    print('Here is the list')
for i in a:
    print('        -',i)
print('Goodbye')
    

    
