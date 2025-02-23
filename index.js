require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });

bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    
    const options = {
        reply_markup: {
            inline_keyboard: [
                [{ text: "Button 1", callback_data: "button1" }],
                [{ text: "Button 2", callback_data: "button2" }]
            ]
        }
    };

    bot.sendMessage(chatId, "Choose an option:", options);
});

// Handle button clicks
bot.on("callback_query", (callbackQuery) => {
    const message = callbackQuery.message;
    const data = callbackQuery.data;

    let responseText = "You clicked: " + (data === "button1" ? "Button 1" : "Button 2");

    bot.sendMessage(message.chat.id, responseText);
    bot.answerCallbackQuery(callbackQuery.id);
});

console.log("Bot is running...");
