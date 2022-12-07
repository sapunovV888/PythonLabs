import csv
import matplotlib.pyplot as plt

try:
    with open('data1.csv', newline='') as File: 
        reader = csv.reader(File,delimiter=',')
        years = range(2000, 2021)
        usa = []
        ukraine = []
        i=0
        j=0
        for row in reader:
            if row[0] =='Ukraine':
                if row[len(row)-1] != "..":
                    ukraine.append(float(row[len(row)-1]))
                    print('hello')
                else:
                    ukraine.append(0)
            if row[0] =='United States':
                if row[len(row)-1] != "..":
                    usa.append(float(row[len(row)-1]))
                else:
                    usa.append(0)
        years = range(2000, 2021)
        plt.plot(years, ukraine, 'y-', label='Ukraine')
        plt.plot(years, usa, 'b-', label='United States of America')
        plt.axis([2000, 2020, 0, 20])
        plt.xlabel('Year')
        plt.ylabel('month')
        plt.legend()
        plt.title('School life expectancy')
        plt.show()
except:
    print('file wasn`t found')

