#!/usr/bin/env python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bop import bop
from caps import caps
from locate import locate, request_location, get_location
from echo import echo
from start import start
from unknown import unknown

# Change your token here
TOKEN = '1043648115:AAGd5Sta2ffN06-4fFIpOuS_hJ-Do44MEos'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Error logging
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('caps', caps))
    dp.add_handler(CommandHandler('locate', request_location))
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(MessageHandler(Filters.location, get_location))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
