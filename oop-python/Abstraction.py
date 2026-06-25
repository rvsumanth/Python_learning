from abc import ABC, abstractmethod
from typing import Dict, Any

# 1. Abstract Base Class (Defines the blueprint / contract)
class PaymentGateway(ABC):
    
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self._api_key = api_key  # Abstract/hidden internal detail

    # Concrete method: Shared by all payment gateways
    def log_transaction_start(self) -> None:
        print(f"[{self.__class__.__name__}] Initiating secure transaction for Merchant: {self.merchant_id}")

    # Abstract method: Must be implemented by every child class
    @abstractmethod
    def process_payment(self, amount: float, currency: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # Abstract method: Every gateway must support refund logic
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        pass


# 2. Concrete Implementation: Stripe (Must implement abstract methods)
class StripeGateway(PaymentGateway):
    
    def process_payment(self, amount: float, currency: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation details are abstracted away from the caller
        print(f"Processing Stripe charge of {currency} {amount}")
        return {
            "status": "success",
            "transaction_id": "ch_12345stripe",
            "gateway": "stripe"
        }

    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        print(f"Refunding Stripe transaction {transaction_id}")
        return {"status": "refunded", "tx_id": transaction_id}


# 3. Concrete Implementation: PayPal (Must implement abstract methods)
class PayPalGateway(PaymentGateway):
    
    def process_payment(self, amount: float, currency: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Processing PayPal payment of {currency} {amount}")
        return {
            "status": "success",
            "transaction_id": "PAYID-12345paypal",
            "gateway": "paypal"
        }

    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        print(f"Refunding PayPal transaction {transaction_id}")
        return {"status": "refunded", "tx_id": transaction_id}


# 4. Usage: High-level code doesn't need to know how the gateway works
def execute_checkout(gateway: PaymentGateway, amount: float):
    gateway.log_transaction_start()
    payload = {"source": "web_checkout"}
    result = gateway.process_payment(amount, "INR", payload)
    print(f"Result: {result}\n")

# Execution
if __name__ == "__main__":
    stripe = StripeGateway(merchant_id="MERCHANT_991", api_key="sk_live_stripe_key")
    paypal = PayPalGateway(merchant_id="PAYPAL_001", api_key="access_token_paypal")

    execute_checkout(stripe, 2500.00)
    execute_checkout(paypal, 1500.00)
