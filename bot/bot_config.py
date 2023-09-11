from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


available_options = ["Get data (Difficult + Theme)", "Get data (Name of problem)", "How is it work?"]
available_themes = ["binary search", "bitmasks", "data structures", "dp", "greedy", "implementation", "bitmasks", "constructive", "algorithms", "math"]


class MakeChoice(StatesGroup):
    choosing_options = State()
    choosing_food_size = State()
    choosing_difficult = State()
    choosing_theme = State()


router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text="Select an option.", reply_markup=make_row_keyboard(available_options))
    await state.set_state(MakeChoice.choosing_options)


@router.message(MakeChoice.choosing_options, F.text.in_(available_options))
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text.lower())
    await message.answer(text="Спасибо. Теперь, пожалуйста, сложность:")
    await state.set_state(MakeChoice.choosing_difficult)


@router.message(MakeChoice.choosing_difficult)
async def difficult_chosen(message: Message):
    x = message.text
    print(x)
    await message.answer(text=f"Выбрано сложность: {x} Выберите тему:",
                         reply_markup=make_row_keyboard(available_themes)
                         )



#
# @router.message(MakeChoice.choosing_difficult, F.text.in_("*"))
# async def difficult_chosen(message: Message, state: FSMContext):
#     await state.update_data(chosen_options=message.text.lower())
#     await message.answer(text="Спасибо. Теперь, пожалуйста, тему:", reply_markup=make_row_keyboard(available_food_sizes))
#     await state.set_state(MakeChoice.choosing_difficult)
#
#
# @router.message(MakeChoice.choosing_theme, F.text.in_(available_options))
# async def theme_chosen(message: Message, state: FSMContext):
#     await state.update_data(chosen_options=message.text.lower())
#     await message.answer(text="Спасибо. Теперь, пожалуйста, тему!!!!!!!!!!!!!!!!!!!!!!!:", reply_markup=make_row_keyboard(available_food_sizes))
#     await state.set_state(MakeChoice.choosing_theme)


# @router.message(MakeChoice.choosing_difficult)
# async def food_chosen_incorrectly(message: Message):
#     await message.answer(
#         text="Я не знаю такого блюда.\n\n"
#              "Пожалуйста, выберите одно из названий из списка ниже:",
#         reply_markup=make_row_keyboard(available_options)
#     )





# @router.message(MakeChoice.choosing_options)
# async def food_chosen_incorrectly(message: Message):
#     await message.answer(
#         text="Я не знаю такого блюда.\n\n"
#              "Пожалуйста, выберите одно из названий из списка ниже:",
#         reply_markup=make_row_keyboard(available_options)
#     )







# @router.message(MakeChoice.choosing_food_size, F.text.in_(available_food_sizes))
# async def food_size_chosen(message: Message, state: FSMContext):
#     user_data = await state.get_data()
#     await message.answer(
#         text=f"Вы выбрали {message.text.lower()} порцию {user_data['chosen_food']}.\n"
#              f"Попробуйте теперь заказать напитки: /drinks",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     # Сброс состояния и сохранённых данных у пользователя
#     await state.clear()

#
# @router.message(MakeChoice.choosing_food_size)
# async def food_size_chosen_incorrectly(message: Message):
#     await message.answer(
#         text="Я не знаю такого размера порции.\n\n"
#              "Пожалуйста, выберите один из вариантов из списка ниже:",
#         reply_markup=make_row_keyboard(available_food_sizes)
#     )
#
#






async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(TOKEN)

    dp.include_router(router)
    # dp.include_router(ordering_food.router)
    # сюда импортируйте ваш собственный роутер для напитков

    await dp.start_polling(bot)


asyncio.run(main())

#
#
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token=TOKEN)
# # Диспетчер
# dp = Dispatcher()
#
#
# # @dp.message(Command("start"))
# # async def cmd_start(message: types.Message):
# #     await message.answer("Hello!")
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text="Searching. Difficult + Theme."),
#             types.KeyboardButton(text="Searching. Problem name."),
#             types.KeyboardButton(text="How is it work?.")
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Working.."
#     )
#     await message.answer("SELECT OPTIONS.", reply_markup=keyboard)
#
#
# @dp.message(F.text == "Searching. Difficult + Theme.")
# async def with_puree(message: types.Message):
#     x = message.from_user
#     await message.answer(str(x))
#
#
# @dp.message(F.text == "Searching. Problem name.")
# async def with_puree(message: types.Message):
#     x = 1 + 1
#     await message.answer(str(x))
#
#
# @dp.message(F.text == "How is it work?.")
# async def without_puree(message: types.Message):
#     await message.answer("2")
#
#
#
#
#
#
# #
# # class OrderFood(StatesGroup):
# #     choosing_food_name = State()
# #     choosing_food_size = State()
# #
# #
# # @router.message(Command("food"))
# # async def cmd_food(message: Message, state: FSMContext):
# #     await message.answer(
# #         text="Выберите блюдо:",
# #         reply_markup=make_row_keyboard(available_food_names)
# #     )
# #     # Устанавливаем пользователю состояние "выбирает название"
# #     await state.set_state(OrderFood.choosing_food_name)
#
#
#
#
# async def main():
#     await dp.start_polling(bot)
#
# asyncio.run(main())
#
#
#
#


# import logging
# from telegram import ForceReply, Update, ReplyKeyboardMarkup
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
#
# TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'
# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.reply_html(rf"Hi {user.mention_html()}!", reply_markup=ForceReply(selective=True),)
#
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Help!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#
#
# async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Searching start!")
#
# """Start the bot."""
#
# application = Application.builder().token(TOKEN).build()
#
# # on different commands - answer in Telegram
# application.add_handler(CommandHandler("start", start))
# application.add_handler(CommandHandler("help", help_command))
# application.add_handler(CommandHandler("search", search_command))
# application.run_polling(allowed_updates=Update.ALL_TYPES)
