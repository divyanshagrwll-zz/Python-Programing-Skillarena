n = int(input())
if not n>0:
    print('Wrong Input')
else:
    r = int(input())
    if n<r:
        print('Wrong Input')
    else:
        if n==r:
            print(1)
        mul = n
        for q in range(r-1):
            mul*=n-1
            n-=1
        print(mul)