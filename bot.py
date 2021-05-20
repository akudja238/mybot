import logging #импорт модуля записи лога работы бота

import ephem #импорт астрономического модуля

import datetime #импорт модуля даты и времени

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#MessageHandler - модуль обработки сообщений (текст, картинки, аудио, видео)
#Filters

import settings

log_format = '%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename='bot.log', encoding='utf-8', mode='a+')], format=log_format, datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

#функция ответа пользователю на команду /start (приветствие)
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Приветствуем тебя! Ты вызвал команду /start')

#функция ответа пользователю на команду /planet, запрос планеты от пользователя и выдача созвездия
def ask_planet(update, context):
    print('Вызван /planet')
    text = update.message.text
    if len(text.split()) < 3:
        try:
            text = text.split()[1]
            print(text) #для отображения в консоли
            current_date = datetime.date.today()
            current_date = str(current_date).replace('-','/')
            try:
                planet = getattr(ephem, text, 'Увы, такая планета еще не сформировалась, подождём немного.')
                print(planet) #для отображения в консоли
                pl = planet(current_date)
                print(pl) #для отображения в консоли
                constellation = ephem.constellation(pl)
                update.message.reply_text(f'Сегодня эта планета в созвездии: {constellation}?')
                print(constellation) #для отображения в консоли
            except:
                update.message.reply_text(planet)
        except IndexError:
            update.message.reply_text('Введите название планеты по примеру: /planet Mars')
    else:
        update.message.reply_text('Имя планеты должно быть из одного слова!\nВведите название планеты по примеру: /planet Mars')
    
    #print(len(text))
    #update.message.reply_text(f'Вы ввели планету {text}?')
   

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
    dp.add_handler(CommandHandler('planet', ask_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
 
    logging.info('Бот стартовал') #запись сообщения о старте бота в логфайл
    logging.Filter.

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()