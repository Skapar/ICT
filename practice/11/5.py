a = {
    'Best joke ever' : 'Why should not you eat clowns? They taste funny',
    'Another joke': 'aaaa',
    'dinosaur joke':  'bbbb',
    'The student joke' : 'cccc'
}

my = "-{0}"
print('Here are all my jokes')
for x in a.keys():
    print(my.format(x))


print('Which one do you want to see:')
d=input()

formm = ' Here is {0} ; {1}'
print('Here is', d, a[d])


