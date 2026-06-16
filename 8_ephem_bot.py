"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PLANETS = {
    'Mercury': ephem.Mercury(),
    'Venus': ephem.Venus(),
    'Mars': ephem.Mars(),
    'Jupiter': ephem.Jupiter(),
    'Saturn': ephem.Saturn(),
    'Uranus': ephem.Uranus(),
    'Neptune': ephem.Neptune()
}
# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def get_constellation(update, context):
    user_text = update.message.text.split()
    try: 
        user_planet = user_text[1].capitalize()
    except IndexError:
        text = 'Where`s no planet to looking for or no such planet on my sky.'
        user_planet = ''

    if PLANETS.get(user_planet):
        planet = PLANETS.get(user_planet)
        planet.compute()
        planet_data = ephem.constellation(planet)
        text = f'The {user_planet} in {planet_data[1]} constellation.'
    elif user_planet:
        text = 'No such planet in my sky.'
    update.message.reply_text(text)
    

def main():
    mybot = Updater(
        "КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather",
        request_kwargs=PROXY,
        use_context=True,
    )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', get_constellation))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
