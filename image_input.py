from chat_action_util import send_upload_photo_action
from image_util import get_image_label
from request_location import request_location, VERIFYING_LABEL

# download image
@send_upload_photo_action
def image_handler(update, context):
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.getFile(file_id)
    name = file_id + '.jpg'
    newFile.download(custom_path='downloads/'+name, timeout=None)

    return get_image_label(
        'downloads/'+name, update, context)
