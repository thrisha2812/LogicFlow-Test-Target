def calculate_average_order_value(self) -> float:
    if not self.order_manager.orders:
        return 0

    totals = []

    for order in self.order_manager.orders.values():
        total = order.calculate_total(discount_percentage=10)
        totals.append(total)

    return mean(totals)