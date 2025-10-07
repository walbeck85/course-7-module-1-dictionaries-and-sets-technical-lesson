# src/customers/manager.py

def display_customers(customer_db):
    print("\nCustomer Records:")
    for cust_id, details in customer_db.items():
        print(
            f"ID: {cust_id} | Name: {details['name']} | "
            f"Location: {details['location']} | Purchases: {details['purchases']}"
        )

def filter_customers_by_city(customer_db, city):
    """Dictionary comprehension to filter records by city (case-insensitive)."""
    filtered = {
        cid: d for cid, d in customer_db.items()
        if d.get("location", "").lower() == city.lower()
    }
    if not filtered:
        print(f"\nNo customers found in {city}.")
    else:
        print(f"\nCustomers in {city}:")
        display_customers(filtered)

def unique_locations(customer_db):
    """Set comprehension to extract the unique set of locations."""
    return {d.get("location") for d in customer_db.values() if d.get("location")}

def update_customer_location(customer_db, customer_id, new_location):
    """Update the dict in place, then recompute unique locations."""
    record = customer_db.get(customer_id)
    if not record:
        print("\nCustomer not found.")
        return None
    old = record["location"]
    record["location"] = new_location
    print(f"\nUpdated {record['name']}'s location from {old} to {new_location}.")
    return unique_locations(customer_db)