import unittest
from src.creational_patterns.factory_method import (
    CreditCardProcessorFactory, PayPalProcessorFactory
)


class TestFactoryMethod(unittest.TestCase):
    
    def test_credit_card_processor(self):
        factory = CreditCardProcessorFactory("4111111111111111", "12/25", "123")
        processor = factory.create_processor()
        
        result = processor.process_payment(150.00)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["method"], "credit_card")
        self.assertEqual(result["amount"], 150.00)
    
    def test_paypal_processor(self):
        factory = PayPalProcessorFactory("user@example.com")
        processor = factory.create_processor()
        
        result = processor.process_payment(75.50)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["method"], "paypal")
        self.assertEqual(result["amount"], 75.50)
    
    def test_refund_functionality(self):
        factory = CreditCardProcessorFactory("4111111111111111", "12/25", "123")
        processor = factory.create_processor()
        
        payment_result = processor.process_payment(100.00)
        refund_result = processor.refund(payment_result["transaction_id"])
        
        self.assertEqual(refund_result["status"], "success")
        self.assertIn("REFUND_", refund_result["refund_transaction_id"])


if __name__ == '__main__':
    unittest.main()