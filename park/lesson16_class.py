from dataclasses import dataclass

@dataclass
class MobilePhone:
    id: int
    name: str
    price: int
    amount: int

mobile1 = MobilePhone(1, 'iPhone 17', 85000, 15)
mobile2 = MobilePhone(2, 'Xiaome 14', 50000, 18)
