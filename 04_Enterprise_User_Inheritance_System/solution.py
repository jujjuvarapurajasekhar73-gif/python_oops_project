class user:

    def __init__(self, name: str, email: str) -> None:
        """
        Initializes a standard user with base profile data.
        """

        self.name: str = name
        self.email: str = email

    def get_profile_details(self) -> str:

        """
        Returns a formatted string containing user profile details.
        """
        return f"User: {self.name} | Email: {self.email}"

class primeuser(user):
    def __init__(self, name: str, email: str, prime_fee: float) -> None:
        
        """ Initializes a prime user with extended delivery attributes. """
        super().__init__(name,email)
        self.prime_fee: float =prime_fee
    

def run_inheritance_tests() -> None:
    """
    Executes test cases to verify the inheritance behavior between user and primeuser.
    """
    print("--- Testing Standard User ---")
    normal_rider = user("Raja", "raja@email.com")
    print(normal_rider.get_profile_details())

    print("\n--- Testing Prime User (Inheritance) ---")
    
    prime_rider = primeuser("Surya", "surya@email.com", 150.0)
    print(prime_rider.get_profile_details())
    print(f"Prime Account Delivery Fee: ${prime_rider.prime_fee}")


if __name__ == "__main__":
    run_inheritance_tests()
