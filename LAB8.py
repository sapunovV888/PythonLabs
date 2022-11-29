import csv

max=float('-inf')
min=float('inf')


try:
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            if row[0] =='Ukraine':
                if row[len(row)-1] != "..":
                        buff = float(row[len(row)-1]) 
                        if buff > max:
                            max = float(row[len(row)-1])
                        if buff < min:
                            min = float(row[len(row)-1])
                        print(' '.join(row))
except FileNotFoundError:
    print('file wasn`t found')
try:
    with open('new_data.csv', 'w', newline='') as file:
        reader = csv.writer(file, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        reader.writerow(['max ='] + [max] + ['min ='] + [min])
except FileExistsError:
    print("file not exist")
try:
    with open('new_data.csv', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in reader:
            print(' '.join(row))
except FileNotFoundError:
    print("file not found")