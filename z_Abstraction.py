"""5. Abstraction
Abstraction focuses on exposing only essential features. In Python, this is done using the abc module.

"""
#Example:

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):  # Abstract base class
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

# Using abstraction
cc_processor = CreditCardProcessor()
paypal_processor = PayPalProcessor()

print(cc_processor.process_payment(100))  # Output: Processing credit card payment of $100
print(paypal_processor.process_payment(50))  # Output: Processing PayPal payment of $50

