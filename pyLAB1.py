import math

def first():
    a=float(input("please enter a, a must be more than 0 \n "))
    while a<0 :
       a=float( input("please enter other value for a"))
    b=float(input("please enter b, b also must be more than 0 \n "))
    while a<0 :
       b=float( input("please enter other value for b"))
    if a>b:
        x=b*a-1
    elif a == b :
        x=-10
    else :
        x=(a-5)/b
    print('answer is x = ', x)

def second():
    sum=0
    prod=1
    for i in range(21):
        if (i%2==0):
            sum+=i
        else:
            prod*=i
    print('answer is sum = ',sum,' prod =', prod)

def third():
    n=int(input("please enter the number of floors of the pyramid between 1 and 9\n"))
    while n <= 1 or n >= 9 :
        n=int(input("please enter the other number of floors of the pyramid\n"))
    for i in range(n):
        k=n-i
        while k>0:
            print(n, end=' ')
            k=k-1
        print('\n')
    for i in range(n):
        k=0
        while k<i+1:
           # print(k)
            print(n, end=' ')
            k=k+1
        print('\n')


print('----------first task----------')
first()
print('----------second task----------')
second()
print('----------third task----------')
third()
