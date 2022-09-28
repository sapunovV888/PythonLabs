def digitsum(n):
    while n<10 :
        n=int(input("please enter other value of x that more than 0 \n"))
    sum=0
    while n>0 :
        sum=sum+n%10
        n=n//10;
    return sum