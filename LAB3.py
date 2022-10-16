import math

def first():
    b=input("please input string b\n ")
    while len(b) <= 7:
            b=input("please input string b again")
    print(b[3:20:3])

def second():
    b=input("please enter the number\n")
    max = int(b[0])
    for i in range(len(b)):
        if max < int(b[i]):
            max=int(b[i])
    print('maximal number is ',max)
    

def third():
    b=input("please enter string\n")
    a = b.split()
    min=len(a[0])
    for i in range(len(a)):
        if len(a[i])<min:
            min=len(a[i])
    print('lenth of the most small word in the sentance is ',min)

print('---------first task--------')
first()
print('---------second task--------')
second()
print('---------third task--------')
third()