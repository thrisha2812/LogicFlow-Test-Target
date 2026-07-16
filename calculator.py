def calculate_discount(price, customer_type, years_as_member):
    discount = 0.0
    
    # Bug 1: Using 'or' instead of 'and'
    if customer_type == "premium" or years_as_member > 5:
        discount = 0.20
        
    # Bug 2: Missing 'elif' causes double discounting
    if years_as_member > 10:
        discount = discount + 0.10
        
    # Bug 3: Float comparison error
    if discount == 0.30:
        return "MAX DISCOUNT APPLIED"
        
    final_price = price - (price * discount)
    return final_price

# This should return 80.0, but because of Bug 1 & 2, it returns 70.0
print(calculate_discount(100, "premium", 12))