from chat_action_util import send_typing_action

# Echo any user input
@send_typing_action
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)
