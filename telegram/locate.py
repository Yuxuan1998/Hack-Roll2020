from chat_action_util import send_typing_action

# /locate
# Send location
@send_typing_action
def locate(update, context):
    context.bot.send_location(
        chat_id=update.effective_chat.id, latitude=1.2966, longitude=103.7764)
