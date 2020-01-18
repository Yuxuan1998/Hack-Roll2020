from chat_action_util import send_typing_action

# Any unknown commands
@send_typing_action
def unknown(update, context):
    update.message.reply_text("Sorry, I don't understand this command.")
