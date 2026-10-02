class OrderSystem:
# ===================================================
# Step 1: class validation
# ===================================================

    def __init__(self) -> None:
        """
        Initializes the Order System and setups an empty orders database inside the class object.
        """
        self.orders: list[dict] = []

# ===================================================
# Step 2: placing an order
# ===================================================

    def place_order(self, item_name:str, quantity:int, price_per_item:float) ->dict:

        """
        Places a new order in the system after validation.
        
        Args:
            item_name (str): The name of the item.
            quantity (int): The number of items to order.
            price_per_item (float): The price per unit of the item.
            
        Returns:
            dict: The created order dictionary.
        """


        if quantity<=0:
            raise ValueError("Quantity must be greater than zero.")
        
        if price_per_item<=0:
            raise ValueError("Price must be greater than zero.")
        
        total_amount=quantity*price_per_item

        orders={"item_name":item_name,
                "quantity":quantity, 
                "total_amount":total_amount
        }

        self.orders.append(orders)
        
        return orders

# ===================================================
# Step 3: total sales revenue
# ===================================================

    def get_total_sales(self)->float:
        
        """
        Calculates the total sales revenue from all stored orders.
        """
        total_sales =0.0

        for order in self.orders:

            total_sales+=order["total_amount"]
        
        return total_sales
# ===================================================
# Step 4: Object Creation & Testing Engine
# ===================================================

def run_order_oops_tests() -> None:
    """
    Executes test cases using the OrderSystem class object.
    """
    
    amazon_orders = OrderSystem()

    print("\n--- Testing Edge Case Validation ---")
    try:
        print("Order 1 (Laptop):", amazon_orders.place_order("Laptop", 2, 50000.0))
        print("Order 2 (Headphones):", amazon_orders.place_order("Headphones", 3, 1500.0))
        amazon_orders.place_order("Smartphone", -1, 20000.0)
    except ValueError as error:
        print("Expected Captured Error:", error)

    print("\n--- Total E-Commerce Sales Report ---")
   
    print("Grand Total Revenue: $", amazon_orders.get_total_sales())


if __name__ == "__main__":
    run_order_oops_tests()
