import logging
from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '6480811920:AAHEynHpGdX9Wd7ImYGtOTi74Wjn2OmVqBw'
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(rf"Hi {user.mention_html()}!", reply_markup=ForceReply(selective=True),)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


"""Start the bot."""

application = Application.builder().token(TOKEN).build()

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.run_polling(allowed_updates=Update.ALL_TYPES)
