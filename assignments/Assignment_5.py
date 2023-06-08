def dividers(div1, div2, numb):
    if div1==0 or div2==0:
        return False
    elif numb%div1==0 and numb%div2==0:
        return True
    else:
        return False

ans = dividers(2, 5, 10)
print(ans)
ans = dividers(1, 77, 77)
print(ans)
ans = dividers(10, 2, 5)
print(ans)   
ans = dividers(0, 1, 6)
print(ans) 
ans = dividers(1, 1, 1)
print(ans)
ans = dividers(3, 7, 25)
print(ans)  