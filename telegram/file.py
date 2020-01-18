# prevent user from upload through files
def file_handler(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text="Please choose 'Photo or Video' to upload your photo")
