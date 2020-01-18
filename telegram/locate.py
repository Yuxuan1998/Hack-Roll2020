from chat_action_util import send_typing_action
from telegram import KeyboardButton, ReplyKeyboardMarkup

# TODO:
# Request location
@send_typing_action
def request_location(update, context):
    button1 = KeyboardButton(
        text="Yes", request_location=True)
    button2 = KeyboardButton(
        text="No", request_location=False)
    custom_keyboard = [[button1], [button2]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Would you mind sharing your location with me?", reply_markup=reply_markup)


@send_typing_action
def get_location(update, context):
    // TODO
    print(update.message.location)
    update.message.reply_text(
        "We are trying to find your nearest recycling points.")
