from chat_action_util import send_upload_photo_action
from image_util import get_image_label
from request_location import request_location, VERIFYING_LABEL

# download image
@send_upload_photo_action
def file_handler(update, context):
    file_id = update.message.document.file_id
    newFile = context.bot.getFile(file_id)
    if update.message.document.mime_type != "image/jpeg":
        context.bot.sendMessage(
            chat_id=update.message.chat_id, text="We only allow jpg format!")
    name = file_id + '.jpg'
    newFile.download(custom_path='downloads/'+name, timeout=None)

    return get_image_label(
        'downloads/'+name, update, context)
