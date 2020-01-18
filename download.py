from chat_action_util import send_upload_photo_action
from img_process import image_reg
from locate import request_location

# download image
@send_upload_photo_action
def image_handler(update, context):
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.getFile(file_id)
    name = file_id + '.jpg'
    newFile.download(custom_path='downloads/'+name, timeout=None)
    context.bot.sendMessage(chat_id=update.message.chat_id, text="wait for processing")

    context.user_data['trash'] = image_reg('downloads/'+name, update, context)
    request_location(update, context)

