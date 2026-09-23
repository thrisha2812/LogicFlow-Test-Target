from typing import List, Dict, Optional
from datetime import datetime
from statistics import mean


class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        category: str,
        price: float,
        stock: int,
        rating: float
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.rating = rating

    def is_available(self) -> bool:
        return self.stock > 0

    def update_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError(
                f"Insufficient stock for {self.name}"
            )

        self.stock -= quantity

    def apply_discount(self, percentage: float) -> float:
        discount = self.price * (percentage / 100)
        return self.price - discount

    def __str__(self):
        return (
            f"{self.name} | "
            f"{self.category} | "
            f"₹{self.price} | "
            f"Stock: {self.stock}"
        )


class Customer:
    def __init__(
        self,
        customer_id: int,
        name: str,
        email: str,
        location: str
    ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.location = location
        self.orders = []

    def add_order(self, order_id: int):
        self.orders.append(order_id)

    def get_order_count(self) -> int:
        return len(self.orders)

    def get_customer_summary(self) -> Dict:
        return {
            "id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "location": self.location,
            "orders": len(self.orders)
        }


class OrderItem:
    def __init__(
        self,
        product: Product,
        quantity: int
    ):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity

    def get_discounted_total(
        self,
        discount: float
    ) -> float:
        discounted_price = self.product.apply_discount(discount)
        return discounted_price * self.quantity


class Order:
    def __init__(
        self,
        order_id: int,
        customer: Customer
    ):
        self.order_id = order_id
        self.customer = customer
        self.items: List[OrderItem] = []
        self.status = "CREATED"
        self.created_at = datetime.now()

    def add_item(
        self,
        product: Product,
        quantity: int
    ):
        if not product.is_available():
            raise ValueError(
                f"{product.name} is out of stock"
            )

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        item = OrderItem(product, quantity)
        self.items.append(item)

    def calculate_subtotal(self) -> float:
        subtotal = 0

        for item in self.items:
            subtotal += item.get_subtotal()

        return subtotal

    def calculate_discount(
        self,
        discount_percentage: float
    ) -> float:

        total_discount = 0

        for item in self.items:
            original = item.get_subtotal()
            discounted = item.get_discounted_total(
                discount_percentage
            )

            total_discount += original - discounted

        return total_discount

    def calculate_total(
        self,
        discount_percentage: float = 0
    ) -> float:

        subtotal = self.calculate_subtotal()

        discount = self.calculate_discount(
            discount_percentage
        )

        return subtotal - discount

    def update_status(self, status: str):
        allowed_statuses = [
            "CREATED",
            "CONFIRMED",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED"
        ]

        if status not in allowed_statuses:
            raise ValueError(
                f"Invalid status: {status}"
            )

        self.status = status

    def get_summary(self) -> Dict:
        return {
            "order_id": self.order_id,
            "customer": self.customer.name,
            "items": len(self.items),
            "subtotal": self.calculate_subtotal(),
            "status": self.status,
            "created_at": str(self.created_at)
        }


class InventoryManager:
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        if product_id not in self.products:
            raise KeyError(
                f"Product {product_id} not found"
            )

        del self.products[product_id]

    def get_product(
        self,
        product_id: int
    ) -> Optional[Product]:

        return self.products.get(product_id)

    def search_products(
        self,
        keyword: str
    ) -> List[Product]:

        results = []

        for product in self.products.values():
            if (
                keyword.lower() in product.name.lower()
                or keyword.lower() in product.category.lower()
            ):
                results.append(product)

        return results

    def get_low_stock_products(
        self,
        threshold: int = 5
    ) -> List[Product]:

        return [
            product
            for product in self.products.values()
            if product.stock <= threshold
        ]

    def calculate_inventory_value(self) -> float:

        total_value = 0

        for product in self.products.values():
            total_value += (
                product.price * product.stock
            )

        return total_value


class OrderManager:
    def __init__(
        self,
        inventory: InventoryManager
    ):
        self.inventory = inventory
        self.orders: Dict[int, Order] = {}

    def create_order(
        self,
        order_id: int,
        customer: Customer
    ) -> Order:

        if order_id in self.orders:
            raise ValueError(
                "Order already exists"
            )

        order = Order(
            order_id,
            customer
        )

        self.orders[order_id] = order
        customer.add_order(order_id)

        return order

    def add_product_to_order(
        self,
        order_id: int,
        product_id: int,
        quantity: int
    ):

        if order_id not in self.orders:
            raise KeyError(
                "Order not found"
            )

        product = self.inventory.get_product(
            product_id
        )

        if product is None:
            raise KeyError(
                "Product not found"
            )

        order = self.orders[order_id]

        order.add_item(
            product,
            quantity
        )

        product.update_stock(quantity)

    def confirm_order(self, order_id: int):

        if order_id not in self.orders:
            raise KeyError(
                "Order not found"
            )

        order = self.orders[order_id]

        if len(order.items) == 0:
            raise ValueError(
                "Cannot confirm empty order"
            )

        order.update_status("CONFIRMED")

    def ship_order(self, order_id: int):

        if order_id not in self.orders:
            raise KeyError(
                "Order not found"
            )

        order = self.orders[order_id]

        if order.status != "CONFIRMED":
            raise ValueError(
                "Only confirmed orders can be shipped"
            )

        order.update_status("SHIPPED")

    def deliver_order(self, order_id: int):

        if order_id not in self.orders:
            raise KeyError(
                "Order not found"
            )

        order = self.orders[order_id]

        if order.status != "SHIPPED":
            raise ValueError(
                "Order must be shipped first"
            )

        order.update_status("DELIVERED")


class AnalyticsEngine:

    def __init__(
        self,
        inventory: InventoryManager,
        order_manager: OrderManager
    ):
        self.inventory = inventory
        self.order_manager = order_manager

    def calculate_average_order_value(self) -> float:

        if not self.order_manager.orders:
            return 0

        totals = []

        for order in self.order_manager.orders.values():

            total = order.calculate_total(
                discount_percentage=10
            )

            totals.append(total)

        return mean(totals)

    def get_category_statistics(self) -> Dict:

        category_data = {}

        for product in self.inventory.products.values():

            category = product.category

            if category not in category_data:
                category_data[category] = {
                    "count": 0,
                    "inventory_value": 0,
                    "average_price": 0
                }

            category_data[category]["count"] += 1

            category_data[category][
                "inventory_value"
            ] += product.price * product.stock

        for category, data in category_data.items():

            prices = [
                product.price
                for product in self.inventory.products.values()
                if product.category == category
            ]

            if prices:
                data["average_price"] = mean(prices)

        return category_data

    def get_sales_statistics(self) -> Dict:

        completed_orders = [
            order
            for order in self.order_manager.orders.values()
            if order.status == "DELIVERED"
        ]

        revenue = 0

        for order in completed_orders:
            revenue += order.calculate_total(
                discount_percentage=10
            )

        return {
            "completed_orders": len(
                completed_orders
            ),
            "revenue": revenue,
            "average_order_value":
                self.calculate_average_order_value()
        }


class RecommendationEngine:

    def __init__(
        self,
        inventory: InventoryManager
    ):
        self.inventory = inventory

    def recommend_by_category(
        self,
        category: str,
        limit: int = 5
    ) -> List[Product]:

        products = [
            product
            for product in self.inventory.products.values()
            if product.category.lower()
            == category.lower()
        ]

        products.sort(
            key=lambda product: product.rating,
            reverse=True
        )

        return products[:limit]

    def recommend_by_price(
        self,
        maximum_price: float,
        limit: int = 5
    ) -> List[Product]:

        products = [
            product
            for product in self.inventory.products.values()
            if product.price <= maximum_price
        ]

        products.sort(
            key=lambda product: product.rating,
            reverse=True
        )

        return products[:limit]


def create_demo_inventory() -> InventoryManager:

    inventory = InventoryManager()

    products = [
        Product(
            101,
            "Laptop Pro",
            "Electronics",
            85000,
            12,
            4.8
        ),
        Product(
            102,
            "Wireless Mouse",
            "Accessories",
            1500,
            30,
            4.3
        ),
        Product(
            103,
            "Mechanical Keyboard",
            "Accessories",
            4500,
            8,
            4.7
        ),
        Product(
            104,
            "Smartphone X",
            "Electronics",
            65000,
            15,
            4.6
        ),
        Product(
            105,
            "Tablet Air",
            "Electronics",
            42000,
            4,
            4.5
        ),
        Product(
            106,
            "USB-C Hub",
            "Accessories",
            3200,
            20,
            4.1
        ),
        Product(
            107,
            "Monitor 4K",
            "Displays",
            35000,
            6,
            4.6
        ),
        Product(
            108,
            "Webcam HD",
            "Accessories",
            5000,
            10,
            4.2
        )
    ]

    for product in products:
        inventory.add_product(product)

    return inventory


def create_demo_customer() -> Customer:

    return Customer(
        customer_id=501,
        name="Rahul Sharma",
        email="rahul@example.com",
        location="Bengaluru"
    )


def run_demo():

    inventory = create_demo_inventory()

    customer = create_demo_customer()

    order_manager = OrderManager(
        inventory
    )

    order = order_manager.create_order(
        order_id=1001,
        customer=customer
    )

    order_manager.add_product_to_order(
        1001,
        101,
        1
    )

    order_manager.add_product_to_order(
        1001,
        102,
        2
    )

    order_manager.add_product_to_order(
        1001,
        103,
        1
    )

    order_manager.confirm_order(1001)

    order_manager.ship_order(1001)

    order_manager.deliver_order(1001)

    analytics = AnalyticsEngine(
        inventory,
        order_manager
    )

    recommendations = RecommendationEngine(
        inventory
    )

    print("\nORDER SUMMARY")
    print("=" * 40)

    print(order.get_summary())

    print("\nSALES STATISTICS")
    print("=" * 40)

    print(
        analytics.get_sales_statistics()
    )

    print("\nCATEGORY STATISTICS")
    print("=" * 40)

    print(
        analytics.get_category_statistics()
    )

    print("\nLOW STOCK PRODUCTS")
    print("=" * 40)

    for product in inventory.get_low_stock_products():
        print(product)

    print("\nRECOMMENDED PRODUCTS")
    print("=" * 40)

    recommended = recommendations.recommend_by_category(
        "Electronics"
    )

    for product in recommended:
        print(product)


if __name__ == "__main__":
    run_demo()