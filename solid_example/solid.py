from abc import ABC, abstractmethod


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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order1 = Order()
order1.add_item("keyboard", 1, 50)
order1.add_item("SSD", 1, 150)
order1.add_item("USB cable", 2, 5)

print(f"Total order price: {order1.total_price()}")

processor = DebitPaymentProcessor()
processor.pay(order1, "0123456ABC")
