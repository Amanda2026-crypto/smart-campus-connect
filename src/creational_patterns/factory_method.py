"""
Factory Method Pattern
Use Case: Different payment processors for different payment types
"""

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Abstract product"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> dict:
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str) -> dict:
        pass


class CreditCardProcessor(PaymentProcessor):
    """Concrete product for credit card payments"""
    
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
    
    def process_payment(self, amount: float) -> dict:
        return {
            "status": "success",
            "method": "credit_card",
            "amount": amount,
            "transaction_id": f"CC_{hash(self.card_number)}"
        }
    
    def refund(self, transaction_id: str) -> dict:
        return {
            "status": "success",
            "method": "credit_card",
            "refund_transaction_id": f"REFUND_{transaction_id}"
        }


class PayPalProcessor(PaymentProcessor):
    """Concrete product for PayPal payments"""
    
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float) -> dict:
        return {
            "status": "success",
            "method": "paypal",
            "amount": amount,
            "transaction_id": f"PP_{hash(self.email)}"
        }
    
    def refund(self, transaction_id: str) -> dict:
        return {
            "status": "success",
            "method": "paypal",
            "refund_transaction_id": f"REFUND_{transaction_id}"
        }


class PaymentProcessorFactory(ABC):
    """Abstract creator"""
    
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass


class CreditCardProcessorFactory(PaymentProcessorFactory):
    """Concrete creator for credit card processors"""
    
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
    
    def create_processor(self) -> PaymentProcessor:
        return CreditCardProcessor(self.card_number, self.expiry, self.cvv)


class PayPalProcessorFactory(PaymentProcessorFactory):
    """Concrete creator for PayPal processors"""
    
    def __init__(self, email: str):
        self.email = email
    
    def create_processor(self) -> PaymentProcessor:
        return PayPalProcessor(self.email)