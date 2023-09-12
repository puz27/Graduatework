from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from src.data_base_manager import DBManager
from src.utils import config

connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'
problem_difficult = 0


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
the_end = ["/start"]


class MakeChoice(StatesGroup):
    choosing_options = State()
    choosing_difficult = State()
    choosing_theme = State()
    choosing_result = State()
    choosing_name = State()


router = Router()

# Start dialog with bot
@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text="Select an option.", reply_markup=make_row_keyboard(available_options))
    await state.set_state(MakeChoice.choosing_options)


# First step
@router.message(MakeChoice.choosing_options, F.text == "Get data (Difficult + Theme)")
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text.lower())
    await message.answer(text="Спасибо. Теперь, пожалуйста, сложность:")
    await state.set_state(MakeChoice.choosing_difficult)


@router.message(MakeChoice.choosing_options, F.text == "Get data (Name of problem)")
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text.lower())
    await message.answer(text="Спасибо. Вы берите тему для поиска...")
    await state.set_state(MakeChoice.choosing_name)


@router.message(MakeChoice.choosing_options, F.text == "How is it work?")
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text)
    await message.answer(text=f"ИНФОРМАЦИЯ", reply_markup=make_row_keyboard(the_end))


# Second step for Get data (Difficult + Theme)
@router.message(MakeChoice.choosing_difficult)
async def difficult_chosen(message: Message, state: FSMContext):
    global problem_difficult
    problem_difficult = int(message.text)
    await message.answer(text=f"Выбрано сложность: {problem_difficult} Выберите тему:", reply_markup=make_row_keyboard(available_themes))
    await state.set_state(MakeChoice.choosing_result)


@router.message(MakeChoice.choosing_result, F.text.in_(available_themes))
async def result_chosen(message: Message):
    global problem_difficult
    problems_lists = []
    problem_theme = message.text

    search_problem = data_base.get_problems("problems", problem_difficult, problem_theme, 10)
    for problem in search_problem:
        problems_lists.append(problem)
    print(problems_lists)
    await message.answer(text=f"Theme: {problem_theme} Problems: {problems_lists}", reply_markup=make_row_keyboard(the_end))


# Second step for Get data (Name of problem)
@router.message(MakeChoice.choosing_name)
async def result_chosen(message: Message):
    problems_lists = []
    problem_name = message.text

    search_problem = data_base.get_problem_by_name("problems", problem_name, 10)
    for problem in search_problem:
        problems_lists.append(problem)
    print(problems_lists)
    await message.answer(text=f" Problems: {problems_lists}", reply_markup=make_row_keyboard(the_end))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(TOKEN)

    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
