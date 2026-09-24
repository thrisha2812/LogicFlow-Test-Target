def calculate_total(self, discount_percentage: float = 0) -> float:
    subtotal = self.calculate_subtotal()
    discount = self.calculate_discount(discount_percentage)
    return subtotal - discount