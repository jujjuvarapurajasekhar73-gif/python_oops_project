# 💳 Real-Time Digital Ride-Sharing Wallet Subsystem

A production-grade, object-oriented digital wallet simulation engine engineered to manage user balances, process automatic ride-fare deductions, validate transaction deposits, maintain historical statement ledgers, and enforce strict financial guard clauses.

---

## 📌 Project Overview & Infrastructure Setup

This project demonstrates how to construct a state-driven financial backend engine utilizing core Object-Oriented Programming (OOPs) design patterns, structural sequence queries, defensive guard assertions, and isolated memory instance states.

### 🔐 Environment Initialization Checklist:
1. **Repository Folder Setup:** Inside your main OOP projects repository, create a dedicated subdirectory named exactly `02_Digital_Ride_Sharing_Wallet` [mLnPGq].
2. **Core Source File:** Create a python runtime script file named `wallet_system.py` inside that workspace folder to house the class implementations [mLnPGq].
3. **Documentation Layer:** Establish this `README.md` file wrapper to guide reviewers through the system component flows and testing matrices [mLnPGq].

---

## 🚀 Step-by-Step Functional Execution Roadmap

To understand or code this financial framework tracker from scratch, follow this sequential execution breakdown layout:

### 📥 Step 1: Subsystem Ingestion & Dynamic Data Seeding
* **Action:** The system initializes by invoking the automated constructor `__init__()` method.
* **Backend Mechanism:** Python allocates a fresh state register list container (`self.wallets: list[dict] = []`) inside the system heap memory. This list acts as an in-memory database to store dynamic individual user wallet dictionaries holding account details, live balances, and transaction logs.

### 🔍 Step 2: Internal Lookup Verification Loop
* **Action:** Deep scanning for account signatures utilizing the helper engine `find_wallet(username)`.
* **Backend Mechanism:** The engine performs a linear search sweep over the wallet collection loops. If a username match is isolated, it returns a direct reference pointer to that specific dictionary box. If missing, it safely returns `None`.

### 🛡️ Step 3: Defensive Account Creation Gateways
* **Action:** Onboarding fresh clients using the `create_wallet(username, initial_amount)` method interface.
* **Backend Mechanism:** Before creating any new account rows, Python fires two heavy guard validation checkpoints:
  1. Checks if the `initial_amount` drops below or equals `0`. If true, it raises a `ValueError` to block invalid currency deposits.
  2. Runs `find_wallet()` to see if the name already exists. If an account is found, it throws a duplicate error to prevent overwriting existing assets. Only when both gates pass, a new account ledger is pushed onto the array stacks.

### 💰 Step 4: Transaction Ledger Loading & Validation
* **Action:** Injecting currency balances cleanly using the `add_money(username, amount)` tool.
* **Backend Mechanism:** Checks if the addition factor is above `0` and verifies that the wallet account exists. Once validated, it directly mutates the `balance` field inside that object's dictionary and appends an explicit structured statement sub-dictionary log (`{"type": "Deposit", "amount": amount}`) onto that specific user's `history` tracking array stack.

### 🚗 Step 5: Atomic Fare Deductions & Insufficient Balance Safeguards
* **Action:** Charging fares automatically at the end of a ride pass using the `pay_for_ride(username, ride_fare)` gateway.
* **Backend Mechanism:** Runs critical business rule checks: validates fare bounds, ensures account presence, and compares the active wallet balance directly against the incoming `ride_fare`. 
  * **The Overdraft Law:** If the balance is less than the fare, the transaction is completely rolled back and short-circuited, throwing an explicit "wallet has insufficient balance" `ValueError` crash block to protect accounts from going into the negative. If valid, the fare is deducted and logged as `"Ride Payment"`.

### 📊 Step 6: Statement Summarization Summary Report
* **Action:** Auditing user accounts visually using the `show_wallet(username)` reporting engine.
* **Backend Mechanism:** Fetches the target profile reference pointer and extracts its data fields. It outputs a formatted, professional terminal ledger displaying the username, active available balance, and prints a continuous linear audit stream of the entire historical transaction statement list.

---

## 🚀 System Architecture Flowchart

<details>
<summary>💡 <b>Click to view Core Wallet Component Flow</b></summary>
<br>

```text
📊 Subsystem Component Execution Flowchart:
 [ Inbound Deposit / Fare Request ] ───> find_wallet Check ───> Account Exists?
                                                                      │
                                              ┌───────────────────────┴───────────────────────┐
                                             YES                                              NO
                                              │                                               │
                                              ▼                                               ▼
                             Evaluates Guard Validation Gates                   [ Raises ValueError Exception ]
                                              │                                      (Threat Blocked Safely)
                       ┌──────────────────────┴──────────────────────┐
                    PASSED                                        FAILED
                       │                                             │
                       ▼                                             ▼
         [ Mutates In-Memory Balance ]                 [ Triggers Overdraft Rollback ]
                       │                               (Raises Insufficient Balance Error)
                       ▼
         [ Appends History Dictionary Log ]
                       │
                       ▼
         show_wallet() Terminal Statement Output
```
</details>

---

## 🖥️ Expected Terminal Diagnostic Output

When your custom solution code runs inside the `wallet_system.py` execution thread, the active terminal runtime console will exactly match the following system diagnostic telemetry logs:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
<br>

```text
--- Testing Wallet Creation & Deposits ---

--- Testing Insufficient Balance Error ---
Expected Error: wallet has insufficient balance

 wallet account summary: surya
 wallet available balance: 570.0
wallet history:
- Deposit : 150.0
- Ride Payment : 80.0
```
</details>
