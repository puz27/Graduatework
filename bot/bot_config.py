import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Dispatcher, types
from aiogram.filters.state import State, StatesGroup
TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="GO TO SEARCH."),
            types.KeyboardButton(text="HOW IT IS WORK.")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="SELECT OPTIO"
    )
    await message.answer("SELECT OPTIONS.", reply_markup=keyboard)


@dp.message(F.text == "GO TO SEARCH.")
async def with_puree(message: types.Message):
    x = 1 + 1
    await message.reply(str(x))


@dp.message(F.text == "HOW IT IS WORK.")
async def without_puree(message: types.Message):
    await message.reply("2")



async def main():
    await dp.start_polling(bot)

asyncio.run(main())






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
