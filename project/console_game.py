# ⁡⁣⁣⁢1.Приветствие игрока и 0 уровень
# 2.Первый уровень: базовый монстр
# 3.Второй уровень: мини игра и босс
# 4.Третий уроыень: мини игра и босс 
# 5.Четвертый уровень: мини игра и босс
# 6.Заключительный пятый уровень: мега босс⁡

import random
import time

def one_line(text):

    for i in text:
        
        print(i, end='', flush=True)
        time.sleep(0.05)
    
    print()

def smooth_text(text):

    for i in text:
        
        print(i, sep='\n', flush=True)
        time.sleep(0.1)
    
    print()

text_greetings = (
                  '🌟 Приветствую, отважный путник! 🌟',
                  'Рад видеть тебя в мире Приключений! 🗺️✨',
                  'Здесь тебя ждут древние загадки, опасные подземелья 🏰⚔️ и сокровища, сияющие ярче звёзд 💎🌌.', 
                  'Готовься к приключениям — судьба целого мира теперь в твоих руках! 💪🔥', 
                  'Удачи, и пусть удача всегда будет на твоей стороне! 🍀😊'
)

smooth_text(text_greetings)

def correct_name(name):

    forbidden = '0123456789-,.' 
    if not name: 
        return None
    for i in name:
        if i in forbidden:
            return None
    return name

text_of_the_comment = (
                        '🌿 Ой-ой-ой! 🌸', 'Похоже, это имя уже занято лесными духами...',
                        'или, может быть, его унёс ветер перемен? 🍃✨', 'Не беда! Давай попробуем снова —',
                        'твоё настоящее имя ждёт своего часа! ✨📜',
                        '🌟 Подсказка от мудрого дракона: Имя должно быть волшебным, но удобным для произношения! 🐉💎',
                        'Жду твой выбор с нетерпением! 💖🎨'
)
text_congratulations = ('🎉 ВООООУ! Ты просто невероятен(а)! 💥')

while True:
    
    user_name = input('Введите имя персонажа: ')
    function_name = correct_name(user_name)
    
    if function_name is None:
        smooth_text(text_of_the_comment)
    else:
        one_line(text_congratulations)
        break

user_hp = 100
user_damage = 1
user_inventory = ['1 x Зелье исцеления']

zero_text = (
             '🎮 ДОБРО ПОЖАЛОВАТЬ НА СТАРТОВУЮ ЛИНИЮ, ГЕРОЙ! 🛡️✨',
             'Твой путь начинается здесь — с нулевого уровня,',
             'где каждая победа будет шагом к легенде! 🌱🌟',
             '📊 ТВОИ СТАРТОВЫЕ ХАРАКТЕРИСТИКИ:',
             '❤️ Здоровье: 100 HP — твой запас стойкости и отваги!',
             '⚔️ Атака: 1 DMG — крошечное семя будущей силы!',
             'Не сомневайся — даже величайшие драконы 🐉',
             'начинали с малого! Твои 1 урон сегодня —',
             'это завтрашние сокрушительные удары! 💥🔥',
             '🌼 Не страшно быть новичком!',
             'Каждый великий герой когда-то делал первый шаг.',
             'Твои 100 HP — это целых 100 возможностей',
             'подняться, сразиться и стать сильнее! 💪✨',
             '🌟 Запомни:',
             'Даже самая длинная дорога начинается',
             'с первого, пусть и скромного, шага! 🛤️🍃',
             'Вперёд — к первому уровню, к первой победе! 🏆🚀',
             'Мир ждёт твоего роста! 🌍💫'
)

print()
smooth_text(zero_text)

inventar_text = (
                 '🎒 ВОТ ТВОЙ ПЕРВЫЙ СПУТНИК – ВОЛШЕБНЫЙ ИНВЕНТАРЬ! ✨',
                 '📦 СОДЕРЖИМОЕ:'
                 '▸ 1 х Зелье исцеления ❤️🌀'

)

smooth_text(inventar_text)

first_monster_hp = 5
first_monster_damage = 2 
first_monster_text = (
                      '👹 ПЕРВАЯ УГРОЗА:',
                      '«Слизень-скребок» (Уровень 0)',
                      '❤️ HP: 5',
                      '⚔️ Атака: 2',
                      'Медленный, липкий, но очень назойливый!',
                      'Питается страхом новичков… и старыми сапогами. 👞💦'
)

smooth_text(first_monster_text)

def battle(us_hp, us_damage, monster_hp, monster_damage):

    while monster_hp != 0:

        us_hp -= monster_damage
        monster_hp -= us_damage

    return us_hp 

user_hp_after_battle = battle(user_hp, user_damage, first_monster_hp, first_monster_damage)
user_hp = user_hp_after_battle

