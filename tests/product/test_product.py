from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "product_name",
        "company_name",
        "manufacturing_date",
        "expiration_date",
        "serial_number",
        "storage_instructions",
    )
    assert product.id == "1"
    assert product.product_name == "product_name"
    assert product.company_name == "company_name"
    assert product.manufacturing_date == "manufacturing_date"
    assert product.expiration_date == "expiration_date"
    assert product.serial_number == "serial_number"
    assert product.storage_instructions == "storage_instructions"
