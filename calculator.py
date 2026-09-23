def calculate_average_order_value(self, data): 
    # ... 
    discount = calculate_discount(data['price'], data['customer_type'], data['years_as_member']) 
    # ... 
    return average 

def calculate_discount(price, customer_type, years_as_member):
    discount = 0.0
    # ... 
    return discount
