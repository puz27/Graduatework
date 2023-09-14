from aiogram import Router, F,  Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from src.data_base_manager import DBManager
from src.utils import config

connection_params = config(section="postgresql")
TOKEN = config(section="token")["id"]
data_base = DBManager(connection_params, "codeforces_base")
# TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'
# global for work with difficult of problem
problem_difficult = 0


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Create keyboard
    :param items: list of buttons
    :return: prepared keyboard
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


available_options = ["Get data (Difficult + Theme)", "Get data (Name of problem)", "How is it work?"]
available_themes = ["binary search", "bitmasks", "data structures", "dp", "greedy", "implementation",
                    "bitmasks", "constructive", "algorithms", "math", "brute force", "graphs", "dsu",
                    "geometry", "trees", "combinatorics", "games"]
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
    await message.answer(text="Choose the difficulty of the problem.")
    await state.set_state(MakeChoice.choosing_difficult)


@router.message(MakeChoice.choosing_options, F.text == "Get data (Name of problem)")
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text.lower())
    await message.answer(text="Choose the theme of the problem.")
    await state.set_state(MakeChoice.choosing_name)


@router.message(MakeChoice.choosing_options, F.text == "How is it work?")
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text)
    await message.answer(text=f"ИНФОРМАЦИЯ", reply_markup=make_row_keyboard(the_end))


@router.message(MakeChoice.choosing_options)
async def options_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text)
    await message.answer(text=f"Make your choice again!", reply_markup=make_row_keyboard(available_options))


# Second step for Get data (Difficult + Theme)
@router.message(MakeChoice.choosing_difficult)
async def difficult_chosen(message: Message, state: FSMContext):
    global problem_difficult
    problem_difficult = message.text
    if problem_difficult.isdigit():
        await message.answer(text=f"Difficulty of the problem: {int(problem_difficult)}\nChoose the theme of the problem:", reply_markup=make_row_keyboard(available_themes))
        await state.set_state(MakeChoice.choosing_result)
    else:
        await message.answer(text="Data entered incorrectly. Choose the difficulty of the problem again.",)
        await state.set_state(MakeChoice.choosing_difficult)


@router.message(MakeChoice.choosing_result, F.text.in_(available_themes))
async def result_chosen(message: Message):
    global problem_difficult
    problem_theme = message.text

    search_problem = data_base.get_problems("problems", problem_difficult, problem_theme, 10)
    converted_list = []
    for problem in search_problem:
        converted_list.append(problem)
        converted_list.append('\n')

    problems_string = ''.join([str(problem) for problem in converted_list])
    if problems_string:
        await message.answer(text=f"Founded information:\n {problems_string}", reply_markup=make_row_keyboard(the_end))
    else:
        await message.answer(text=f"No data.", reply_markup=make_row_keyboard(the_end))


@router.message(MakeChoice.choosing_result)
async def result_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_options=message.text)
    await message.answer(text=f"Make your choice again!", reply_markup=make_row_keyboard(available_themes))


# Second step for Get data (Name of problem)
@router.message(MakeChoice.choosing_name)
async def result_chosen(message: Message):
    problem_name = message.text

    search_problem = data_base.get_problem_by_name("problems", problem_name, 10)
    converted_list = []
    for problem in search_problem:
        converted_list.append(problem)
        converted_list.append('\n')
    problems_string = ''.join([str(problem) for problem in converted_list])
    if problems_string:
        await message.answer(text=f"Founded information:\n {problems_string}", reply_markup=make_row_keyboard(the_end))
    else:
        await message.answer(text=f"No data.", reply_markup=make_row_keyboard(the_end))


async def main_bot():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)
