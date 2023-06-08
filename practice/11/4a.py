mapp = {
    'Best joke ever' : 'Why should not you eat clowns? They taste funny.'
}

while True:
    a=input()
    if a == 'stop':
        break
    b = input()
    mapp[a]=b

print('Here are the jokes:')
my = "Joke title: {0}.  Joke: {1}. "
for x, y in mapp.items():
    print(my.format(x,y))
