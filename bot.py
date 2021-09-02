#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
#   Created by Vakhlakov Alexandr    #


import telebot
from telebot import apihelper
from telebot import types
import time
from config import *
from tasks import MBJira
from tasks import send_to_telegram

bot = telebot.TeleBot(tg_token)

apihelper.proxy = {
    # "USERNAME:PASSWORD@" is optional, if you need authentication:
    'https': tg_proxy,
}

jira = MBJira()
m = jira.get_issues()
for new_issue in m:
    msg = tg_messages_2.format(
        key=new_issue.key,
        issue_url=jira.get_issue_url(new_issue)
    )

    send_to_telegram(msg)

@bot.message_handler(content_types=[tg_messages_1])
def task(message):
    bot.send_message(message.chat.id, tg_messages_1)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton(text='Назначить мне.', callback_data='yes')
    cancel_button = types.InlineKeyboardButton(text='Оставить.', callback_data='cancel')
    keyboard.add(yes_button, cancel_button)
    bot.send_message(message.chat.id, 'Кто хочет взять задачу себе?', reply_markup=keyboard)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)
