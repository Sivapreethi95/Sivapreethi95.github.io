hours_worked = {"Alice":{"Monday":8,"Tuesday":7,"Wednesday":8,"Thursday":7,"Friday":6},
                "Bob":{"Monday":9,"Tuesday":8,"Wednesday":8,"Thursday":8,"Friday":7},
                "Charlie":{"Monday":7,"Tuesday":6,"Wednesday":8,"Thursday":7,"Friday":7}}
total_hours = {}
for employee in hours_worked:
    sum = 0
    for days in hours_worked[employee]:
        #print(hours_worked[employee][days])
        sum = sum + hours_worked[employee][days]
    total_hours[employee] = sum
print(total_hours)

