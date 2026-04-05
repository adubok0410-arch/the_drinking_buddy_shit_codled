import telebot
import telebot.types

import random

#---ТЕКСТЫ ДЛЯ НАСТРОЕНИЯ---
happy_responses = [
    "Ого, это чувствуется даже через экран! 😄\nСохраняй это настроение и делись им с миром ✨",
    "Круто! 😊 Похоже, сегодня твой день.\nМожет, сделаешь что-то ещё, что усилит это состояние?",
    "Вот это настрой! 🔥\nЗапомни, что именно делает тебя таким счастливым — это пригодится 💛",
    "Рад за тебя 😄\nИногда такие моменты — лучшие. Наслаждайся ими на полную!",
    "Звучит как отличное настроение! 🌈\nМожет, зафиксируем, что сегодня пошло особенно хорошо?"
]

normal_responses = [
    "Понял 🙂\nСпокойное состояние — это тоже хорошо.\nИногда именно в нём мы восстанавливаемся.",
    "Нормально — это уже неплохо 👍\nХочешь попробовать немного улучшить настроение?",
    "Такое состояние бывает чаще всего 🙂\nМожет, добавить что-то маленькое приятное в день?",
    "Стабильность — это тоже ценность 💛\nЕсть что-то, что могло бы сделать день чуть лучше?",
    "Окей 🙂\nИногда 'нормально' — это пауза перед чем-то хорошим."
]

sad_responses = [
    "Понимаю… 😔\nХочешь немного рассказать, что случилось? Я рядом.",
    "Сожалею, что тебе сейчас грустно 💛\nЭто состояние пройдёт, даже если сейчас так не кажется.",
    "Иногда такие дни просто бывают 😔\nПопробуй сделать что-то маленькое и тёплое для себя.",
    "Ты не один с этим 💛\nДаже маленький шаг может немного облегчить состояние.",
    "Грусть — это тоже важная эмоция 😔\nОна говорит, что тебе не всё равно.\nБереги себя сейчас."
]

#---ЛОГИКА БОТА---
TOKEN = "8558944640:AAEtXDvKxNG5bhnyzpIrR0TSiuO3Li876Gc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n"
        "Я здесь, чтобы помогать тебе замечать и понимать своё настроение в течение дня.\n"
        "Давай вместе сделаем его чуть лучше? 💛"
    )

@bot.message_handler(commands=["mood"])
def command_start_handler(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton("😊 Весёлое", callback_data="mood_happy")
    button2 = telebot.types.InlineKeyboardButton("😐 Нормальное", callback_data="mood_normal")
    button3 = telebot.types.InlineKeyboardButton("😢 Грустное", callback_data="mood_sad")

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    bot.send_message(
        message.chat.id,
        "Выбери своё настроение:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "mood_happy":
        text = random.choice(happy_responses)
    elif call.data == "mood_normal":
        text = random.choice(normal_responses)
    elif call.data == "mood_sad":
         text = random.choice(sad_responses)

    bot.send_message(call.message.chat.id, text)
    bot.answer_callback_query(call.id)

bot.infinity_polling()