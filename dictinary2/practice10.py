students = {
    "Alice": {"department": "Science", "grades": {"math": 85, "english": 78, "science": 92}, "attendance": 180, "extracurricular_activities": 5},
    "Bob": {"department": "Arts", "grades": {"history": 88, "english": 90, "geography": 84}, "attendance": 170, "extracurricular_activities": 3},
    "Charlie": {"department": "Science", "grades": {"math": 95, "english": 85, "science": 89}, "attendance": 175, "extracurricular_activities": 4},
    "David": {"department": "Commerce", "grades": {"economics": 82, "math": 78, "accounting": 85}, "attendance": 165, "extracurricular_activities": 2},
    "Eva": {"department": "Arts", "grades": {"history": 91, "english": 87, "geography": 89}, "attendance": 180, "extracurricular_activities": 6}}
department_attendance = {}
department_extracurricular = {}
for student in students:
    if students[student]["department"] not in department_attendance:
        department_attendance[students[student]["department"]] = students[student]["attendance"]
    else:
        department_attendance[students[student]["department"]]+= students[student]["attendance"]
print(department_attendance)

for student in students:
    if students[student]["department"] not in department_extracurricular:
        department_extracurricular[students[student]["department"]] = students[student]["extracurricular_activities"]
    else:
        department_extracurricular[students[student]["department"]]+= students[student]["extracurricular_activities"]
print(department_extracurricular)

