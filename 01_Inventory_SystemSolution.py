class InventorySystem:
    def __init__(self) -> None:
        """
        Initializes the warehouse database inside the class object.
        """
        self.inventory: list[dict] = [
            {"item_name": "Laptop", "stock": 15, "price": 50000.0},
            {"item_name": "Smartphone", "stock": 4, "price": 20000.0},
            {"item_name": "Headphones", "stock": 25, "price": 1500.0}
        ]

    def update_stock(self, item_name: str, quantity_change: int) -> dict:
        """
        Updates the stock quantity of a specific item in the inventory.
        
        Args:
            item_name (str): The name of the product to search.
            quantity_change (int): The positive or negative change in stock.
            
        Returns:
            dict: The updated product record.
            
        Raises:
            ValueError: If stock drops below zero or the product is not found.
        """
        for product in self.inventory:
            if product["item_name"] == item_name:
                if product["stock"] + quantity_change < 0:
                    raise ValueError("Not enough stock available.")
                product["stock"] += quantity_change   
                return product
        raise ValueError("Product not found in inventory.")

    def check_low_stock(self, threshold: int = 5) -> list[str]:
        """
        Scans the inventory and detects products falling below the threshold.
        
        Args:
            threshold (int): The critical stock danger level default to 5.
            
        Returns:
            list[str]: A list of warning messages for low stock items.
        """
        low_stock_list: list[str] = []
        for product in self.inventory:
            if product["stock"] < threshold:
                low_stock_list.append(
                    f"{product['item_name']} is running low! Only {product['stock']} left."
                )
        return low_stock_list


def run_oops_tests() -> None:
    """
    Executes automated test cases to verify the InventorySystem class.
    """
    hyderabad_warehouse = InventorySystem()
    
    print("--- Testing Stock Updates ---")
    print("Laptop sold 5:", hyderabad_warehouse.update_stock("Laptop", -5))
    print("Headphones added 10:", hyderabad_warehouse.update_stock("Headphones", 10))

    print("\n--- Testing Errors ---")
    try:
        hyderabad_warehouse.update_stock("Smartphone", -10)
    except ValueError as error:
        print("Expected Error:", error)

    print("\n--- Low Stock Alerts ---")
    print("Alerts:", hyderabad_warehouse.check_low_stock())


if __name__ == "__main__":
    run_oops_tests()
