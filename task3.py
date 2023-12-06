from functools import reduce

def filter_orders_by_customer(orders, customer_id):
    return list(filter(lambda order: order["customer_id"] == customer_id, orders))

def calculate_total_order_amount(orders):
    return reduce(lambda x, y: x + y["amount"], orders, 0)

def calculate_average_order_amount(orders):
    return calculate_total_order_amount(orders) / len(orders) if orders else 0


orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 102, "amount": 120.0},
    {"order_id": 7, "customer_id": 103, "amount": 90.0},
    {"order_id": 8, "customer_id": 101, "amount": 110.0},
    {"order_id": 9, "customer_id": 102, "amount": 80.0},
    {"order_id": 10, "customer_id": 103, "amount": 200.0},
    {"order_id": 11, "customer_id": 101, "amount": 150.0},
    {"order_id": 12, "customer_id": 102, "amount": 170.0},
    {"order_id": 13, "customer_id": 103, "amount": 120.0},
    {"order_id": 14, "customer_id": 101, "amount": 130.0},
    {"order_id": 15, "customer_id": 102, "amount": 180.0},
    {"order_id": 16, "customer_id": 103, "amount": 90.0},
    {"order_id": 17, "customer_id": 101, "amount": 110.0},
    {"order_id": 18, "customer_id": 102, "amount": 200.0},
    {"order_id": 19, "customer_id": 103, "amount": 160.0},
    {"order_id": 20, "customer_id": 101, "amount": 140.0}
]


customer_id_to_filter = 101
filtered_orders = filter_orders_by_customer(orders, customer_id_to_filter)
total_order_amount = calculate_total_order_amount(filtered_orders)
average_order_amount = calculate_average_order_amount(filtered_orders)

print("Filtered Orders for Customer ID", customer_id_to_filter, ":", filtered_orders)
print("Total Order Amount:", total_order_amount)
print("Average Order Amount:", average_order_amount)
