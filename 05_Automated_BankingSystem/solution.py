
# ==============================================================================
# SECTION 1: BASE BANK ACCOUNT ARCHITECTURE Blueprint
# ==============================================================================



class BankAccount:
    
    def __init__(self, bank_holder: str, initial_amount:float)-> None:
        """ 
        Initializes a base bank account with a holder name and balance. 
        
        """

        self.bank_holder: str= bank_holder
        self.balance: float= initial_amount

    def withdraw(self,amount:float)-> float:
        """ 
        Withdraws an amount from the account balance after checking limits. 
        
        """
        if self.balance < amount:
            raise ValueError("insufficient balance in your account!")
        
        self.balance -= amount

        return self.balance

    def deposit(self, amount: float) -> float:

        """ 
        Deposits an amount into the account balance after validation. 
        
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount

        return self.balance

# ==============================================================================
# SECTION 2: SPECIALIZED SUBSCRIPTION TIER (INHERITANCE & OVERRIDING)
# ==============================================================================

class SavingsAccount(BankAccount):
    def __init__(self, bank_holder:str, initial_amount:float, interest_rate:float):
        """
        Initializes a savings account with a holder name, balance, and interest rate.
        """


        super().__init__(bank_holder,initial_amount)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> float:
        """ 
        Overrides the base withdraw method to enforce a minimum balance rule. 
            
        """
        if self.balance - amount < 500.0:
            raise ValueError("Cannot withdraw! Minimum balance of $500 must be maintained.")

        return super().withdraw(amount)

# ==============================================================================
# SECTION 3: AUTOMATED DIAGNOSTIC TESTING ENGINE
# =============================================================================


def run_banking_tests() -> None:
    """
    Executes automated test cases including try-except block for transaction errors.
    """
    print("--- Testing Base Bank Account ---")
    account = BankAccount("Raja", 1000.0)
    account.withdraw(200.0)
    account.deposit(500.0)
    print(f"Raja's Final Balance: ${account.balance}")

    try:
        print("\n--- Testing Savings Account (Method Overriding) ---")

        savings = SavingsAccount("Surya", 600.0, 0.05)
        savings.withdraw(50.0)
        print(f"Surya's Balance after safe withdrawal: ${savings.balance}")

        print("\nAttempting to withdraw $100.0 from Surya's account (Should trigger minimum balance rule)...")
        savings.withdraw(100.0)

    except ValueError as error:
        
        print(f"Captured Transaction Error: {error}")

    print(f"\nSurya's Final Protected Balance: ${savings.balance}")

# ==============================================================================
# SECTION 4: APPLICATION SYSTEM ENTRY POINT RUNNER
# ==============================================================================

if __name__ == "__main__":
    run_banking_tests()

