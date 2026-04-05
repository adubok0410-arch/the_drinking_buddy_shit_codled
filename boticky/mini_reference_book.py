import telebot
import telebot.types

TOKEN = "8611828073:AAHG0-BubhmYWhYkc6hvenpEurgCWQY4UdM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(
        message.chat.id,
        "👨‍💻 Добро пожаловать!\n"
        "Я — твой помощник по Python 🐍\n"
        "Могу подсказать синтаксис, объяснить темы и показать примеры."
    )

@bot.message_handler(commands=["help_python"])
def command_start_handler(message: telebot.types.Message):
    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton("Переменные", callback_data="reference_variables")
    button2 = telebot.types.InlineKeyboardButton("Условия", callback_data="reference_conditions")
    button3 = telebot.types.InlineKeyboardButton("Циклы", callback_data="reference_cycles")

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    bot.send_message(
        message.chat.id,
        "Выбери тему:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "reference_variables":
        bot.send_message(call.message.chat.id,
            "📌 Переменные — это контейнеры для хранения данных.\n\n"
            "Пример:\n"
            "x = 10\n"
            "name = 'Leha'\n\n"
            "Документация:\n"
            "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator"
        )
    elif call.data == "reference_conditions":
        bot.send_message(call.message.chat.id,
            "📌 Условия позволяют выполнять код при выполнении условия.\n\n"
            "Пример:\n"
            "x = 10\n"
            "if x > 5:\n"
            "    print('Больше 5')\n\n"
            "Документация:\n"
            "https://docs.python.org/3/tutorial/controlflow.html#if-statements"
        )
    elif call.data == "reference_cycles":
        bot.send_message(call.message.chat.id,
            "📌 Циклы позволяют повторять действия.\n\n"
            "Пример:\n"
            "for i in range(5):\n"
            "    print(i)\n\n"
            "Документация:\n"
            "https://docs.python.org/3/tutorial/controlflow.html#for-statements"
        )

    bot.answer_callback_query(call.id)

bot.infinity_polling()