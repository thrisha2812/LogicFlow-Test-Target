def calculate_discount(price, customer_type, years_as_member, discount_rate):
    discount = 0.0

    # Bug 1: Using 'or' instead of 'and'
    if customer_type == "premium" and years_as_member > 5:
        discount = discount_rate
        # Bug 2: Missing 'elif' causes double discounting
    elif years_as_member > 10:
        discount = discount_rate + 0.10
    # Bug 3: Float comparison error
    if discount == 0.30:
        return "MAX DISCOUNT APPLIED"

    final_price = price - (price * discount)
    return final_price

# Call the function with the discount rate
print(calculate_discount(100, "premium", 12, 0.20))