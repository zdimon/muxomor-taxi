import sys
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Bot
from django.core.management.base import BaseCommand, CommandError

from taxi.models import UserProfile, SocialAuth

from dj_prj.settings import TELEGRAMM_KEY

'''

t.me/zdimon77_bot

'''
bot = Bot(token=TELEGRAMM_KEY)

def start(update: Updater, context: CallbackContext):
    print("Start command!")
    username = update.message.from_user['username']
    room_id = update.message.chat_id 
    try:
        user = UserProfile.objects.get(username=username)
        bot.send_message(room_id, 'Добро пожаловать %s' % user.publicname)
    except:

        bot.send_message(room_id, 'Регистрация')
        user = UserProfile()
        user.username = update.message.from_user['username']
        user.publicname = update.message.from_user['first_name']
        user.is_active = True
        user.set_password('123')
        user.save()
        s = SocialAuth()
        s.user = user
        s.type = 'telegram'
        s.secret = room_id
        s.save()
        message = 'Вы успешно зарегистрированы логин: %s пароль %s ' % (user.username, '123')

class Command(BaseCommand):


    def handle(self, *args, **options):
        print('Start telegram bot .... %s' % TELEGRAMM_KEY)
        print('t.me/zdimon77_bot')
        

        

        start_handler = CommandHandler('start', start)

        updater = Updater(token=TELEGRAMM_KEY, use_context=True)
        updater.dispatcher.add_handler(start_handler)
        updater.start_polling()
