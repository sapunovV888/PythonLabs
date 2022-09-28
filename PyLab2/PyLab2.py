import math 
import PyMod 

def func(x):
    while x<0 :
        x=input("please enter other value of x that more than 0 \n")
    z=float(math.exp(x)+math.sqrt(x))
    return z

def func1(n):
    while n<10 :
        n=int(input("please enter other value of x that more than 0 \n"))
    sum=0
    while n>0 :
        sum=sum+n%10
        n=n//10;
    return sum


print('----------first task----------')
x=float(input("Please enter number \n "))
z=func(x)
print('our equation is ', z, end=' ',)

print('\n----------second task----------')
n=int(input("Please enter number \n "))
sum=func1(n)
print('Sum of every digit in our number is ', sum, end=' ')

print('\n----------second task with module solution----------')
n1=int(input("Please enter number \n "))
sum1=digitsum(n1)
print('Sum of every digit in our number is ', sum1, end=' ')