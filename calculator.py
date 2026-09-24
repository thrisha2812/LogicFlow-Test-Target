def calculate_discount(price, customer_type, years_as_member):
    discount = 0.0

    # Bug 1: Using 'and' instead of 'or'
    if customer_type == 'premium' and years_as_member > 5:
        discount = 0.20

    # Bug 2: Missing 'elif' causes double discounting
    if years_as_member > 10:
        discount = discount + 0.10
    elif years_as_member <= 5:
        discount = 0.10

    # Bug 3: Float comparison error
    if discount == 0.20:
        return 'MAX DISCOUNT APPLIED'
    elif discount == 0.30:
        return 'MAX DISCOUNT APPLIED'

    final_price = price - (price * discount)
    return final_price