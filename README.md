# Technical Lesson: Dictionaries & Sets

## Learning Goals

- Utilize **Dictionary Comprehensions** to filter, transform, and generate new dictionaries efficiently.
- Apply **Set Operations** for fast membership testing and duplicate elimination.
- Implement **state updates** in Python applications using dictionaries and sets for structured data management.
- Explore real-world applications of dictionary and set processing for **scalability and performance**.

## Introduction

In Python, **dictionaries** and **sets** play a crucial role in managing structured data efficiently. However, handling large datasets requires **optimized data processing techniques**. This lesson introduces **Dictionary Comprehensions** and **Set Operations**, two powerful tools for working with key-value pairs and unique data collections.

Let's consider a **customer management system** for a retail company. The system currently supports:

- Storing customer records in a dictionary.
- Adding new customers dynamically.

However, the system still lacks:

- Filtering customers based on location (**Dictionary Comprehensions**).
- Identifying unique customer locations (**Set Operations**).

To address these issues, we will:

1. **Filter customer records** using Dictionary Comprehensions.
2. **Track unique customer locations** using Set Operations.
3. **Manage dynamic state updates** efficiently without modifying the original dictionary.

## Code Along

### Setting Up the Project

To get started, clone this repository and set up the environment:

```sh
git clone <repo-url>
cd course-7-module-1-dictionaries-and-sets-technical-lesson
pip install -r requirements.txt
```

Now, let's define an initial dictionary of customers in Python:

```python
customers = {
    "cust_101": {"name": "Alice", "location": "New York", "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob", "location": "Los Angeles", "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York", "purchases": ["Tablet", "Headphones"]}
}
```

### Filtering Customers with Dictionary Comprehensions

Dictionary Comprehensions allow us to **create a filtered dictionary** efficiently.

#### Example:

```python
def filter_customers_by_city(customer_db, city):
    filtered_customers = {cust_id: details for cust_id, details in customer_db.items() if details["location"].lower() == city.lower()}
    
    if filtered_customers:
        print(f"\nCustomers in {city}:")
        for cust_id, details in filtered_customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")
    else:
        print(f"\nNo customers found in {city}.")

filter_customers_by_city(customers, "New York")
```

- Uses a **Dictionary Comprehension** to filter customers based on location.
- Dynamically updates the filtered results **without modifying the original data**.

### Tracking Unique Customer Locations with Sets

For managing customer locations, **sets** provide an efficient way to **store unique values** and eliminate duplicates.

#### Example:

```python
customer_locations = {customer["location"] for customer in customers.values()}
print("\nUnique Customer Locations:", customer_locations)
```

- Uses a **Set Comprehension** to extract unique locations.
- Automatically **removes duplicate entries**.

### State Management with Dynamic Location Updates

Instead of manually managing locations, store them dynamically in a set.

#### Example:

```python
def update_customer_location(customer_db, customer_id, new_location):
    if customer_id in customer_db:
        old_location = customer_db[customer_id]["location"]
        customer_db[customer_id]["location"] = new_location
        print(f"\nUpdated {customer_db[customer_id]['name']}'s location from {old_location} to {new_location}.")
    else:
        print("\nCustomer not found.")

update_customer_location(customers, "cust_102", "San Francisco")

# Recalculate unique locations
customer_locations = {customer["location"] for customer in customers.values()}
print("\nUpdated Unique Locations:", customer_locations)
```

- **Modifies customer location dynamically** without creating redundant records.
- **Automatically updates** the unique location set **without additional storage**.

## Best Practices for Using Dictionaries & Sets

- **Use comments** to explain logic for future maintainability.
- **Optimize filtering** with Dictionary Comprehensions for readability and performance.
- **Use Set Operations** for efficient **membership testing** and **unique value storage**.
- **Handle edge cases**, such as when no customers match the search criteria.

#### Example:

```python
def filter_customers_by_city(customer_db, city):
    filtered_customers = {cust_id: details for cust_id, details in customer_db.items() if details["location"].lower() == city.lower()}
    
    if not filtered_customers:
        print(f"\nNo customers found in {city}.")
    else:
        print(f"\nCustomers in {city}:")
        for cust_id, details in filtered_customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")
```

- **Prevents UI issues** when no matching customers are found.

## Conclusion

By mastering **Dictionaries, Dictionary Comprehensions, and Set Operations**, developers can:

- **Optimize data lookups** using dictionary methods.
- **Enhance efficiency** using Set Operations for **unique value storage**.
- **Improve application scalability** with structured data management.