import csv
import matplotlib.pyplot as plt

extra_runs =[]
year = []
team =[]
match_id = []
bowling_team = []
# function that fetch data into csvfile
def transform():
    with open('matches.csv','r')as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            year.append(row[1])
            if row[4] not in team:
                team.append(row[4])
    with open("deliveries.csv",'r') as file1:
        reader = csv.reader(file1)
        next(reader)                               #removing header
        for row in reader:
            extra_runs.append(row[16])
            match_id.append(row[0])
            bowling_team.append(row[3])
           # print(row)

transform()
team.sort()
extra = []
# it takes 2016 index
first = year.index(str(2016))
last = year.count(str(2016))+year.index(str(2016))
#it calculate team per extra run in 2016
for t in team:
    run = 0
    #print(team)
    for i in range(match_id.index(str(first)),match_id.index(str(last))+match_id.count(str(last))):
        #print(i)
        if (bowling_team[i]==t):
            run = run + int(extra_runs[i])

    extra.append(run)
#print(extra)
#plot graph
plt.bar(team , extra ,color = 'g')
plt.xticks(rotation='90')
plt.title(" Extra run conceded per team in year 2016",fontweight = 'bold')
plt.xlabel("Teams",fontweight = 'bold')
plt.ylabel("Extra_run",fontweight = 'bold')
plt.show()