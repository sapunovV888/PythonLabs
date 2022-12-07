import csv
import matplotlib.pyplot as plt
import numpy

try:
    with open('data1.csv', newline='') as File: 
        reader = csv.reader(File,delimiter=',')
        c = ''
        years = range(2000, 2021)
        country = []
        c = input('Enter country information about which you want to get: ')
        for row in reader:
           if row[0] ==c:
                if row[len(row)-1] != "..":
                    country.append(float(row[len(row)-1]))
                else:
                    country.append(0)
        if len(country) == 0:
            print('No such Country')
        plt.bar(years, country, width=0.6, color=numpy.random.rand(3,), label=c)
        plt.ylim([0,8])
        plt.xlabel('Year')
        plt.ylabel('month')
        plt.legend()
        plt.title('School life expectancy')
        plt.show()
except:
    print('file wasn`t found')

