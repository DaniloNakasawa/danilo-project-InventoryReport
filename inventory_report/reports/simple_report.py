from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport:
    def __init__(self) -> None:
        self.inventories: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]

        if not all_products:
            return (
                "Oldest manufacturing date: N/A\n"
                "Closest expiration date: N/A\n"
                "Company with the largest inventory: N/A"
            )

        oldest_manufacturing_date = min(
            product.manufacturing_date for product in all_products
        )
        closest_expiration_date = min(
            product.expiration_date
            for product in all_products
            if product.expiration_date > datetime.now().strftime("%Y-%m-%d")
        )

        company_inventory_count = {}
        for product in all_products:
            company_inventory_count[product.company_name] = (
                company_inventory_count.get(product.company_name, 0) + 1
            )

        largest_inventory_company = max(
            company_inventory_count, key=company_inventory_count.get
        )

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )
