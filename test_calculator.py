from calculator import calculate_discount

def test_premium_discount():
    # Premium user, 12 years member. Should get 20% + 10% = 30% max discount.
    # Expected: "MAX DISCOUNT APPLIED"
    result = calculate_discount(100, "premium", 12)
    assert result == "MAX DISCOUNT APPLIED", f"Expected MAX DISCOUNT, got {result}"

def test_standard_user():
    # Standard user, 2 years. Should get 0 discount.
    result = calculate_discount(100, "standard", 2)
    assert result == 100.0, f"Expected 100.0, got {result}"