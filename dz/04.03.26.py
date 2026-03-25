class Item:
    product_name: str
    price: float
    category: str

    def __init__(self, product_name: str, price: float, category: str) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.product_name = product_name
        self.price = price
        self.category = category

    def get_info(self) -> str:
        return f"Товар: {self.product_name}, цена: {self.price:.2f}, категория: {self.category}"

    def apply_discount(self, discount: float) -> None:
        if not 0 <= discount <= 100:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100")
        self.price *= (1 - discount / 100)


class ShoppingCart:
    products: list[Item]

    def __init__(self) -> None:
        self.products = []

    def add_item(self, item: Item) -> None:
        self.products.append(item)

    def remove_item_by_name(self, name: str) -> None:
        self.products = [item for item in self.products if item.product_name != name]

    def get_total(self) -> float:
        return sum(item.price for item in self.products)