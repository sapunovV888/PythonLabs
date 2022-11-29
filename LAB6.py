
def Add(dictionary, key, surname):
  dictionary[key] = surname

def Del(dictionary, key):
  del dictionary[key]

def get_key(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k

def sort_dict(dictionary) :
    sorted_classmates = {k: dictionary[k] for k in sorted(dictionary, reverse=True)}
    print('\nour dict sorted by height\n ',sorted_classmates)
    return sorted_classmates

def invert(dictionary):
    new_dict = {value: key for key, value in dictionary.items()}
    return new_dict

def sur_less(old_dict, new_dict, height):
    a = [] 
    j=0
    for i in new_dict:
        if new_dict[i]<height_new:
            a.append(old_dict.get(new_dict[i]))
    return a

def sur_sort(old_dict, new_dict, height):
    j=0
    for i in new_dict:
        if new_dict[i]>height_new:
            j=i
    return old_dict.get(new_dict[j])

def min_sur(old_dict, new_dict, height):
    min=100
    min_surname=''
    for i in new_dict:
         if min>abs(new_dict[i]-height_new):
             min=new_dict[i]-height_new
             min_surname=old_dict.get(new_dict[i])
    return min_surname

classmates={186:'Sapunov',192: 'Petrushanko',182: 'Naumenko',178:'Buryak',180:'Pushkar',188:'Galuga',176:'Marinchenko',174:'Baturinko',190:'Dudarenko',170:'Shapoval'}
print('our start dictionary\n', classmates)
key=input('if you want to add new people please press (y), if don`t want press any key\n')
if(key=='y'):
    try:
        height=int(input('please enter height of this boy\n'))
        surname=input('please enter surname that you want to add in dict\n')
        while height in classmates.keys() or (height<0 or height>250) :
            height=int(input('please enter another height and surname of boy because boy with simular height in dict or dict is impassible\n'))
            surname=input('please enter surname that you want to add in dict\n')
        Add(classmates,int(height),surname)
    except:
        print('Error: your input string value in int variable')
dell_key=input('if you want to delete new people please press (y), if don`t want press any key\n')
if(dell_key=='y'):
   surname=str(input('please enter surname of boy who must be delete from dict\n'))
   while(get_key(classmates,surname) not in classmates):
       surname=str(input('please enter another surname of boy who must be delete from dict because that boy enabel in dict\n'))
   Del(classmates,get_key(classmates,surname)) 
print('\nour unsorted dictionary \n', classmates)
sorted_classmates=sort_dict(classmates)
new_dict=invert(sorted_classmates)
height_new=185
print('\nnew boy height is: ', height_new)
list_surnames=sur_less(sorted_classmates,new_dict,height_new)
b=sur_sort(sorted_classmates,new_dict,height_new)
c=min_sur(sorted_classmates,new_dict,height_new)
print('guys that have less height than new boy')
for i in range(len(list_surnames)):
    print(list_surnames[i])
print('boy`s surname that on one step heighter than new boy\n ',b)
print('boy`s surname that height difference is smollest between new boy\n', c)
    
#Задано дані про про зріст n=10 юнаків класу, впорядковані за
#зменшенням (немає жодної пари учнів, які мають однаковий зріст). На початку
#навчального року до класу вступив новий учень (його зріст не співпадає із
#зростом жодного з учнів класу, перевищує зріст самого низького учня і менше
#зросту найвищого). Скласти програму, яка визначає: а) прізвища всіх учнів,
#зріст яких менше росту «новенького»; б) прізвище учня, після якого слід
#записати прізвище «новенького», щоб впорядкованість не порушилася;
#в)прізвище учня, зріст якого найменше відрізняється від росту «новенького». 