text_current_health = (
                       '❤️ ТВОЯ ЖИЗНЕННАЯ СИЛА:',
                      f'{user_hp_after_battle}/100 HP'
                       '🩸 Раны свежи, но дух непоколебим!'
                       'Капля крови на доспехах — лишь отметина отваги. 🛡️💪'
)

smooth_text(text_current_health)

first_use_of_the_potion = input('Желаете ли вы использовать зелье исцеления? ')
print()

while True:
    if first_use_of_the_potion == 'Нет' or first_use_of_the_potion == 'нет' or first_use_of_the_potion == 'НЕТ':

        print(f'Твое здоровье {user_hp}/100HP❤️')
        print('в твоем инвентаре находиться', *user_inventory)
        break

    elif first_use_of_the_potion == 'Да' or first_use_of_the_potion == 'ДА' or first_use_of_the_potion == 'да':
    
        user_hp += 10
        index_inventory = 0
        user_inventory.pop(index_inventory)
        print(f'Твое здоровье {user_hp}/100HP❤️', 'Твой инвентарь пуст!', sep='\n')
        break

    else:
        
        print('⚠️ Непонятный ответ! Пожалуйста, напишите Да или Нет')
        first_use_of_the_potion = input('Использовать зелье исцеления? (Да/Нет): ')

text_about_the_start_of_the_game = (
                                    '🌿 ОКРУЖЕНИЕ:',
                                    'Ты стоишь на древней каменной тропе, заросшей мхом.',
                                    'Воздух пахнет влажной землёй и тайнами.',
                                    'Впереди — густой лес, в котором шепчутся ветви столетних дубов.',
                                    'Где-то вдали журчит ручей, словно зовёт за собой. 🌳💧',
                                    '🎯 ЗАДАЧА УРОВНЯ:',
                                    '1️⃣ Разгадать загадку Хранителя Рощи 🧠🗝️',
                                    '2️⃣ Победить Босса слизней 👹💥'
)

print()
smooth_text(text_about_the_start_of_the_game)


game_is_running = True

