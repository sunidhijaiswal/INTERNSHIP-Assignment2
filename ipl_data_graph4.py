import csv
import matplotlib.pyplot as plt

year = []
match_id = []
over = []
total_run = []
bowlers = []

def transform():
    with open('matches.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            year.append(row[1])
    file.close()
    with open('deliveries.csv','r') as file1:
        reader = csv.reader(file1)
        next(reader)
        for row in reader:
            match_id.append(row[0])
            over.append(row[4])
            bowlers.append(row[8])
            total_run.append(row[17])
    file1.close()
transform()
bowler = []
first = year.index(str(2015))
last = year.index(str(2015))+year.count(str(2015))
print(first,last)
run_list = []
for i in range(match_id.index(str(first)), match_id.index(str(last)) + match_id.count(str(last))):
    if bowlers[i] not in bowler:
        bowler.append(bowlers[i])
d = {}       #for all bowler and economy
for b in bowler:
    run=0
    over = 0
    for i in range(match_id.index(str(first)),match_id.index(str(last))+match_id.count(str(last))):
        if b == bowlers[i]:
            run = run+int(total_run[i])
            if bowlers[i+1] != b:
                over += 1

    d[run/over]= b
data = {}     #for top 5 bowler economy
count =0
for i in sorted(d.keys(),reverse=True):
    if count<5:
        data[d[i]] = i
        count = count+1
    else:
        break
#print(data)
#plot graph
plt.bar(data.keys(),data.values(),width= 0.5, color='g')
plt.title("Top 5 Economical Bowler of year 2015",fontweight='bold')
plt.xlabel("Bowlers",fontweight='bold')
plt.ylabel("Economic",fontweight='bold')
plt.show()







