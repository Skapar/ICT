n = int(input('Enter the height of the pyramid: '))
d = input('Which character for the top you want to use? ')
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    
    for l in range(n):
        if l == 0 and i == 0:
            print(d , end='')

    for k in range(2 * i + 1):

        if k == 0 and i > 0:
            print('/', end='')
        elif k == 2 * i and i > 0:
            print('\\', end='')
        elif i > 0:
            if i == n - 1:
                print('_', end='')
            else:
                print(' ', end='')
    print()