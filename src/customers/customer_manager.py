class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self):
        """Displays all customer records."""
        for cust_id, details in self.customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

    def filter_customers_by_city(self, city):
        """Placeholder for filtering customers (students will implement)."""
        print(f"\nFiltering customers in {city} is not yet implemented.")

    def get_unique_locations(self):
        """Placeholder for retrieving unique locations (students will implement)."""
        print("\nUnique locations tracking is not yet implemented.")
