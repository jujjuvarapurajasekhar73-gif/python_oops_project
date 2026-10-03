# =====================================================================
# 1. BASE GATEWAY INTERFACE (PARENT CLASS)
# =====================================================================

class payment:
    def __init__(self, balance: float) -> None:
        """
        Initializes the base payment gateway with a starting balance.
        """
        self.balance: float = balance

    def process_payment(self, amount: float) -> None:
        """ 
        Processes a basic deduction from the available balance. 
        """
        self.balance -= amount


# =====================================================================
# 2. SUBCLASS IMPLEMENTATION: CREDIT / DEBIT CARD GATEWAY
# =====================================================================

class cardpayment(payment):
    def __init__(self, balance: float, processing_fee: float) -> None:
        """ 
        Initializes the card payment system with a balance and processing fee. 
        """
        super().__init__(balance)
        self.processing_fee = processing_fee

    def process_payment(self, amount: float) -> None:
        """ 
        Processes card payment after adding the processing fee to the amount. 
        """
        total_cost = amount + self.processing_fee
        self.balance -= total_cost


# =====================================================================
# 3. SUBCLASS IMPLEMENTATION: UPI INTERFACE W/ RISK BOUNDARIES
# =====================================================================

class UPIPayment(payment):
    def __init__(self, balance: float, limit: float = 50000.0) -> None:
        """ 
        Initializes the UPI payment system with a balance and a daily transaction limit. 
        """
        super().__init__(balance)
        self.limit = limit

    def process_payment(self, amount: float) -> None:
        """ 
        Processes UPI payment after verifying the transaction limit. 
        """
        if amount > self.limit:
            raise ValueError("Transaction amount exceeds UPI daily limit.")
        self.balance -= amount


# =====================================================================
# 4. POLYMORPHIC RUNTIME ROUTER (INTERFACE ENGINE)
# =====================================================================

def run_universal_payment(payment_gateway: payment, amount: float) -> None:
    """
    Demonstrates Polymorphism by accepting any subclass of Payment
    and calling the appropriate overriding method dynamically.
    """
    payment_gateway.process_payment(amount)
    print(f"Payment processed successfully! Remaining Balance: ${payment_gateway.balance}")


# =====================================================================
# 5. AUTOMATED INTEGRATION TESTING ENGINE
# =====================================================================

def run_gateway_tests() -> None:
    """
    Executes automated test cases to verify core OOP pillars:
    Encapsulation, Inheritance, Method Overriding, and Polymorphism.
    """
    print("--- Testing Card Payment (Inheritance & Overriding) ---")
    card_payment = cardpayment(1000.0, 2.0)
    run_universal_payment(card_payment, 100.0)

    print("\n--- Testing UPI Payment within Limit ---")
    upi_payment = UPIPayment(2000.0)
    run_universal_payment(upi_payment, 500.0)

    print("\n--- Testing UPI Payment Exceeding Limit (Error Handling) ---")
    try:
        restricted_upi = UPIPayment(5000.0, limit=100.0)
        run_universal_payment(restricted_upi, 500.0)
    except ValueError as error:
        print(f"Captured Expected Validation Error: {error}")


# =====================================================================
# 6. SYSTEM ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    run_gateway_tests()
