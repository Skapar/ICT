mapp = {
    'Best joke ever' : 'Why should not you eat clowns? They taste funny.'
}
a = input()
while a != 'stop' or b != 'stop':
    b=input()
    mapp[a]=b
    a = input()

print('Here are the jokes:')
my = "Joke title: {0}.  Joke: {1}. "
for x, y in mapp.items():
    print(my.format(x,y))
