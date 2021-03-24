import typing

from aiogram import Bot, Dispatcher, types

from .keyboards import *
from .logger import create_logger

__author__ = "Ammosov Daniil"


# ======================== MAIN OBJECTS ===============================
API_TOKEN = "TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
bot.logger = create_logger()


PDF_DOC = ""
FAQ_INFO =  """
Q: Документы, которые нужны для входа на площадку?
A: Наличие юр.лица, сертификаты, декларации и другое

Q: Можно ли выйти на площадку, как самозанятый? 
A: Пока только на WB

Q: Можно ли выйти на площадку, как физ.лицо?
A: Нет, понадобится либо наличие юр.лица (ИП/ООО), либо оформленная самозанятость, но только для WB

Q: Какие комиссии площадок по разным категориям товаров?
A: WB, Ozon, Lamoda, Goods, Яндекс.Маркет

Q: Плата за доставку до клиента
A: сколько и как

Q: опустимые размеры товаров для мп (маркетплейс), размеры кгт (крупногабаритный товар);
A: Нет данных

Q: По каким схемам работают мп?
A: Ozon - FBO И FBS; WB - пока отгрузка на их склад; Яндекс.Маркет - FBY, FBY+, FBS

Q: Где находятся склады у мп, если доставка со склада площадки?
A: Нет данных

Q: Нужны ли сертификаты соответствия качества на товары для выхода на мп?
A: Нет данных

Q: На какой мп дешевле и быстрее зайти сначала?
A: По срокам выхода - на WB, мы рекомендуем ее, как первую площадку, она же генерирует 80% продаж наших клиентов

Q: Как можно доставить свой товар на склад мп?
A: С помощью транспортной компании, своей логистики

Q: Делаем ли мы упаковку, маркировку товара?
A: Делаем за отдельную плату, логистический комплекс “Мул” находится в г.Подольск

Q: На какой срок рассчитаны наши пакеты услуг?
A: На один календарный год

Q: Какие способы оплаты пакетов существуют?
A: Как правило, 100% предоплата пакета + %% за сопровождение и продвижение в конце месяца работы. В индивидуальном порядке можем обсудить иные способы оплаты пакета

Q: Сколько вы работаете с мп?
A: С российскими площадками работаем более двух лет. За это время накопилось много интересных и сложных кейсов наших клиентов

Q: Для чего нужна онлайн-встреча с менеджером, на которую вы приглашаете после обзвона?
A: На ней анализируем ваши товар и нишу, определяем финансовые гарантии и тайм-лайн проекта

Q: Я хочу сам упаковывать и маркировать товар. Что для этого потребуется? 
A: Термопринтер для печати маркировок, упаковка по правилам мп

Q: Почему у вас нет пакетов только с техническим заведением? Мне не нужно продвижение 
A: Мы настроены на долгосрочное сотрудничество с партнерами. К тому же, технический выход на площадку не равно продажи. Наша главная цель ─ увеличение оборота до 1 млн рублей и выше.
Без должного продвижения продажи будут случайными и органическими, но не системными

Q: Сколько товаров рекомендуется к первой поставке?
A: Первую партию делаем пробную, от 50 до 300 товаров в зависимости от категории

Q: Что делать с ценами на мп? 
A: Как правило, мы закладываем комиссию площадки и плату за логистику до клиента в цену. наши менеджеры помогут с ценообразованием и подскажут, как правильнее будет сделать

Q: Есть ли у вас обучение, хочу все делать сам?
A: Обучение есть, но опция становится доступной только после приобретения одного из пакетов услуг"""

RASCHET =   '<a href="https://topmarketplace.ru/tmpcourses#rec183967632">Расчитать чек</a>'
CONTACTS =  "Вы можете написать нам:\nРыжий +7 952 336 34 10"


# ========================= MESSAGE HANDLING ==============================
@dp.message_handler(commands=["start"])
async def hello_msg(message: types.Message):
    user: User = message.from_user

    # TODO задать стейт
    answer = "Здравствуйте\n" \
             "Мы компания 'TopMarketPlace' поможем вам разобраться с маркетплейсами\n" \
             "Нажмите /instruction чтобы узнать больше"
    keyboard = create_hello_msg_kb()
    return await message.reply(answer, reply_markup=keyboard)


@dp.message_handler(commands=["instruction"])
async def hello_msg(message: types.Message):
    user: User = message.from_user

    # TODO задать стейт
    answer = "Команда 1 - FAQ\n" \
             "Команда 2 - Расчёт\n" \
             "Команда 3 - Выбор\n" \
             "Команда 4 - Кейсы\n" \
             "Команда 5 - Партнёрство\n" \
             "Команда 6 - Контакты\n"

    keyboard = create_hello_msg_kb()
    return await message.reply(answer, reply_markup=keyboard)


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["FAQ"]))
async def show_faq(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()
    answer = f"{FAQ_INFO}"
    messages = []
    if len(answer) > 4096:
        lines = answer.split("\n\n")
        message = ""
        for line in lines:
            message += line
            if len(message) > 4096:
                message -= line
                messages.append(message)
                message = line

    else:
        messages.append(answer)

    for message in messages:
        await callback.message.answer(message)

    return


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["Расчёт"]))
async def show_chek(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()

    answer = RASCHET
    return await callback.message.answer(answer, parse_mode="HTML")


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["Выбор"]))
async def show_marketplaces(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()

    answer = "Пожалуйста, выберите интересующую вас торговую площадку"
    keyboard = create_marketplaces_msg_kb()
    return await callback.message.answer(answer, reply_markup=keyboard)


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["Кейсы"]))
async def show_cases(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()

    return await bot.send_document(callback.message.chat.id,
                                   caption="Ознакомьтесь с нашей компанией",
                                   document=types.InputFile("/home/user/bot/data/company.pdf"))


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["Партнёрство"]))
async def show_partners(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()

    answer = f"{CONTACTS}"
    return await callback.message.answer(answer)


# Flow to marketplace
@dp.callback_query_handler(Marketplaces.filter(market=["1"]))
@dp.callback_query_handler(Marketplaces.filter(market=["2"]))
@dp.callback_query_handler(Marketplaces.filter(market=["3"]))
@dp.callback_query_handler(Marketplaces.filter(market=["4"]))
@dp.callback_query_handler(Marketplaces.filter(market=["5"]))
@dp.callback_query_handler(Marketplaces.filter(market=["6"]))
async def show_partners(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    answer = f"Вы выбрали {callback_data['market']}"
    return await callback.message.answer(answer)


# ========================= HANDLING CALLBACKS ========================
# Flow to marketplace
@dp.callback_query_handler(HelloMsgCallbackData.filter(opinion=["Контакты"]))
async def show_contacts(callback: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    """
    Method for accept new user callback by admins
    """
    await callback.answer()

    return await callback.message.reply("Отправьте свой контакт", reply_markup=SendContact)
    # answer = f"{CONTACTS}"
    # return await callback.message.answer(answer)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def save_contact(message: types.Message):
    print(message.contact)
    bot.logger.info(f"New contact: {str(message.contact.full_name)} {str(message.contact.phone_number)}")
    return await message.reply(f"Спасибо, {message.contact.full_name}, мы свяжемся с вами как можно быстрее", reply_markup=ReplyKeyboardRemove())


@dp.errors_handler(exception=Exception)
def error(update: types.Update, error):
    bot.logger.exception(f"Catch error: {str(error)}")
    return True
