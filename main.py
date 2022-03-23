import os

import schedule
import telebot
from threading import Thread
from time import sleep

TOKEN = "5181579455:AAGKsHIFRPqaUM2klJXU7VUHtCOad8UbsR8"

bot = telebot.TeleBot(TOKEN)
some_id = -623268281  # This is our chat id.


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def function_to_run():
    bot.send_sticker(some_id, "./2026612102/webp")
    return bot.send_message(some_id, "ПО ДОМАМ ХУТКО БЛЯТЬ")



# Create the job in schedule.
schedule.every().second.do(function_to_run)

# Spin up a thread to run the schedule check so it doesn't block your bot.
# This will take the function schedule_checker which will check every second
# to see if the scheduled job needs to be ran.
Thread(target=schedule_checker).start()

bot.infinity_polling()
