
sum=0
while True:
    n=int(input('Enter a number between 1 and 10 (or 0 to exit): \n'))
    if n==0:
        print('The program is finished, the final sum is:',sum)
        break
    if n>10 or n<0:
        print("Sorry, if the number is not between 0 and 10 it's too hard for me.")
    else:
        sum+=n
        print('The sum of all your number is:',sum)


    