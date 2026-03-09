class Item:
    def __init__(self, name: str, price: float, category: str) -> None:
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.name = name
        self.price = price
        self.category = category

    def get_info(self) -> str:
        return f"Товар: {self.name}, цена: {self.price:.2f}, категория: {self.category}"

    def apply_discount(self, discount: float) -> None:
        if not 0 <= discount <= 1:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 1")
        self.price *= (1 - discount)


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item_by_name(self, name: str) -> bool:
        for i, item in enumerate(self.items):
            if item.name == name:
                del self.items[i]
                return True
        return False

    def get_total(self) -> float:
        return sum(item.price for item in self.items)


if __name__ == "__main__":
    milk = Item("Молоко", 120.0, "продукты")
    tshirt = Item("Футболка", 1500.0, "одежда")

    milk.apply_discount(0.1)

    cart = ShoppingCart()
    cart.add_item(milk)
    cart.add_item(tshirt)

    print(milk.get_info())
    print(tshirt.get_info())
    print(f"Итоговая сумма: {cart.get_total():.2f}")

    cart.remove_item_by_name("Молоко")
    print(f"После удаления 'Молоко': {cart.get_total():.2f}")
