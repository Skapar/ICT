a = input().split()
print(a)

b = [i for i in a if int(i)%2==0]
c = [i for i in a if int(i)%2!=0]

print(*b)
print(*c)
