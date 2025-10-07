from .customers.customer_manager import display_customers
from .customers.filters import filter_customers_by_city
from .customers.location_tracker import unique_locations, update_customer_location

customers = {
    "cust_101": {"name": "Alice",   "location": "New York",     "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob",     "location": "Los Angeles",  "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York",     "purchases": ["Tablet", "Headphones"]},
}

def main():
    # 1) Display all
    display_customers(customers)

    # 2) Filter by city (dictionary comprehension)
    filter_customers_by_city(customers, "New York")
    filter_customers_by_city(customers, "Chicago")  # edge case: none found

    # 3) Unique locations (set comprehension)
    print("\nUnique Customer Locations:", unique_locations(customers))

    # 4) Update location + recompute unique locations (set ops concept)
    updated = update_customer_location(customers, "cust_102", "San Francisco")
    if updated is not None:
        print("\nUpdated Unique Locations:", updated)

if __name__ == "__main__":
    main()