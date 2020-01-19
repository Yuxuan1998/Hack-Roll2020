import img_recog
from request_location import VERIFYING_LABEL
from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_image_label(path, update, context):
    update.message.reply_text(
        "Please wait for a while, I am trying to identify your trash type")

    label = img_recog(path)
    context.user_data['label'] = label

    button1 = KeyboardButton(
        text="Yes")
    button2 = KeyboardButton(
        text="No")
    custom_keyboard = [[button1], [button2]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I have identified your trash type to be: " + label + ". Is this the correct type?", reply_markup=reply_markup)

    return VERIFYING_LABEL
