import json

def output():
    try:
        with open('data.json') as f:
            json_text = f.read()
        data=json.loads(json_text)
        print(data)
    except:
        print('file wasn`t found')


def add(userheight,usersurname,usergender):
    try:
        with open('data.json') as f:
            json_text= f.read()
        data=json.loads(json_text)
        while userheight<0 or userheight>250:
            userheight=int(input('please enter another height that between 0 and 250 \n'))
        while usergender!='male' and usergender!='female':
            usergender=input('Please input valid gender of person that you want to add(male/female)\n')
        data['items'].append({'height':userheight,'surname':usersurname,'gender':usergender})
    except:
        print('file wasn`t found')
    try:
        with open('data.json','w') as f:
            json.dump(data,f)
        f.close()
        print('succesfully added\n')
    except:
        print('file wasn`t found')

def search(Surname):
    key={}
    try:
        with open('data.json') as f:
            json_text= f.read()
        data=json.loads(json_text)
        for i in range(len(data['items'])):
            if data['items'][i]['surname']==Surname:
                key=i
        print('index of dcitionary that you found is ',key,'\ninformation that you found is ',data['items'][key])
        return key
    except:
        print('surname wasn`t found')

def deleter(Surname):
        key={}
        try:
            with open('data.json') as f:
                json_text = f.read()
            data=json.loads(json_text)
            data['items'].pop(search(Surname))
            with open('data.json','w') as f:
                json.dump(data,f)
            f.close()
            print('succesfully deleted\n')
        except:
            #print('surname wasn`t found')
            print('surname isn`t in file try again\n')


        
def function():
        b_height=0
        g_height=0
        with open('data.json') as f:
            json_text = f.read()
        data=json.loads(json_text)
        for i in range(len(data['items'])):
            if data['items'][i]['gender']=='male':
                b_height=b_height+data['items'][i]['height']
            if data['items'][i]['gender']=='female':
                g_height=g_height+data['items'][i]['height']
        if g_height>b_height:
            return True
        else:
            return False
        print('file wasn`t found')

numb=1
while True:
    print("if you want to output information from file press 1\n")
    print('if you want to add person to file press 2\n')
    print('if you want to delete person from file press 3\n')
    print('if you want to find person with surname from file press 4\n')
    print('if you want to know do a girls height more than boys press 5\n')
    print('if you want to close from programm press 0\n')
    try:
        numb=int(input("input digit from menu\n"))
    except:
        print("input digit value\n")
    if(int(numb==0)):
        break
    if(int(numb)==1):
        output()
    if(int(numb)==2):
        userheight=input('Please input height of person that you want to add\n')
        usersurname=input('Please input surname of person that you want to add\n')
        usergender=input('Please input gender of person that you want to add(male/female)\n')
        add(int(userheight),usersurname,usergender)
    if(int(numb)==3):
        surnm=input("please input surname of person that must be deleted from file\n")
        deleter(surnm)
    if(int(numb)==4):
        sur=input("please input surname of person that you want to find in file\n")
        search(sur)
    if(int(numb)==5):
        if function():
            print("sum of girls height more than sum of boys height\n")
        else:
            print("sum of boys height more than sum of girls height\n")

#Задано дані про про зріст n=10 учнів класу, впорядковані за
#зменшенням (немає жодної пари учнів, які мають однаковий зріст). 
#Скласти програму, яка визначає чи перевищує сумарний зріст дівчат у класі 
#зріст хлопців.
