import telebot
from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage

TOKEN = "8707053530:AAH_iYjdeEglbjpfgLVFgun2tt1887qkec8"

bot = telebot.TeleBot(
    TOKEN,
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True
)

registrations_dictionary = {}

class RegistrationStates(StatesGroup):
    main_menu_button_press = State()
    input_team_title = State()
    input_team_count_members = State()
    input_team_chosen_task = State()
    check_team_data = State()

@bot.message_handler(commands=["start"])
def command_start_handler(message: types.Message):

    output_text = "Приветствуем вас на регистрации Хакатона!\nВыберите нужное действие:"

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_add_team = telebot.types.InlineKeyboardButton(
        "Добавить новую команду", callback_data="button_add_team"
    )
    button_show_all_teams = telebot.types.InlineKeyboardButton(
        "Просмотреть все добавленные команды", callback_data="button_show_all_teams"
    )

    inline_reply_keyboard.add(button_add_team)
    inline_reply_keyboard.add(button_show_all_teams)

    bot.send_message(
        message.chat.id,
        output_text,
        reply_markup=inline_reply_keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "button_add_team")
def callback_button_add_team_handler(call, state: StateContext):
    bot.answer_callback_query(call.id)

    output_text = (
        "Пожалуйста введи название вашей команды. (от 1 до 30 символов длинной)"
    )

    state.set(RegistrationStates.input_team_title)

    bot.send_message(call.message.chat.id, output_text)

@bot.message_handler(state=RegistrationStates.input_team_title)
def message_text_team_title_handler(message: types.Message, state: StateContext):
    title = message.text.strip()

    if len(title) > 30:
        output_text = "Ошибка. Длина названия команды должна быть от 1 до 30 символов\nВведите название ещё раз"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(title=title)
    state.set(RegistrationStates.input_team_count_members)
    bot.send_message(
        message.chat.id,
        "Введите количество участников вашей команде( от 1-го до 4-х человек): ",
    )

@bot.message_handler(state=RegistrationStates.input_team_count_members)
def message_text_team_title_handler(message: types.Message, state: StateContext):
    count_members_as_text = message.text.strip()

    if count_members_as_text.isdigit() == False:
        output_text = "Ошибка. Вы ввели НЕ число. Попробуйте ещё раз:"
        bot.send_message(message.chat.id, output_text)
        return

    count_members = int(count_members_as_text)

    if count_members < 1 or count_members > 4:
        output_text = "Ошибка. Количество участников в команде от 1-х до 4-х"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(count_members=count_members)
    state.set(RegistrationStates.input_team_chosen_task)

    bot.send_message(
        message.chat.id,
        "Заглушка заданий ",
    )

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()