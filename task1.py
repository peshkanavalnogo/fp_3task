students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
    # ... (другие студенты)
]

# Фильтрация данных
def filter_students(age=None, subjects=None):
    filtered_students = students.copy()

    if age is not None:
        filtered_students = [student for student in filtered_students if student["age"] == age]

    if subjects is not None:
        filtered_students = [student for student in filtered_students if all(grade in student["grades"] for grade in subjects)]

    return filtered_students

# Преобразование данных
def calculate_average_grades(students_list):
    for student in students_list:
        grades = student["grades"]
        average_grade = sum(grades) / len(grades)
        student["average_grade"] = average_grade

    total_average = sum(student["average_grade"] for student in students_list) / len(students_list)

    return total_average

# Агрегация данных
def find_top_student(students_list):
    top_student = max(students_list, key=lambda student: student["average_grade"])
    return top_student

# Пример использования
filtered_students = filter_students(age=21, subjects=[92, 95, 88, 94])
total_average_grades = calculate_average_grades(filtered_students)
top_student = find_top_student(filtered_students)

print("Filtered Students:", filtered_students)
print("Total Average Grades:", total_average_grades)
print("Top Student:", top_student)
