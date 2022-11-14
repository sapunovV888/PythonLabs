def first():
     a = ["hello","my"," ","lovely","world"]
     #a=[1,2,4,5,6,7,8,9,45]
     b=[]
     c=[]
     print('----------------our list is--------------- \n',a)
     x=input("please enter word that you want to use such atribut \n")
     if x in a:
         for i in range(len(a)):
            if a.index(x)> i:
                b.append(a[i])
            if a.index(x)<i:
                c.append(a[i])
         print(b)
         print(c)
     else:
         print("word isn`t found")


def second():
    a = ["hello","my","lovely","world"]
    print('----------------our list is--------------- \n',a)
    x=input('please enter word that you want to find\n')
    if x in a :
        print('index of word that we are finding is ',a.index(x))
    else:
        print('word isn`t found')

def third():
    a={"c","d"}
    print('first set is\n',a)
    b={1,2,3,4,5,6,7,8,9,0}
    print('second set is\n',b)
    a=a|b
    print('sets after union operation\n',a)

#first()
#second()
third()
