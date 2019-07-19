import csv
import matplotlib.pyplot as plt
year = []
#function that fetch data into csvfile
def transform():
    with open('matches.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            year.append(row[1])

    file.close()
transform()
del year[0]
year.sort()
plt.hist(year,  histtype='bar',rwidth=0.8)
plt.xlabel('Years',fontweight='bold')
plt.ylabel('No_of_matches',fontweight='bold')
plt.title('No_of_matches played per Year in IPL',fontweight='bold')
plt.show()