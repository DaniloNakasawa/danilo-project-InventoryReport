from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)

    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = json.load(file)
            return [Product(**product) for product in data]


class CsvImporter(Importer):
    def __init__(self, path: str):
        super().__init__(path)

    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = csv.DictReader(file)
            return [Product(**product) for product in data]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
