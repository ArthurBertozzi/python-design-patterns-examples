# Define the payment strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Implement concrete payment strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid ${amount} using Credit Card.')

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid ${amount} using PayPal.')

# Context class that uses a payment strategy
class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def execute_payment(self, amount):
        self.payment_strategy.pay(amount)

# Client code
if __name__ == "__main__":
    # Client chooses Credit Card payment strategy
    credit_card_payment = CreditCardPayment()
    payment_context = PaymentContext(credit_card_payment)
    payment_context.execute_payment(100)

    # Client switches to PayPal payment strategy
    paypal_payment = PayPalPayment()
    payment_context.payment_strategy = paypal_payment
    payment_context.execute_payment(50)
