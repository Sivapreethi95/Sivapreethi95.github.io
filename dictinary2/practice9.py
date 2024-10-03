employees = {"Alice":{"department":"HR","salary":50000,"hours_worked":40,"expenses":500,"projects_completed":5},
             "bob":{"department":"IT","salary":70000,"hours_worked":45,"expenses":1200,"projects_completed":10},
             "charlie":{"department":"HR","salary":45000,"hours_worked":35,"expenses":300,"projects_completed":7},
             "David":{"department":"IT","salary":80000,"hours_worked":50,"expenses":800,"projects_completed":8},
             "Eva":{"department":"Finance","salary":60000,"hours_worked":30,"expenses":1000,"projects_completed":4},}
department_hours = {}
department_salaries = {}
for employee in employees:
    #print(employees[employee])
    if employees[employee]["department"] not in department_hours:
       department_hours[employees[employee]["department"]] = employees[employee]["hours_worked"]
    else:
        department_hours[employees[employee]["department"]]+= employees[employee]["hours_worked"]
print(department_hours)

for employee in employees:
    if employees[employee]["department"] not in department_salaries:
        department_salaries[employees[employee]["department"]] = employees[employee]["salary"]
    else:
        department_salaries[employees[employee]["department"]]+= employees[employee]["salary"]
print(department_salaries)
