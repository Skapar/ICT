a = {
    'Best joke ever' : 'Why should not you eat clowns? They taste funny'
}
b=input()
c=input()
a[b]=c
my = "Joke title:{0}.  Joke: {1}. "
for x, y in a.items():
    print(my.format(x,y))