# 🏭 Real-Time Warehouse Inventory Management System

A production-grade, object-oriented inventory simulation subsystem engineered to monitor logistics, track stock variances, evaluate critical threshold alerts, and enforce automated business rule validation gates.

---

## 🚀 System Architecture & Capabilities

<details>
<summary>💡 <b>Click to view Core Subsystem Architecture</b></summary>
<br>

* **Encapsulated State Databases:** The system stores the active product rows (`item_name`, `stock`, `price`) securely inside the initialized class object memory heap space.
* **Defensive Stock Mutation Gates:** All inventory changes pass through a strict rule engine that dynamically blocks transactions if they cause stock balances to fall into negative numbers.
* **Proactive Monitoring Alerts:** Scans the database using dynamic threshold markers to catch low stock items early and flag logistics before empty shelves happen.

```text
📊 System Component Execution Flowchart:
 [ Active Sales / Inbound Orders ] ───> update_stock() ───> Passes Validation?
                                                               │
                                       ┌───────────────────────┴───────────────────────┐
                                      YES                                              NO
                                       │                                               │
                                       ▼                                               ▼
                         [ Commits Stock Delta Change ]                  [ Raises ValueError Exception ]
                                       │                                        (Crashes Blocked safely)
                                       ▼
                         check_low_stock() Checkpoint
                                       │
                                       ▼
                         [ Emits Terminal Warning Logs ]
```
</details>

---

## 💻 Technical Execution Source Code

<details>
<summary>📂 <b>Click to view Verified Production Solution Code</b></summary>
<br>

```python
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
```
</details>

---

## 🖥️ Active Terminal Diagnostic Output

<details>
<summary>📊 <b>Click to view Expected Runtime Console Logs</b></summary>
<br>

```text
--- Testing Stock Updates ---
Laptop sold 5: {'item_name': 'Laptop', 'stock': 10, 'price': 50000.0}
Headphones added 10: {'item_name': 'Headphones', 'stock': 35, 'price': 1500.0}

--- Testing Errors ---
Expected Error: Not enough stock available.

--- Low Stock Alerts ---
Alerts: ['Smartphone is running low! Only 4 left.']
```
</details>
