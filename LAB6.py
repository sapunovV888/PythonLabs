
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
#в)прізвище учня, зріст якого найменше відрізняється від росту «новенького». 