from chat_action_util import send_upload_photo_action
import requests

# TODO
# /bop
# Send a random dog picture
@send_upload_photo_action
def bop(update, context):
    url = requests.get('https://random.dog/woof.json').json()['url']
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=url)
