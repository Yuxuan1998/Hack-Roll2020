from chat_action_util import send_typing_action
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from location_results import ALL_KEYWORDS

REQUESTING_LOCATION = 1

# TODO:
# Request location
@send_typing_action
def request_location(update, context):
    if update.message.text not in ALL_KEYWORDS:
        update.message.reply_text(
            "Sorry I cannot recognize this item. You try again by uploading a picture")
        return ConversationHandler.END
        
    context.user_data['trash'] = update.message.text

    button1 = KeyboardButton(
        text="Send location", request_location=True)
    button2 = KeyboardButton(
        text="No", request_location=False)
    custom_keyboard = [[button1], [button2]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Would you mind sharing your location with me?", reply_markup=reply_markup)
    return REQUESTING_LOCATION