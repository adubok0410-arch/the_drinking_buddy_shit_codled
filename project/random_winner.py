import random

number_of_participants = int(input('Введите количество участников: '))
list_of_participants = []
participant_number = 1

for i in range(number_of_participants):
    # ⁡⁢⁣⁢ввод всех участников ⁡
    name = input(f'Введите ФИО {participant_number} участника: ')
    list_of_participants.append(name)
    participant_number += 1
    
number_of_winners = int(input('Введите количество победителя(-ей): '))
list_of_winners = []

for i in range(number_of_winners):
    # ⁡⁣⁢⁢рандомайзер побидителей⁡
    index_winners = random.randint(0, len(list_of_participants) - 1 - i)
    list_of_winners.append(list_of_participants[index_winners])
    list_of_participants.pop(index_winners)

print('Победители:')
print(*list_of_winners, sep='\n')