while game_is_running:

    text_about_groves = (
                         '🌌 МЕСТО ВСТРЕЧИ:',
                         'Ты вышел на поляну, где воздух мерцает, словно наполнен светлячками.',
                         'В центре, на камне, покрытом бархатным мхом, сидит девушка с глазами цвета тёмного мёда.',
                         'Её платье соткано из лесных теней и лунного света.',
                         'Это Рози — дух древней мудрости этих мест. ✨',

                         '🗣️ ЕЁ ПЕРВЫЕ СЛОВА:',
                         '«Приветствую, путник. Я видела, как ты сражался со слизнями...',
                         'Недурно для начала. Но сила мышц — ничто без силы ума.',
                         'Готов ли ты разгадать мою загадку? Награда стоит того.»',
                         'Она улыбается, и в воздухе расцветают сияющие цветы-миражи. 🌸',
    )
    
    smooth_text(text_about_groves)

    question_about_the_game = input('Желаете ли вы пройти квест? ')
    print()

    if question_about_the_game.lower() == 'да':

        while True:

            CROSSES_MOVE = "X"
            NOUGHTS_MOVE = "O"
            EMPTY_CELL = "."

            COLS = 3
            ROWS = 3

            QUANTITY_CROSSES = 5
            QUANTITY_NOUGHTS = 4

            USER_STEP = "USER"
            COMP_STEP = "COMP"
            CURRENT_STEP = ''

            USER_SIGN = ""
            COMP_SIGN = ""

            USER_WINNER = "USER"
            COMP_WINNER = "COMP"
            WINNER = ''
            field = []

            noughts_and_crosses_is_running = True

            STEPS_COUNT = 0

            for i in range(COLS):
                field.append([])
                for j in range(ROWS):
                    field[i].append(EMPTY_CELL)

            for i in range(ROWS):
                for j in range(COLS):
                    print(field[i][j], end=' ')
                print()

            if random.randint(1, 1000) <= 500:
                CURRENT_STEP = USER_STEP
                USER_SIGN = CROSSES_MOVE
                COMP_SIGN = NOUGHTS_MOVE
            else:
                CURRENT_STEP = COMP_STEP
                COMP_SIGN = CROSSES_MOVE
                USER_SIGN = NOUGHTS_MOVE

            while noughts_and_crosses_is_running:
                i_input = 0
                j_input = 0
                if CURRENT_STEP == USER_STEP:
                    print('Ход игрока:')
                    continue_random = True
                    while continue_random:
                        i_input = int(input('Введите номер строки: ')) - 1
                        j_input = int(input('Введите номер столбца: ')) - 1
                        if field[i_input][j_input] == EMPTY_CELL:
                            continue_random = False
                        else:
                            print('Эта клетка уже занята')
                    field[i_input][j_input] = USER_SIGN
                    for i in range(ROWS):
                        for j in range(COLS):
                            print(field[i][j], end=' ')
                        print()
                    STEPS_COUNT += 1
                    CURRENT_STEP = COMP_STEP
                else:
                    print('Ход леса (нажмите Enter):')
                    input()
                    continue_random = True
                    while continue_random:
                        i_input = random.randint(0, ROWS - 1)
                        j_input = random.randint(0, ROWS - 1)
                        if field[i_input][j_input] == EMPTY_CELL:
                            continue_random = False
                    field[i_input][j_input] = COMP_SIGN
                    for i in range(ROWS):
                        for j in range(COLS):
                            print(field[i][j], end=' ')
                        print()
                    STEPS_COUNT += 1
                    CURRENT_STEP = USER_STEP
                if STEPS_COUNT >= 5:
                    main_diagonal = False
                    side_diagonal = False
                    verticals = False
                    horizontals = False
                    if (field[0][0] == field[1][1] == field[2][2]) and field[0][0] != EMPTY_CELL:
                        main_diagonal = True
                        if field[0][0] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif (field[2][0] == field[1][1] == field[0][2]) and field[2][0] != EMPTY_CELL:
                        side_diagonal = True
                        if field[0][2] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[0][0] == field[1][0] == field[2][0] and field[0][0] != EMPTY_CELL:
                        verticals = True
                        if field[0][0] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[0][1] == field[1][1] == field[2][1] and field[0][1] != EMPTY_CELL:
                        verticals = True
                        if field[0][1] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[0][2] == field[1][2] == field[2][2] and field[0][2] != EMPTY_CELL:
                        verticals = True
                        if field[0][2] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[0][0] == field[0][1] == field[0][2] and field[0][0] != EMPTY_CELL:
                        horizontals = True
                        if field[0][0] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[1][0] == field[1][1] == field[1][2] and field[1][0] != EMPTY_CELL:
                        horizontals = True
                        if field[1][0] == USER_SIGN:
                            WINNER = USER_WINNER
                        else:
                            WINNER = COMP_WINNER
                    elif field[2][0] == field[2][1] == field[2][2] and field[2][0] != EMPTY_CELL:
                        horizontals = True
                        if field[2][0] == USER_SIGN:
                            WINNER = USER_WINNER

                        else:
                            WINNER = COMP_WINNER
                    if main_diagonal or side_diagonal or verticals or horizontals or STEPS_COUNT == 9:
                        noughts_and_crosses_is_running = False

            if WINNER == USER_WINNER:
                print(f'Победил {user_name}')
                break
            elif WINNER == COMP_WINNER:
                print('Победил лес')
                break
            else:
                print('Ничья')

                restart = input("Хотите сыграть еще раз? (да/нет): ")

                if restart.lower() == "нет":
                    print("Спасибо за игру!")
                    break
            
        if WINNER == USER_WINNER:

               congratulatory_text_for_passing_the_Rosie = (
                                                            '🌹 ЗАГАДКА РАЗГАДАНА, ЭХО УСЛЫШАНО! 🎉',
                                                            '✨ БРАВО, ОСТРОУМНЫЙ ПУТНИК!',
                                                            'Твой ответ прозвучал по поляне, и на миг весь лес замер,',
                                                            'чтобы затем взорваться сияющим фейерверком светлячков!',
                                                            'Рози встаёт, и её платье из теней расцветает живыми розами. 🌌🌺',
                                                            '🧠 ТЫ ДОКАЗАЛ, ЧТО:',
                                                            '• Мудрость может быть острее любого клинка',
                                                            '• Умение слушать важнее умения кричать',
                                                            '• Даже у эха есть душа, если знать, как его услышать',
                                                            '• Загадки — это не стены, а двери к новому пониманию',
                   
               )

               smooth_text(congratulatory_text_for_passing_the_Rosie)

               user_damage = 20

               text_about_damage = (
                                    f'✨Поздравляю {user_name} с победой!!!'
                                    f'Твой урон теперь равен {user_damage}'
               )

               one_line(text_about_damage)
               print()

        else:

            text_of_consolation = (
                                   '🌹 НЕ РАССТРАИВАЙСЯ, ДОРОГОЙ ПУТНИК... 🌧️✨',
                                   '🍃 ЗАГАДКА НЕ РАЗГАДАНА, НО УРОК УСВОЕН',
                                   'Рози смотрит на тебя не с осуждением, а с теплой грустью, словно видит в тебе старого друга, который лишь на мгновение забыл очевидное.',
                                   '«Иногда даже самый острый ум теряет нить Ариадны в простейших лабиринтах...» — её голос звучит мягко, как шелест осенних листьев. 🍂',
            )

            smooth_text(text_of_consolation)

            print('Ты не получил наград, но не расстраививайся.')