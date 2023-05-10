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
    def pay(self, order):
        pass

    @abstractmethod
    def auth_sms(self,  code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

    def auth_sms(self,  code):
        print(f"Verifying SMS code {code}")
        self.verified = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

    def auth_sms(self,  code):
        raise Exception("Credit card payments don't support SMS code authorization")


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

    def auth_sms(self,  code):
        print(f"Verifying SMS code {code}")
        self.verified = True


order1 = Order()
order1.add_item("keyboard", 1, 50)
order1.add_item("SSD", 1, 150)
order1.add_item("USB cable", 2, 5)

print(f"Total order price: {order1.total_price()}")

processor = PaypalPaymentProcessor("adolfo@intel.com")
processor.auth_sms("0456")
processor.pay(order1)
