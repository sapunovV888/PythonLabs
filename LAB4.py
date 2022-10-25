def task2() :
    a=7
    c = [[0]*a for i in range(a)]
    for i in range(a) :
        for j in range(a) :
            if i%2==0 and j%2==0:
                c[i][j]=1
            if i%2!=0 and j%2!=0:
                c[i][j]=1
    for i in range(a) :
        for j in range(a) :
            print(c[i][j], end=" ")
        print('\n')


def task1() :
    N=int(input('please enter size of array\n'))
    while N<0:
        N=int(input('please enter size of array that more than 0\n'))
    sum=0
    arr=[]
    for i in range(N):
        print('please enter ', i,' member of array\n')
        arr.append(int(input()))
        if i%2==0:
            sum+=arr[i]
    print('sum of couples member of array is ', sum)

print('--------------TASK1---------------')
task1()
print('--------------TASK2---------------')
task2()