from dataclasses import dataclass


@dataclass
class InventoryItem:
    item_id: int
    name: str
    sport: str
    material: str
    weight: int
    size: str
    price: int
    condition: str
    quantity: int


def _truncate(text: str, max_len: int) -> str:
    if len(text) > max_len:
        return text[:max_len]
    return text


def input_int(prompt: str, min_value: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Нужно целое число.")
            continue
        if min_value is not None and value < min_value:
            print(f"Число должно быть не меньше {min_value}.")
            continue
        return value


def input_text(prompt: str, max_len: int) -> str:
    value = input(prompt).strip()
    return _truncate(value, max_len)


def read_inventory() -> list[InventoryItem]:
    items: list[InventoryItem] = []
    count = input_int("Сколько позиций инвентаря добавить? ", min_value=0)
    for i in range(count):
        print(f"\nПозиция #{i + 1}")
        item_id = input_int("ID: ", min_value=0)
        name = input_text("Название (до 20 символов): ", 20)
        sport = input_text("Вид спорта (до 15 символов): ", 15)
        material = input_text("Материал (до 15 символов): ", 15)
        weight = input_int("Вес (целое число): ", min_value=0)
        size = input_text("Размер (до 10 символов): ", 10)
        price = input_int("Цена (целое число): ", min_value=0)
        condition = input_text("Состояние (до 10 символов): ", 10)
        quantity = input_int("Количество на складе (целое число): ", min_value=0)
        items.append(
            InventoryItem(
                item_id=item_id,
                name=name,
                sport=sport,
                material=material,
                weight=weight,
                size=size,
                price=price,
                condition=condition,
                quantity=quantity,
            )
        )
    return items


def print_items(items: list[InventoryItem]) -> None:
    if not items:
        print("Список пуст.")
        return
    header = (
        "ID | Название | Спорт | Материал | Вес | Размер | Цена | Состояние | Кол-во"
    )
    print(header)
    print("-" * len(header))
    for it in items:
        print(
            f"{it.item_id} | {it.name} | {it.sport} | {it.material} | "
            f"{it.weight} | {it.size} | {it.price} | {it.condition} | {it.quantity}"
        )


def search_by_sport_and_weight(items: list[InventoryItem]) -> None:
    sport = input_text("Введите вид спорта: ", 15)
    min_w = input_int("Мин. вес: ", min_value=0)
    max_w = input_int("Макс. вес: ", min_value=min_w)
    result = [
        it for it in items if it.sport == sport and min_w <= it.weight <= max_w
    ]
    print_items(result)


def sort_inventory(items: list[InventoryItem]) -> None:
    print("1) По цене")
    print("2) По количеству на складе (по убыванию)")
    choice = input_text("Выберите сортировку: ", 1)
    if choice == "1":
        items.sort(key=lambda it: it.price)
    elif choice == "2":
        items.sort(key=lambda it: it.quantity, reverse=True)
    else:
        print("Неизвестный выбор.")
        return
    print_items(items)


def write_off_inventory(items: list[InventoryItem]) -> None:
    item_id = input_int("ID для списания: ", min_value=0)
    amount = input_int("Сколько списать: ", min_value=0)
    for it in items:
        if it.item_id == item_id:
            it.quantity = max(0, it.quantity - amount)
            print(f"Новое количество: {it.quantity}")
            return
    print("Позиция с таким ID не найдена.")


def total_cost(items: list[InventoryItem]) -> None:
    total = sum(it.price * it.quantity for it in items)
    print(f"Общая стоимость склада: {total}")


def print_new_items(items: list[InventoryItem]) -> None:
    result = [it for it in items if it.condition == "новый"]
    print_items(result)


def mark_need_repair(items: list[InventoryItem]) -> None:
    for it in items:
        if it.condition != "новый":
            it.condition = "требует ремонта"
    print("Все позиции с состоянием не 'новый' помечены как 'требует ремонта'.")


def heaviest_items(items: list[InventoryItem]) -> None:
    if not items:
        print("Список пуст.")
        return
    max_weight = max(it.weight for it in items)
    result = [it for it in items if it.weight == max_weight]
    print_items(result)


def main() -> None:
    items = read_inventory()
    while True:
        print("\nМеню:")
        print("1) Поиск по виду спорта и диапазону веса")
        print("2) Сортировка инвентаря")
        print("3) Списать инвентарь")
        print("4) Подсчитать общую стоимость склада")
        print("5) Вывести инвентарь в состоянии 'новый'")
        print("6) Пометить как 'требует ремонта'")
        print("7) Найти самый тяжелый инвентарь")
        print("0) Выход")
        choice = input_text("Выберите действие: ", 1)
        if choice == "1":
            search_by_sport_and_weight(items)
        elif choice == "2":
            sort_inventory(items)
        elif choice == "3":
            write_off_inventory(items)
        elif choice == "4":
            total_cost(items)
        elif choice == "5":
            print_new_items(items)
        elif choice == "6":
            mark_need_repair(items)
        elif choice == "7":
            heaviest_items(items)
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
