from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport:
    def __init__(self) -> None:
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)


def generate(self) -> str:
    oldest_manufacturing_date = min(
        product.manufacturing_date
        for inventory in self.inventories
        for product in inventory.data
    )
    closest_expiration_date = min(
        product.expiration_date
        for inventory in self.inventories
        for product in inventory.data
        if product.expiration_date > datetime.now()
    )
    company_with_largest_inventory = max(
        self.inventories, key=lambda inventory: len(inventory.data)
    ).company

    return (
        f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
        f"Closest expiration date: {closest_expiration_date}\n"
        f"Company with the largest inventory: {company_with_largest_inventory}"
    )
