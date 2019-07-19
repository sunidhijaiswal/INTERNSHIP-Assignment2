import csv
import matplotlib.pyplot as plt

total_runs =[]
year = []
team =[]
match_id = []
batting_team = []
# function that fetch data into csv file
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
            total_runs.append(row[17])
            match_id.append(row[0])
            batting_team.append(row[2])
           # print(row)

transform()
team.sort()
total = []
# it take index of 2015
first = year.index(str(2015))
last = year.count(str(2015))+year.index(str(2015))
# it calculate team per total score in IPL 2015
for t in team:
    run = 0
    #print(team)
    for i in range(match_id.index(str(first)),match_id.index(str(last))+match_id.count(str(last))):
        #print(i)
        if (batting_team[i]==t):
            run = run + int(total_runs[i])

    total.append(run)
print(total)
print( '''This graph is plot between Team and Total_Run.Total 8 team were played in IPL 2015,where Mumbai Indians scored
          Scored most run in ipl 2015 and they beat csk by 10 runs''')
# plot graph
plt.bar(team,total,color = ['b','r','k','c','pink','black'])
plt.xticks(rotation = 90)
plt.title("Total run per Team in Year 2015",fontweight= 'bold')
plt.xlabel("Team",fontweight= 'bold')
plt.ylabel("Total_run_score",fontweight= 'bold')
plt.show()