temperatures = {"Monday":[23,25,21,22],"Tuesday":[20,22,19,21],"Wednesday":[25,28,24,26],
                "Thursday":[22,24,20,23],"Friday":[26,27,25,28],"Saturday":[24,25,23,22],
                "Sunday":[21,22,20,19]}
avg_temperatures = {}
for days in temperatures:
    sum = 0
    for i in temperatures[days]:
       sum = sum + i
    avg_temperatures[days] =  sum / len(temperatures[days])
print(avg_temperatures)
#print (len(temperatures[days]))
       #average = sum / len(days)

    #print(average)
       #print(i)
       #sum = sum + [days][i]
    #print(sum)
       # print(temperatures[days])