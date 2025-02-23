import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = "8161726582:AAHqnPDmFnapvEDHt18PWbC8AziL-8LfAkg"

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command
from telegram import ReplyKeyboardMarkup

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [["Button 1", "Button 2"], ["Button 3"]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

#     await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data="option1")],
        [InlineKeyboardButton("Option 2", callback_data="option2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

# Button click handler
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "option1":
        await query.edit_message_text(text="You selected Option 1!")
    elif query.data == "option2":
        await query.edit_message_text(text="You selected Option 2!")

# Main function
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
