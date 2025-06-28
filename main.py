import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я готов к игре 🎰")

@bot.message_handler(commands=["promo"])
def promo(message):
    bot.send_message(message.chat.id, "🎁 Промокод: LUCKYSPI11
Активируй его на 1Win и получи бонус!")

@bot.message_handler(commands=["games"])
def games(message):
    bot.send_message(message.chat.id, "🎮 Доступные игры:
- Aviator
- Mines
- Plinko
- Crazy Time
- Blackjack и другие")

@bot.message_handler(commands=["support"])
def support(message):
    bot.send_message(message.chat.id, "🆘 Напиши нам: @YourSupportUsername")

@bot.message_handler(commands=["faq"])
def faq(message):
    bot.send_message(message.chat.id, "❓ Частые вопросы:
1. Где вводить промокод?
— На сайте 1Win в разделе бонусов.
2. Как вывести выигрыш?
— В разделе 'Кошелек'.")

bot.infinity_polling()
