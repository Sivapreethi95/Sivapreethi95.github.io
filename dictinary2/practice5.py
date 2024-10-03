students = {"Alice":{"math":80,"english":75,"science":85},
            "Bob":{"math":70,"english":85,"science":80},
            "Charlie":{"math":85,"english":80,"science":90}}
total_marks = {}
for name in students:
    sum = 0
    for i in students[name]:
        sum = sum + (students[name][i])
    #students[name]= sum
    #print(students[name])
    total_marks[name]= sum
print("total_marks = ", total_marks)
    



    