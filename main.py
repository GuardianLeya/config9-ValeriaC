import telebot
bot = telebot.TeleBot('6967336095:AAFGHFWCL1VZcuti7dyt1Of1thcFYraFlRY')

@bot.message_handler(commands=['Start'])
def main(message):
    bot.send_message(message.chat.id, 'Надо любить жизнь больше, чем смысл жизни.', parse_mode='Markdown')

bot.infinity_polling()