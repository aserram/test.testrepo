class Order:
    item = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        if payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"


order1 = Order()
order1.add_item("keyboard", 1, 50)
order1.add_item("SSD", 1, 150)
order1.add_item("USB cable", 2, 5)

print(f"Total order price: {order1.total_price()}")
order1.pay("debit", "0123456ABC")
