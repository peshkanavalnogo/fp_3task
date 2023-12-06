from functools import reduce

def filter_students(students, age=None, subjects=None):
    return list(filter(lambda student: (age is None or student["age"] == age) and
                                       (subjects is None or all(grade in student["grades"] for grade in subjects)),
                       students))

def calculate_average_grades(students):
    return list(map(lambda student: sum(student["grades"]) / len(student["grades"]), students))

def total_average_grade(average_grades):
    return reduce(lambda x, y: x + y, average_grades) / len(average_grades) if average_grades else 0

def find_top_student(students):
    return max(students, key=lambda student: sum(student["grades"]) / len(student["grades"]))


students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "David", "age": 20, "grades": [80, 85, 90, 88]},
    {"name": "Emma", "age": 22, "grades": [75, 80, 82, 78]},
    {"name": "Frank", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Grace", "age": 20, "grades": [78, 80, 75, 85]},
    {"name": "Harry", "age": 22, "grades": [92, 94, 96, 90]},
    {"name": "Ivy", "age": 21, "grades": [89, 92, 88, 94]},
    {"name": "Jack", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Kate", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Liam", "age": 21, "grades": [92, 95, 88, 94]},
    {"name": "Mia", "age": 20, "grades": [80, 85, 90, 88]},
    {"name": "Noah", "age": 22, "grades": [75, 80, 82, 78]},
    {"name": "Olivia", "age": 21, "grades": [85, 88, 90, 92]},
    {"name": "Parker", "age": 20, "grades": [78, 80, 75, 85]},
    {"name": "Quinn", "age": 22, "grades": [92, 94, 96, 90]},
    {"name": "Ryan", "age": 21, "grades": [89, 92, 88, 94]},
    {"name": "Sophia", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Tyler", "age": 22, "grades": [78, 89, 76, 85]}
]


filtered_students = filter_students(students, age=21, subjects=[90, 94])
average_grades = calculate_average_grades(filtered_students)
total_avg_grade = total_average_grade(average_grades)
top_student = find_top_student(filtered_students)

print("Filtered Students:", filtered_students)
print("Average Grades for Each Student:", average_grades)
print("Total Average Grade:", total_avg_grade)
print("Top Student:", top_student)
