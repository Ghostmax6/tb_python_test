from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define the command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            [InlineKeyboardButton("Option 1", callback_data='1')],
            [InlineKeyboardButton("Option 2", callback_data='2')],
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


#Define the callback handler for button presses
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")

#Define the main function to start the bot

def main() -> None:
    #Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater("YOUR_TOKEN")

    #Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the callback query handler
    dispatcher.add_hander(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()

    
