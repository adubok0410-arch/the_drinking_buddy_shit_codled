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
    
GLOBAL_INVENTORY_ID = 0

def input_inventory():
    print("Введите данные инвентаря.\n")

    name = input("Название (до 20 символов): ")
    sport = input("Вид спорта (до 15 символов): ")
    material = input("Материал (до 15 символов): ")
    weight = int(input("Вес (целое число): "))
    size = input("Размер (до 10 символов): ")
    price = int(input("Цена (целое число): "))
    condition = input("Состояние (до 10 символов): ")
    quantity = int(input("Количество на складе (целое число): "))
                   
    return Inventory(
        0, name, sport, material, weight, size, price, condition, quantity
    )

def add_inventory_to_list(inventories, inventory):
    global GLOBAL_INVENTORY_ID
    GLOBAL_INVENTORY_ID += 1

    inventory.id = GLOBAL_INVENTORY_ID

    inventories.append(inventory)

def search_by_type_and_weight(inventory: list[Inventory]):
    while True:
        print("1: поиск по виду спорта.")
        print("2: поиск по диапозону веса.")
        print("0: выход.\n")
        choice = input("\nВыберите действие: ").strip()

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
            return 

        else:
            print("Вы ввели неверный символ!!")
            attempt = input("\nЖелаете ли вы повторить попытку (да/нет): ").strip()

            if attempt.lower() == "нет":
                return 
            
def inventory_sort(inventory: list[Inventory]):
    while True:
        print("1: сортировка по цене.")
        print("2: сортировка по количеству на складе.")
        print("0: выход.\n")
        choice = input("\nВыберите действие: ").strip()
        inventory_sorted = []

        if choice == '1':
            print("1: по возрастанию.")
            print("2: по убыванию.\n")
            choice_sort = input("\nВыберите действие: ").strip()

            if choice_sort == '1':
                inventory_sorted = sorted(inventory, key=lambda x: x.price)

            if choice_sort == '2':
                inventory_sorted = sorted(inventory, key=lambda x: x.price, reverse=True)
        
        elif choice == '2':
            print("1: по возрастанию.")
            print("2: по убыванию.\n")
            choice_sort = input("\nВыберите действие: ").strip()

            if choice_sort == '1':
                inventory_sorted = sorted(inventory, key=lambda x: x.quantity)

            if choice_sort == '2':
                inventory_sorted = sorted(inventory, key=lambda x: x.quantity, reverse=True)

        elif choice == "0":
            return 

        else:
            print("Вы ввели неверный символ!!")
            attempt = input("\nЖелаете ли вы повторить попытку (да/нет): ").strip()

            if attempt.lower() == "нет":
                return 
        
        print(*inventory_sorted)

def write_off(inventory: list[Inventory]):
      while True:
        try:  
            ID_items = int(input("Введите ID для списания: "))
            count_write = int(input("Сколько списать: "))
        except:
            print("ID и количество должны быть числом.\n")
            continue
        
        result = [item for item in inventory if item.id == ID_items]

        if len(result) == 0:
            print("\nТакого ID нет")
        else:
            item = result[0]

            if count_write <= 0:
                print("Количество должно быть положительным.")
                continue

            if item.quantity_in_stock < count_write:
                print("Недостаточно товара на складе.")
            else:
                item.quantity_in_stock -= count_write
                print("Списание выполнено.")
                return

        attempt = input("\nЖелаете ли вы повторить попытку (да/нет): ").strip().lower()
        
        if attempt == "нет":
            return
    
def total_cost(inventory: list[Inventory]):
    result = sum([item.price * item.quantity_in_stock for item in inventory])
    print(f'Общая стоимость склада = {result}\n')

def new_output(inventory: list[Inventory]):
    while True:
        choice = input("Желаете ли вы выволнить действие: ").strip()

        if choice.lower() == 'да':
            result = [item for item in inventory if item.condition.strip().lower() == "новый"]
            return result
        else:
            return

def mark_requires_repair(inventory: list[Inventory]):
    for item in inventory:
        if item.condition.strip().lower() != "новый" and item.condition.strip().lower() != "требует ремонта":
            item.condition = "требует ремонта"
    return inventory

def heaviest_item(inventory: list[Inventory]):
    if not inventory:
        return None
    return max(inventory, key=lambda x: x.weight)

def remove_zero_quantity(inventory: list[Inventory]):
    for item in inventory[:]:
        if item.quantity == 0:
            inventory.remove(item)
    return inventory