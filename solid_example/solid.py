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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"authorizing sms code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class EmailAuth(Authorizer):
    authorized = False

    def verify_code(self, email_code):
        print(f"authorizing email code {email_code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


order1 = Order()
order1.add_item("keyboard", 1, 50)
order1.add_item("SSD", 1, 150)
order1.add_item("USB cable", 2, 5)

print(f"Total order price: {order1.total_price()}")

payment_authorizer = EmailAuth()

processor = PaypalPaymentProcessor("adolfo@intel.com", payment_authorizer)
payment_authorizer.verify_code("0466")

processor.pay(order1)
