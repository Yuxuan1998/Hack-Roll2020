from chat_action_util import send_typing_action

# TODO
# /caps arg1 arg2
@send_typing_action
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
