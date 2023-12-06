from functools import reduce

def filter_users(users, criteria):
    return list(filter(criteria, users))

def calculate_total_expenses(user):
    return sum(user["expenses"])

def calculate_total_all_expenses(filtered_users):
    return reduce(lambda x, y: x + calculate_total_expenses(y), filtered_users, 0)


users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    {"name": "Emma", "expenses": [150, 120, 80, 200]},
    {"name": "Frank", "expenses": [120, 180, 90, 250]},
    {"name": "Grace", "expenses": [90, 100, 120, 80]},
    {"name": "Harry", "expenses": [200, 250, 180, 300]},
    {"name": "Ivy", "expenses": [180, 200, 220, 240]},
    {"name": "Jack", "expenses": [100, 50, 75, 200]},
    {"name": "Kate", "expenses": [50, 75, 80, 100]},
    {"name": "Liam", "expenses": [200, 300, 50, 150]},
    {"name": "Mia", "expenses": [100, 200, 300, 400]},
    {"name": "Noah", "expenses": [150, 120, 80, 200]},
    {"name": "Olivia", "expenses": [120, 180, 90, 250]},
    {"name": "Parker", "expenses": [90, 100, 120, 80]},
    {"name": "Quinn", "expenses": [200, 250, 180, 300]},
    {"name": "Ryan", "expenses": [180, 200, 220, 240]},
    {"name": "Sophia", "expenses": [100, 50, 75, 200]},
    {"name": "Tyler", "expenses": [50, 75, 80, 100]}
]


filtered_users = filter_users(users, lambda user: sum(user["expenses"]) > 300)
total_all_expenses = calculate_total_all_expenses(filtered_users)

print("Filtered Users:", filtered_users)
print("Total All Expenses:", total_all_expenses)
