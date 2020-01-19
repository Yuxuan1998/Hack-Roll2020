from chat_action_util import send_typing_action
from telegram.ext import ConversationHandler
from location_results import ALL_KEYWORDS
from request_location import request_location


@send_typing_action
def text_handler(update, context):
    if update.message.text not in ALL_KEYWORDS:
        update.message.reply_text(
            "Sorry I cannot recognize this item. You try again by uploading a picture")
        return ConversationHandler.END

    context.user_data['trash'] = update.message.text
    return request_location(update, context)
