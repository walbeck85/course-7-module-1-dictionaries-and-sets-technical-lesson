def unique_locations(customer_db):
    """Return a set of unique locations from the customer DB."""
    return {
        d.get("location")
        for d in customer_db.values()
        if d.get("location")
    }

def update_customer_location(customer_db, customer_id, new_location):
    """Update a customer's location in-place and return updated unique locations."""
    record = customer_db.get(customer_id)
    if not record:
        print("\nCustomer not found.")
        return None
    old = record["location"]
    record["location"] = new_location
    print(f"\nUpdated {record['name']}'s location from {old} to {new_location}.")
    return unique_locations(customer_db)