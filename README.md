# Technical Lesson: Dictionaries & Sets

## Overview
This project demonstrates how to use **Python Dictionaries and Sets** to handle structured data efficiently. The lesson introduces **Dictionary Comprehensions** for filtering and transforming data, and **Set Operations** for tracking unique values and performing efficient membership tests.

This lesson was developed as part of the Flatiron School Course 7, Module 1 — *Technical Lesson: Dictionaries and Sets*.

---

## What Was Changed
During development and debugging, the following changes were implemented:

- **Fixed imports** to use relative paths (e.g. `from .customers...`) ensuring the project runs with `python -m src.main`.
- **Added package initialization files** (`__init__.py`) in `/src` and `/src/customers` to recognize these directories as modules.
- **Separated concerns** into logical files:
  - `customer_manager.py` → Displays all customers.
  - `filters.py` → Filters customers by city using Dictionary Comprehensions.
  - `location_tracker.py` → Tracks and updates unique customer locations using Sets.
- **Added graceful error handling** for cases when no customers match a given search.
- **Updated this README** to include setup, usage, and functionality documentation.

---

## Functionality
This application simulates a **customer management system** that can:

- Display all customer records.
- Filter customers dynamically by city using **Dictionary Comprehensions**.
- Identify and track **unique customer locations** using **Set Comprehensions**.
- Update a customer’s location dynamically, automatically recalculating unique locations.

---

## Key Concepts
| Concept | Description |
|----------|--------------|
| **Dictionary Comprehension** | Efficiently filters or transforms key-value pairs. |
| **Set Comprehension** | Extracts unique elements and eliminates duplicates. |
| **Membership Testing** | Uses sets to quickly check if an element exists. |
| **State Management** | Dynamically updates records without modifying the original dataset. |

---

## Project Structure
```
src/
  main.py
  customers/
    customer_manager.py      # Display all customers
    filters.py               # Filter customers by city
    location_tracker.py      # Track and update unique locations
```

---

## Setup & Installation

1. Clone your fork of this repository:
   ```bash
   git clone git@github.com:walbeck85/course-7-module-1-dictionaries-and-sets-technical-lesson.git
   cd course-7-module-1-dictionaries-and-sets-technical-lesson
   ```
2. Install dependencies and start a new virtual environment:
   ```bash
   pipenv install && pipenv shell
   ```
3. Run the program:
   ```bash
   python -m src.main
   ```

---

## Example Output
```
Customer Records:
ID: cust_101 | Name: Alice | Location: New York | Purchases: ['Laptop', 'Mouse']
ID: cust_102 | Name: Bob | Location: Los Angeles | Purchases: ['Phone', 'Charger']
ID: cust_103 | Name: Charlie | Location: New York | Purchases: ['Tablet', 'Headphones']

Customers in New York:
ID: cust_101 | Name: Alice | Location: New York | Purchases: ['Laptop', 'Mouse']
ID: cust_103 | Name: Charlie | Location: New York | Purchases: ['Tablet', 'Headphones']

No customers found in Chicago.
Unique Customer Locations: {'Los Angeles', 'New York'}
Updated Bob's location from Los Angeles to San Francisco.
Updated Unique Locations: {'San Francisco', 'New York'}
```

---

## Tools Used
- **Python 3.13+**
- **Pipenv** for environment management
- **VSCode** for development and debugging

---

## Best Practices
- Use `dict.get()` for safe lookups.
- Keep comprehensions simple—delegate complex filters to helper functions.
- Prefer `value in set` for membership testing instead of list scans.
- Always update `README.md` when new functionality or structure is introduced.

---