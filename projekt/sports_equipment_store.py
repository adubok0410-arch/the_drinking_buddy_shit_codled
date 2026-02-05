from dataclasses import dataclass

@dataclass
class Inventory:
    id: int
    name: str
    sport_type: str
    material: str
    weight: int
    size: str
    price: int
    condition: str
    quantity_in_stock: int


def search_by_type_and_weight(inventory: list[Inventory]):
    while True:
        print()
        print("1: поиск по виду спорта.")
        print("2: поиск по диапозону веса.")
        print("0: выход.\n")
        choice = input("Выберите действие: ").strip()
        print()

        if choice == "1":
            sport = input("Введите вид спорта: ").strip()
            result = [item for item in inventory if item.sport_type == sport]

            if len(result) > 0:
                return result
            else:
                print("Такого вида спорта нет.")

        elif choice == "2":
            try:
                min_weight = int(input("Введите мин.вес: ").strip())
                max_weight = int(input("Введите макс.вес: ").strip())
            except:
                print("Вес нужно вводить числом!")
                continue

            result = [item for item in inventory if min_weight <= item.weight <= max_weight]

            if len(result) > 0:
                return result
            else:
                print("Такого веса нет.")

        elif choice == "0":
            return None

        else:
            print("Вы ввели неверный символ!!")
            attempt = input("Желаете ли вы повторить попытку (да/нет): ").strip()
            print()

            if attempt.lower() == "нет":
                return None

items = []
print(search_by_type_and_weight(items))