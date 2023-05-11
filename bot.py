from telebot import telebot
import logging
import datetime
import time
import random
from constans import *


bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info(' БОТ ЗАПУЩЕН')


@bot.message_handler(commands=['start'])
def start(message):
    cid = message.chat.id
    bot.send_message(cid, '<b>Твой котик ищет комплимент, ожидай ⏳</b>', parse_mode='html')
    bot.send_sticker(cid, sticker='CAACAgIAAxkBAAEGHRtjTFjuHU4VHce0XAABz713gLvuPFYAAvkQAAIc-slLmjOQytI1kpIqBA')
    count = 1
    while True:
        try:
            # 1ый комплимент
            if str(datetime.datetime.now().hour) == str(HOUR1):
                bot.send_sticker(cid, random.choice(stickers))
                bot.send_message(cid, f'<b>{random.choice(complements)}</b> ' + random.choice(hearts),
                                 parse_mode='html')
                logging.info(f' Комплимент номер {count} пользователю @{message.from_user.username} доставлен!')
                count += 1
                time.sleep(3599)
            # 2ой комплимент
            elif str(datetime.datetime.now().hour) == str(HOUR2):
                bot.send_sticker(cid, random.choice(stickers))
                bot.send_message(cid, f'<b>{random.choice(complements)}</b> ' + random.choice(hearts),
                                 parse_mode='html')
                logging.info(f' Комплимент номер {count} пользователю @{message.from_user.username} доставлен!')
                count += 1
                time.sleep(3599)
        except Exception as ex:
            print(ex)
        time.sleep(600)


bot.infinity_polling(timeout=10, long_polling_timeout=5)
