import logging
import requests
import re
from functools import wraps
from telegram import ChatAction
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

# Change your token here
TOKEN = '1043648115:AAGd5Sta2ffN06-4fFIpOuS_hJ-Do44MEos'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func

    return decorator


send_typing_action = send_action(ChatAction.TYPING)
send_upload_photo_action = send_action(ChatAction.UPLOAD_PHOTO)


# /start
@send_typing_action
def start(update, context):
    update.message.reply_text("Hello, let's start recycling today!")


# /caps arg1 arg2
@send_typing_action
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# Echo any user input
@send_typing_action
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


# /locate
# Send location
@send_typing_action
def locate(update, context):
    context.bot.send_location(
        chat_id=update.effective_chat.id, latitude=1.2966, longitude=103.7764)


# /bop
# Send a random dog picture
@send_upload_photo_action
def bop(update, context):
    url = requests.get('https://random.dog/woof.json').json()['url']
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=url)


# Any unknown commands
@send_typing_action
def unknown(update, context):
    update.message.reply_text("Sorry, I don't understand this command.")


# Error logging
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('caps', caps))
    dp.add_handler(CommandHandler('locate', locate))
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
