<<<<<<< HEAD

def sort_dict(dictionary) :
    sorted_classmates = {k: dictionary[k] for k in sorted(dictionary, reverse=True)}
    print('our dict sorted by height\n ',sorted_classmates)
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
print('our unsorted dictionary\n', classmates)
sorted_classmates=sort_dict(classmates)
new_dict=invert(sorted_classmates)
height_new=185
print('new boy height is: ', height_new)
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
=======

classmates={186:'Sapunov',192: 'Petrushanko',182: 'Naumenko',178:'Buryak',180:'Pushkar',188:'Galuga',176:'Marinchenko',174:'Baturinko',190:'Dudarenko',170:'Shapoval'}
sorted_classmates = {k: classmates[k] for k in sorted(classmates, reverse=True)}
print('our dict sorted by height\n ',sorted_classmates)
#print (classmates)
height_new=185
surname='Tsarenko'
print('new boy Surname is: ', surname, '\nnew boy height is: ', height_new)
new_dict = {value: key for key, value in sorted_classmates.items()}
min=100
min_surname=''
j=0
print('guys that have less height than new boy')
for i in new_dict:
    if new_dict[i]<height_new:
        print(sorted_classmates.get(new_dict[i]))
    if new_dict[i]>height_new:
        j=i
    if min>abs(new_dict[i]-height_new):
        min=new_dict[i]-height_new
        min_surname=sorted_classmates.get(new_dict[i])
print('boy`s surname that on one step heighter than new boy\n ',sorted_classmates.get(new_dict[j]))

print('boy`s surname that height difference is smollest between new boy\n', min_surname)
    
    
#Задано дані про про зріст n=10 юнаків класу, впорядковані за
#зменшенням (немає жодної пари учнів, які мають однаковий зріст). На початку
#навчального року до класу вступив новий учень (його зріст не співпадає із
#зростом жодного з учнів класу, перевищує зріст самого низького учня і менше
#зросту найвищого). Скласти програму, яка визначає: а) прізвища всіх учнів,
#зріст яких менше росту «новенького»; б) прізвище учня, після якого слід
#записати прізвище «новенького», щоб впорядкованість не порушилася;
>>>>>>> main
#в)прізвище учня, зріст якого найменше відрізняється від росту «новенького». 