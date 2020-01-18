#!/usr/bin/env python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, PicklePersistence
from locate import request_location, REQUESTING_LOCATION
from location_results import get_results_by_location, get_all_results
from start import start
from unknown import unknown
from download import image_handler

# Change your token here
TOKEN = '860867777:AAH6Hj0-op0CFxc2aa4HpwqmxOwQLfIwVQA'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# TODO
def done(update, context):
    del context.user_data['trash']
    update.message.reply_text("Aborted!")
    return ConversationHandler.END


# Error logging
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    pp = PicklePersistence(filename='data')
    updater = Updater(TOKEN, persistence=pp, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the state REQUESTING_LOCATION
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, request_location),
                      MessageHandler(Filters.photo, image_handler)],

        states={
            REQUESTING_LOCATION: [MessageHandler(Filters.location, get_results_by_location),
                                  MessageHandler(Filters.regex(
                                      '^No$'), get_all_results)
                                  ],
        },

        fallbacks=[CommandHandler('cancel', done)],
        name="trash",
        persistent=True
    )

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(conv_handler)
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
