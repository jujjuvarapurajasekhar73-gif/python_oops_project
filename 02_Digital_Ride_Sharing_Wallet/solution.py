class walletsystem:
    def __init__(self) ->None:
        self.wallets: list[dict] = []

    def find_wallet(self, username:str) ->dict| None:
        """
        Searches for a wallet using the username inside self.wallets.
        """
        for wallet in self.wallets:
             
             if  wallet["username"]==username:
                 return wallet

        return None

    def create_wallet(self, username:str, initial_amount:float):
        """
        Creates a new user wallet with safety guard clauses.
        """
        if initial_amount <=0:
            raise ValueError("The initial deposit must be greater than 0")

        if self.find_wallet(username):
            raise ValueError("already wallet existed on this name!")

        wallet={"username":username, 
                "balance":initial_amount, 
                "history":[]
        }

        self.wallets.append(wallet)

        return wallet
        
        
    def add_money(self, username: str, amount: float) -> float:
        """
        Loads money into a specific user's wallet balance.
        """
        if amount <= 0:
            raise ValueError("Amount to add must be greater than zero.")
            
        wallet = self.find_wallet(username)
        if not wallet:
            raise ValueError("wallet account not found!")

        wallet["balance"] += amount
        wallet["history"].append({
            "type": "Deposit",
            "amount": amount
        })
        return wallet["balance"]
    

    def pay_for_ride(self, username: str, ride_fare: float) -> float:
        """
        Deducts the ride fare from the user's wallet balance after validation.
        """
        if ride_fare <= 0:
            raise ValueError("ride_fare must be greater than zero!")

        wallet = self.find_wallet(username)
        if not wallet:
            raise ValueError("wallet account not found")

        if wallet["balance"] < ride_fare:
            raise ValueError("wallet has insufficient balance")

        wallet["balance"] -= ride_fare
        wallet["history"].append({
            "type": "Ride Payment",
            "amount": ride_fare
        })
        return wallet["balance"]

    
    def show_wallet(self, username: str) -> None:
        """
        Displays the wallet summary and transaction history for a user.
        """
        wallet = self.find_wallet(username)
        if not wallet:
            raise ValueError("wallet account not found")
            
        print(f"\n wallet account summary: {wallet['username']}")
        print(f" wallet available balance: {wallet['balance']}")
        
        print("wallet history:")
        if not wallet["history"]:
            print("no transaction recorded yet")
        else:
            for txn in wallet["history"]:
                print(f"- {txn['type']} : {txn['amount']}")




def run_wallet_oops_tests() -> None:
    """
    Executes test cases using the WalletSystem class object.
    """
    my_wallet_system = walletsystem()
    
    print("--- Testing Wallet Creation & Deposits ---")
    my_wallet_system.create_wallet("surya", 500.0)
    my_wallet_system.add_money("surya", 150.0)
    my_wallet_system.pay_for_ride("surya", 80.0)
    
    print("\n--- Testing Insufficient Balance Error ---")
    try:
        my_wallet_system.pay_for_ride("surya", 1000.0)
    except ValueError as error:
        print("Expected Error:", error)

    my_wallet_system.show_wallet("surya")


if __name__ == "__main__":
    run_wallet_oops_tests()
