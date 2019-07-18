import csv
import matplotlib.pyplot as plt
year = []

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
plt.xlabel('years')
plt.ylabel('no_of_matches')
plt.title('graph1')
plt.show()