def filter_customers_by_city(customer_db, city):
    """Filter customers by city (case-insensitive) and print results."""
    filtered = {
        cid: d for cid, d in customer_db.items()
        if d.get("location", "").lower() == city.lower()
    }
    if not filtered:
        print(f"\nNo customers found in {city}.")
        return

    print(f"\nCustomers in {city}:")
    # Local import avoids circular import if any
    from .customer_manager import display_customers
    display_customers(filtered)