def calculate_discount(price, customer_type, years_as_member):
    discount = 0.0
    
    # Fix Bug 1: Use 'and' instead of 'or' for premium membership condition
    if customer_type == "premium" and years_as_member > 5:
        discount = 0.20
        
    # Fix Bug 2 & 3: Accumulate discount and fix float comparison precision
    if years_as_member > 10:
        discount = discount + 0.10
        
    # Fix Bug 3: Safe float comparison for 0.30
    if abs(discount - 0.30) < 1e-9:
        return "MAX DISCOUNT APPLIED"
        
    final_price = price - (price * discount)
    return final_price

# This should return 80.0, but because of Bug 1 & 2, it returns 70.0
print(calculate_discount(100, "premium", 12))