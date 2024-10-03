employees = {"Alice":{"department":"HR","expenses":500},
             "Bob":{"department":"IT","expenses":1200},
             "Charlie":{"department":"HR","expenses":300},
             "David":{"department":"IT","expenses":800},
             "Eva":{"department":"Finance","expenses":1000}}
department_expenses = {}
for employee in employees:
    
   # print(employee)
   # print(employees[employee]["department"])

    #print(employees[employee]["expenses"])
    if employees[employee]["department"] not in department_expenses:
        department_expenses[employees[employee]["department"]] = employees[employee]["expenses"]
    else:
        department_expenses[employees[employee]["department"]] = department_expenses[employees[employee]["department"]]+employees[employee]["expenses"]
print(department_expenses)   




    