import csv
import matplotlib.pyplot as plt
import numpy as np

winner = []
years = []
Team = []
#function that fetch data into csvfile
def transform():
    with open('matches.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            winner.append(row[10])
            years.append(row[1])
            Team.append(row[4])
    file.close()
transform()
year = list(set(years))
year.sort()
Teams = list(set(Team))
winner_team = []
#calculate no no_of won matches over all year
for t in Teams:
    a = []
    for y in year:
        #print(y)
        #print(year.index(y)+year.count(y))
        w = []
        for i in range(years.index(y),years.index(y)+years.count(y)):
            #print(i)
            w.append(winner[i])
        #print(w)
        a.append(w.count(t))
    winner_team.append(a)

#print(winner_team)

# plot Graph
d1 = np.array(winner_team[0])
d2 = np.array(winner_team[1])
d3 = np.array(winner_team[2])
d4 = np.array(winner_team[3])
d5 = np.array(winner_team[4])
d6 = np.array(winner_team[5])
d7 = np.array(winner_team[6])
d8 = np.array(winner_team[7])
d9 = np.array(winner_team[8])
d10 = np.array(winner_team[9])
d11 = np.array(winner_team[10])
d12 = np.array(winner_team[11])
d13 = np.array(winner_team[12])
d14 = np.array(winner_team[13])

p1 = plt.bar(year,d1,color = '#1abc9c',edgecolor = 'black')
p2 = plt.bar(year,d2,color = '#2ecc71',bottom=d1,edgecolor = 'black')
p3 = plt.bar(year,d3,color = '#3498db',bottom=d1+d2,edgecolor = 'black')
p4 = plt.bar(year,d4,color = '#9b59b6',bottom=d1+d2+d3,edgecolor = 'black')
p5 = plt.bar(year,d5,color = '#f1c40f',bottom=d1+d2+d3+d4,edgecolor = 'black')
p6 = plt.bar(year,d6,color = '#e67e22',bottom=d1+d2+d3+d4+d5,edgecolor = 'black')
p7 = plt.bar(year,d7,color = '#e744c3',bottom=d1+d2+d3+d4+d5+d6,edgecolor = 'black')
p8 = plt.bar(year,d8,color = '#badc58',bottom=d1+d2+d3+d4+d5+d6+d7,edgecolor = 'black')
p9 = plt.bar(year,d9,color = '#95a5a6',bottom=d1+d2+d3+d4+d5+d6+d7+d8,edgecolor = 'black')
p10 = plt.bar(year,d10,color = '#d35400',bottom=d1+d2+d3+d4+d5+d6+d7+d8+d9,edgecolor = 'black')
p11= plt.bar(year,d11,color = '#e056fd',bottom=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10,edgecolor = 'black')
p12= plt.bar(year,d12,color = '#ff7979',bottom=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11,edgecolor = 'black')
p13= plt.bar(year,d13,color = '#22a6b3',bottom=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12,edgecolor = 'black')
p14= plt.bar(year,d14,color = '#130f40',bottom=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12,edgecolor = 'black')
plt.xticks(year,rotation='90')
plt.xlabel("year",fontweight = 'bold')
plt.ylabel("no_of_won",fontweight = 'bold')
plt.title("No_of won matches over all years",fontweight= 'bold')
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0],p6[0],p7[0],p8[0],p9[0],p10[0],p11[0],p12[0],p13[0],p14[0]),Team, loc = "center left",bbox_to_anchor = (1,0.5))
plt.show()










