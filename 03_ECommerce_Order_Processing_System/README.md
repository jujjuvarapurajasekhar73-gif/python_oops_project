# 🛒 Real-Time E-Commerce Order Processing Subsystem

A production-grade, object-oriented order lifecycle management engine engineered to process customer checkout data streams, compute gross transactional revenues, enforce defensive monetary guard clauses, and track multi-value business operations.

---

## 📌 Project Overview & Infrastructure Setup

This project demonstrates how to build a scalable and highly secure transactional e-commerce engine utilizing core Object-Oriented Programming (OOPs) design patterns, linear memory aggregation loops, dynamic input vetting validation keys, and structured test runners.

### 🔐 Environment Initialization Checklist:
1. **Repository Folder Setup:** Inside your main OOP projects repository, create a dedicated subdirectory named exactly `03_ECommerce_Order_Processing_System` to isolate these workspace assets cleanly.
2. **Core Source File:** Create a python runtime script file named `order_system.py` inside that workspace folder to house the operational class implementations.
3. **Documentation Layer:** Establish this master `README.md` file wrapper to guide technical recruiters through the system components and algorithmic execution pathways.

---

## 🚀 Step-by-Step Functional Execution Roadmap

To understand the core behaviors and logical transitions of this transaction framework from scratch, follow this comprehensive sequential execution breakdown layout:

### 📥 Step 1: Subsystem Ingestion & Database Memory Seeding
* **Action:** The system initializes by invoking the automated constructor `__init__()` method.
* **Backend Mechanism:** The Python Virtual Machine (PVM) allocates a fresh, isolated state register list container (`self.orders: list[dict] = []`) inside the system heap memory space. This empty master list acts as an in-memory database to store multiple dynamic transactional dictionaries holding individual order parameters safely.

### 🛡️ Step 2: Defensive Input Vetting & Order Placement Gates
* **Action:** Ingesting new checkout requests by passing target arguments to the `place_order(item_name, quantity, price_per_item)` method.
* **Backend Mechanism:** Before accepting any transaction payload, the engine runs strict business rule validations:
  * **The Quantity Gate:** Checks if the incoming `quantity` parameter is less than or equal to `0`. If true, it raises a `ValueError` to block invalid zero/negative ordering arrays.
  * **The Pricing Gate:** Audits if the `price_per_item` factor is less than or equal to `0`. If breached, another explicit `ValueError` is thrown to defend financial logic.
  * **The Mutation Phase:** Only when both validation gates pass smoothly, the engine computes the dynamic mathematical gross total (`quantity * price_per_item`). It packages the data into a structured record dictionary and appends it directly onto the internal master list stack.

### 💰 Step 3: Linear Revenue Aggregation & Stream Loops
* **Action:** Calculating total platform financial turnover by invoking the `get_total_sales()` audit tool.
* **Backend Mechanism:** The module initializes an independent floating-point variable tracking accumulator (`total_sales = 0.0`). It then initiates a fast linear traversal search sweep across the entire `self.orders` collection logs. During each iteration pass, it extracts the `"total_amount"` dictionary value key and accumulates it into the tracking box, returning a precise aggregate currency float payload.

### 🧪 Step 4: Automated System Diagnostic Testing
* **Action:** Running the core code validation pipeline via the `run_order_oops_tests()` orchestrator engine.
* **Backend Mechanism:** The pipeline spins up a new cluster node instance wrapper named `amazon_orders`. It executes automated transaction sequences (ordering laptops, adding headphones, intentionally passing negative quantities to trigger catch gates, and rendering comprehensive gross income metrics summaries) to ensure every component operates under optimal enterprise parameters.

---

## 🚀 System Architecture Flowchart

<details>
<summary>💡 <b>Click to view Core Order Component Flow</b></summary>
<br>

```text
📊 Subsystem Component Execution Flowchart:
 [ Customer Checkout Trigger ] ───> place_order Ingestion ───> Vetting Parameters
                                                                        │
                                              ┌─────────────────────────┴─────────────────────────┐
                                           PASSED                                              FAILED
                                              │                                                   │
                                              ▼                                                   ▼
                                [ Compute gross total_amount ]                     [ Raises ValueError Exception ]
                                [ Append to self.orders List ]                        (Transaction Blocked Safely)
                                              │
                                              ▼
                                get_total_sales() Invocation
                                              │
                                              ▼
                                [ Linear Traversal Sum Sweep ]
                                              │
                                              ▼
                                [ Emits Grand Total Revenue Logs ]
```
</details>

---

## 🖥️ Expected Terminal Diagnostic Output

When your custom solution code runs inside the `order_system.py` execution thread, the active terminal runtime console will exactly match the following system diagnostic telemetry logs:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
<br>

```text
--- Testing Edge Case Validation ---
Order 1 (Laptop): {'item_name': 'Laptop', 'quantity': 2, 'total_amount': 100000.0}
Order 2 (Headphones): {'item_name': 'Headphones', 'quantity': 3, 'total_amount': 45000.0}
Expected Captured Error: Quantity must be greater than zero.

--- Total E-Commerce Sales Report ---
Grand Total Revenue: \$ 145000.0
```
</details>
