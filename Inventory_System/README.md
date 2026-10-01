# 🏭 Real-Time Warehouse Inventory Management System

A production-grade, object-oriented inventory simulation subsystem engineered to monitor logistics, track stock variances, evaluate critical threshold alerts, and enforce automated business rule validation gates.

---

## 📌 Project Overview & Infrastructure Setup

This project demonstrates how to build a scalable backend inventory engine utilizing core Object-Oriented Programming (OOPs) design patterns, strong type hinting profiles, defensive validation logic keys, and structured test runners.

### 🔐 Environment Initialization Checklist:
1. **GitHub Repository Creation:** Initialize a dedicated public repository named exactly `python_oops_project`.
2. **Project Folder Architecture:** Create a root subfolder named `Inventory_System` to group module assets cleanly [mLnPGq].
3. **Core Source File:** Instantiate a python runtime executable script file named `Solutio.py` inside the workspace folder to hold the operational class structures.
4. **Documentation Layer:** Establish a root `README.md` file wrapper to guide rercruiters and engineers through the system architecture flowcharts [mLnPGq].

---

## 🚀 Step-by-Step Functional Execution Roadmap

To understand or test this subsystem framework from scratch, follow this sequential execution breakdown layout:

### 📥 Step 1: Object Instantiation & Database Memory Seeding
* **Action:** The system initializes by invoking the automated constructor `__init__()` method.
* **Backend Mechanism:** Python allocates a dedicated hardware memory block slot on the system heap grid. It pre-seeds the inventory state parameters using structured dictionary lists (`list[dict]`) holding starting asset records for Laptops, Smartphones, and Headphones cleanly.

### 🛡️ Step 2: Defensive Stock Mutation Filtering
* **Action:** Triggering sales operations or stock additions by passing target arguments to the `update_stock(item_name, quantity_change)` method.
* **Backend Mechanism:** Python initiates a linear search sweep across the inventory array loops. 
  * If a product match is isolated, a defensive guard clause checks if the requested change drops stock below `0`.
  * **The Guard Gateway Law:** If stock remains valid, the change is committed. If it drops below zero, the transaction is short-circuited instantly, raising an explicit `ValueError` crash protection block to defend database integrity. If the item doesn't exist, a "Product not found" exception is thrown instead.

### 🚨 Step 3: Proactive Threshold Scanning
* **Action:** Launching logistics audits by invoking the `check_low_stock(threshold)` method helper.
* **Backend Mechanism:** The engine runs an automated scanning sweep over the live database dictionary matrices. It measures active stock fields against a default critical danger level metric (preset to 5 units). Any struggling product is immediately transformed into a custom string warning log and returned inside an alert array stack.

### 🧪 Step 4: Automated System Diagnostic Testing
* **Action:** Running the core code pipeline execution block via the `run_oops_tests()` orchestrator function block.
* **Backend Mechanism:** The script runs standard mock transaction traces (selling laptops, adding headphones, testing edge-case negative errors, and fetching active alerts) to verify that all OOP classes, loops, and condition gates are operating under optimal industry-standard parameters.

---

## 🚀 System Architecture Flowchart

<details>
<summary>💡 <b>Click to view Core Subsystem Component Flow</b></summary>
<br>

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

## 🖥️ Expected Terminal Diagnostic Output

When your custom solution code runs inside the `Solutio.py` execution thread, the active terminal runtime console should exactly match the following system diagnostic telemetry logs:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
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
