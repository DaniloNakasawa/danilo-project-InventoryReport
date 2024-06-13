from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "123",
        "Product Name",
        "Company Name",
        "2022-09-01",
        "2023-09-01",
        "123456",
        "Store in a cool dry place",
    )
    expected = (
        "The product 123 - Product Name with serial number 123456 "
        "manufactured on 2022-09-01 by the company Company Name "
        "valid until 2023-09-01 must be stored according to the following "
        "instructions: Store in a cool dry place."
    )
    assert str(product) == expected
