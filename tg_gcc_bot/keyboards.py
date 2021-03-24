from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData


__author__ = "Ammosov Daniil"


HelloMsgCallbackData = CallbackData("hello", "opinion")

SendContact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎', request_contact=True)
)


def create_hello_msg_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
            InlineKeyboardButton("Команда 1", callback_data=HelloMsgCallbackData.new(opinion="FAQ")),
            InlineKeyboardButton("Команда 2", callback_data=HelloMsgCallbackData.new(opinion="Расчёт")),
            InlineKeyboardButton("Команда 3", callback_data=HelloMsgCallbackData.new(opinion="Выбор")),
            InlineKeyboardButton("Команда 4", callback_data=HelloMsgCallbackData.new(opinion="Кейсы")),
            InlineKeyboardButton("Команда 5", callback_data=HelloMsgCallbackData.new(opinion="Партнёрство")),
            InlineKeyboardButton("Команда 6", callback_data=HelloMsgCallbackData.new(opinion="Контакты"))
    )

    return keyboard


Marketplaces = CallbackData("marketplaces", "market")


def create_marketplaces_msg_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    for i in range(1, 7):
        keyboard.add(InlineKeyboardButton(f"Market {i}", callback_data=Marketplaces.new(market=f"{i}")))

    return keyboard
