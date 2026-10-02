# 👥 Enterprise User Profile Subscription & Inheritance Subsystem

A production-grade, object-oriented user profile management architecture engineered to demonstrate structural class hierarchy levels, dry code reusability matrices, automated super-constructor escalations, and extended subscription attribute injections.

---

## 📌 Project Overview & Infrastructure Setup

This project demonstrates how to build a scalable and extensible user account profile engine utilizing core Object-Oriented Programming (OOPs) Inheritance design patterns, object instantiation memory mapping, and structured validation test runners.

### 🔐 Environment Initialization Checklist:
1. **Repository Folder Setup:** Inside your main OOP projects repository, create a dedicated subdirectory named exactly `04_Enterprise_User_Inheritance_System` to isolate these workspace assets cleanly [mLnPGq].
2. **Core Source File:** Create a python runtime script file named `user_inheritance.py` inside that workspace folder to house the operational class definitions [mLnPGq].
3. **Documentation Layer:** Establish this master `README.md` file wrapper to guide technical reviewers through the system components and class inheritance flowcharts [mLnPGq].

---

## 🚀 Step-by-Step Functional Execution Roadmap

To understand the core reusability behaviors and memory-pointer mappings of this profile subsystem from scratch, follow this comprehensive sequential execution breakdown layout:

### 📥 Step 1: Base Parent Blueprint Mapping (`User` Class)
* **Action:** The system defines a primary abstract entity structure layout named `user`.
* **Backend Mechanism:** This class acts as the single source of truth for standard user data configuration profiles. It wraps mandatory primitive string parameters (`self.name` and `self.email`) inside its automated configuration box and provides a public shared method `get_profile_details()` to return formatted profile strings instantly.

### 🧬 Step 2: Extended Sub-Class Generation (`PrimeUser` Class)
* **Action:** Instantiating a specialized subscription tier by defining the child class structure `primeuser(user)`.
* **Backend Mechanism:** By passing the parent `user` model into the child brackets signature, Python automatically opens a structural inheritance pathway. The child class gains absolute, free access to all methods and data structures of the parent class instantly without duplicating a single row of code, enforcing the absolute DRY law.

### ⚙️ Step 3: Super-Constructor Escalation & State Injection
* **Action:** Launching a prime user instance triggers the internal `__init__` constructor gate loop.
* **Backend Mechanism:** The exact millisecond the child object is born on the heap, it executes the `super().__init__(name, email)` proxy indicator engine. This command temporarily halts the child thread, escalates the input parameters straight up to the parent constructor to map the base name and email boxes first, and then returns control to the child layer to map its unique custom float attribute (`self.prime_fee`) cleanly underneath.

### 🧪 Step 4: Automated System Diagnostic Testing
* **Action:** Running the core validation pipeline via the `run_inheritance_tests()` orchestrator function.
* **Backend Mechanism:** The pipeline spins up two separate, isolated memory structures:
  * **Instance Alpha (`normal_rider`):** A primitive `user` object containing default profile boundaries.
  * **Instance Bravo (`prime_rider`):** An advanced `primeuser` object. When bravo calls `.get_profile_details()`, Python uses its internal lookup tracking loops to find the method inside the parent class layer since it wasn't rewritten inside the child, executing the parent tool seamlessly while displaying the custom child premium delivery fee metrics cleanly on screen.

---

## 🚀 System Class Inheritance Flowchart

<details>
<summary>💡 <b>Click to view Core Subsystem Component Hierarchy</b></summary>
<br>

```text
📐 Parent-Child Inheritance Modularity Mapping:
     ┌─────────────────────────────────┐
     │   Base Parent Class: user       │ ───> Attributes: name, email
     └────────────────┬────────────────┘       └── Method: get_profile_details()
                      │
            Inherited Via Sub-Class
                      │
                      ▼
     ┌─────────────────────────────────┐
     │  Derived Child Class: primeuser │ ───> Gains name, email, and get_profile_details()
     └─────────────────────────────────┘       └── Adds Custom: prime_fee (via super())
```
</details>

---

## 🖥️ Expected Terminal Diagnostic Output

When your custom solution code runs inside the `user_inheritance.py` execution thread, the active terminal runtime console will exactly match the following system diagnostic telemetry logs:

<details>
<summary>📊 <b>Click to view Runtime Console Logs</b></summary>
<br>

```text
--- Testing Standard User ---
User: Raja | Email: raja@email.com

--- Testing Prime User (Inheritance) ---
User: Surya | Email: surya@email.com
Prime Account Delivery Fee: \$150.0
```
</details>
