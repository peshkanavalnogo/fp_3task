users = [
    {"name": "Alice", "expenses": [100, 50, 75, 200]},
    {"name": "Bob", "expenses": [50, 75, 80, 100]},
    {"name": "Charlie", "expenses": [200, 300, 50, 150]},
    {"name": "David", "expenses": [100, 200, 300, 400]},
    # ... (другие пользователи)
]

# 1. Отфильтровать пользователей по заданным критериям
def filter_users(criteria):
    filtered_users = [user for user in users if criteria(user)]
    return filtered_users

# 2. Рассчитать общую сумму расходов для каждого пользователя
def calculate_total_expenses(user):
    return sum(user["expenses"])

# 3. Получить общую сумму расходов всех отфильтрованных пользователей
def calculate_total_all_expenses(filtered_users):
    total_expenses = sum(calculate_total_expenses(user) for user in filtered_users)
    return total_expenses

# Пример использования
# Пример критерия: фильтрация пользователей, у которых общая сумма расходов больше 300
filtered_users = filter_users(lambda user: calculate_total_expenses(user) > 300)

total_all_expenses = calculate_total_all_expenses(filtered_users)

print("Filtered Users:", filtered_users)
print("Total All Expenses:", total_all_expenses)
