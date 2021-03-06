from chat_action_util import send_typing_action
from request_location import request_location
from telegram.ext import ConversationHandler


@send_typing_action
def verify_label(update, context):
    context.user_data['trash'] = context.user_data['label']
    return request_location(update, context)


@send_typing_action
def reject_label(update, context):
    update.message.reply_text(
        "Sorry I made a mistake! Please try entering text instead.")

    del context.user_data['label']
    return ConversationHandler.END
