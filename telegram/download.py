from chat_action_util import send_upload_photo_action

# download image
@send_upload_photo_action
def image_handler(update, context):
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.getFile(file_id)
    name = file_id + '.jpg'
    newFile.download(name)
    context.bot.sendMessage(chat_id=update.message.chat_id, text="download successfully")
