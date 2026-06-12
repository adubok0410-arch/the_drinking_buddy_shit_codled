import telebot
from telebot import types

bot = telebot.TeleBot('8607180210:AAFxmRkpzj_cF_5hlEptkifqdTagqASa0ac')

user_data = {}
user_state = {}

ACTIVITY = {
    "Минимальная (сидячая работа)": 1.2,
    "Низкая (спорт 1-3 дня/нед)": 1.375,
    "Средняя (спорт 3-5 дней/нед)": 1.55,
    "Высокая (спорт 6-7 дней/нед)": 1.725,
    "Очень высокая (физ.работа + спорт)": 1.9
}

GOALS = {
    "🔥 Похудение (дефицит 15%)": 0.85,
    "💪 Набор массы (профицит 10%)": 1.1,
    "⚖️ Поддержание веса": 1.0
}


def get_gender_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.row(types.KeyboardButton('♂️ Мужской'), types.KeyboardButton('♀️ Женский'))
    return markup


def get_activity_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard = list(ACTIVITY.keys())
    markup.row(types.KeyboardButton(keyboard[0]), types.KeyboardButton(keyboard[1]), types.KeyboardButton(keyboard[2]))
    markup.row(types.KeyboardButton(keyboard[3]), types.KeyboardButton(keyboard[4]))
    return markup


def get_goals_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard = list(GOALS.keys())
    markup.row(types.KeyboardButton(keyboard[0]), types.KeyboardButton(keyboard[1]))
    markup.row(types.KeyboardButton(keyboard[-1]))
    return markup


def remove_keyboard():
    return types.ReplyKeyboardRemove()


def calculate(data):
    age = data['age']
    gender = data['gender']
    height = data['height']
    weight = data['weight']
    basic_metabolism = 0

    if gender == '♂️ Мужской':
        basic_metabolism = (10 * weight) + (6.25 * height) - (5 * age) + 161
    elif gender == '♀️ Женский':
        basic_metabolism = (10 * weight) + (6.25 * height) - (5 * age) - 5

    activity_coefficient = ACTIVITY[data['activity']]
    goal_coefficient = GOALS[data['goal']]

    calories = round(basic_metabolism * activity_coefficient * goal_coefficient)
    proteins = round(calories * 0.3 / 4)
    fats = round(calories * 0.25 / 9)
    carbohydrates = round(calories * 0.45 / 4)

    return {
        'calories': calories,
        'proteins': proteins,
        'fats': fats,
        'carbohydrates': carbohydrates
    }


def format_result(data, result):
    return f"""
🏆 **Твоя норма КБЖУ на день**
🎯 Цель: {data['goal']}
📊 Уровень активности: {data['activity']}
━━━━━━━━━━━━━━━━━
🔥 **Калории:** {result['calories']} ккал
━━━━━━━━━━━━━━━━━
🥩 **Белки:** {result['proteins']} г
🧀 **Жиры:** {result['fats']} г
🍚 **Углеводы:** {result['carbohydrates']} г
    """


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    user_state[chat_id] = 'waiting_age'
    welcome_text = "👋 Привет! Я помогу рассчитать твою норму КБЖУ.\n\n Сколько тебе лет? (напиши число)"
    bot.send_message(chat_id, welcome_text, reply_markup=remove_keyboard())


@bot.message_handler(func=lambda message: True)
def form(message):
    chat_id = message.chat.id
    state = user_state.get(chat_id)

    if chat_id not in user_data:
        user_data[chat_id] = {}

    if state == 'waiting_age':
        if message.text.isdigit():
            age = int(message.text)
            user_data[chat_id]['age'] = age
            user_state[chat_id] = 'waiting_gender'
            bot.send_message(chat_id, "✅ Теперь выбери пол:", reply_markup=get_gender_keyboard())
        else:
            bot.send_message(chat_id, "❌ Напиши возраст числом.")

    elif state == 'waiting_gender':
        if message.text in ['♂️ Мужской', '♀️ Женский']:
            user_data[chat_id]['gender'] = message.text
            user_state[chat_id] = 'waiting_height'
            bot.send_message(chat_id, '✅ Твой рост в сантиметрах?', reply_markup=remove_keyboard())
        else:
            bot.send_message(chat_id, 'Выбери пол из кнопок', reply_markup=get_gender_keyboard())

    elif state == 'waiting_height':
        if message.text.isdigit():
            height = int(message.text)
            user_data[chat_id]['height'] = height
            user_state[chat_id] = 'waiting_weight'
            bot.send_message(chat_id, '✅ Твой вес в килограммах?')
        else:
            bot.send_message(chat_id, '❌ Напиши рост числом.')

    elif state == 'waiting_weight':
        if message.text.isdigit():
            weight = int(message.text)
            user_data[chat_id]['weight'] = weight
            user_state[chat_id] = 'waiting_activity'
            bot.send_message(chat_id, '✅ Какой у тебя уровень активности?', reply_markup=get_activity_keyboard())
        else:
            bot.send_message(chat_id, '❌ Напиши вес числом.')

    elif state == 'waiting_activity':
        if message.text in ACTIVITY:
            user_data[chat_id]['activity'] = message.text
            user_state[chat_id] = 'waiting_goal'
            bot.send_message(chat_id, '✅ Какая у тебя цель?', reply_markup=get_goals_keyboard())
        else:
            bot.send_message(chat_id, '❌ Выбери активность из кнопок', reply_markup=get_activity_keyboard())

    elif state == 'waiting_goal':
        if message.text in GOALS:
            user_data[chat_id]['goal'] = message.text

            result = calculate(user_data[chat_id])

            bot.send_message(chat_id, format_result(user_data[chat_id], result), parse_mode="Markdown",
                             reply_markup=remove_keyboard())
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton('🔄 Рассчитать заново'))
            bot.send_message(chat_id, 'Нажми для нового рассчёта', reply_markup=markup)
            user_state[chat_id] = None
        else:
            bot.send_message(chat_id, '❌ Выбери цель из кнопок', reply_markup=get_goals_keyboard())

    elif message.text == '🔄 Рассчитать заново':
        start(message)


bot.polling(none_stop=True)