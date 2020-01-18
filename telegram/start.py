from chat_action_util import send_typing_action

# TODO
# /start
@send_typing_action
def start(update, context):
    update.message.reply_text("Hello, let's start recycling today!")
