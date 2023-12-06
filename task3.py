orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    # ... (далее по списку)
]

# 1. Фильтрация заказов для определенного клиента
def filter_orders_by_customer(orders_list, customer_id):
    filtered_orders = [order for order in orders_list if order["customer_id"] == customer_id]
    return filtered_orders

# 2. Подсчет общей суммы заказов для данного клиента
def calculate_total_order_amount(orders_list):
    total_amount = sum(order["amount"] for order in orders_list)
    return total_amount

# 3. Подсчет средней стоимости заказов для данного клиента
def calculate_average_order_amount(orders_list):
    if not orders_list:
        return 0  # чтобы избежать деления на ноль

    total_amount = calculate_total_order_amount(orders_list)
    average_amount = total_amount / len(orders_list)
    return average_amount

# Пример использования
customer_id_to_filter = 101
filtered_orders = filter_orders_by_customer(orders, customer_id_to_filter)
total_order_amount = calculate_total_order_amount(filtered_orders)
average_order_amount = calculate_average_order_amount(filtered_orders)

print("Filtered Orders for Customer ID", customer_id_to_filter, ":", filtered_orders)
print("Total Order Amount:", total_order_amount)
print("Average Order Amount:", average_order_amount)
