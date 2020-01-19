from chat_action_util import send_typing_action
from telegram import KeyboardButton, ReplyKeyboardMarkup

REQUESTING_LOCATION = 1


# Request location
def request_location(update, context):
    button1 = KeyboardButton(
        text="Send location", request_location=True)
    button2 = KeyboardButton(
        text="No", request_location=False)
    custom_keyboard = [[button1], [button2]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Would you mind sharing your location with me?", reply_markup=reply_markup)
    return REQUESTING_LOCATION
