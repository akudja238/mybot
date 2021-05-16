import logging #импорт модуля записи лога работы бота

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#MessageHandler - модуль обработки сообщений (текс, картинки, аудио,в идео)
#Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

#функция ответа пользователю на команду start (приветствие)
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Приветствуем тебя! Ты вызвал команду /start')

#функция "разговора"с ботом - возврат пользовательского сообщения
def talk_to_me(update, context):
    usertext = update.message.text
    print(usertext)
    update.message.reply_text(f'Это ты сказал: {usertext}?')

#функция работы бота, основной код
def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher #переменная для упрощения кода
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал') #запись сообщения о старте бота в логфайл

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()