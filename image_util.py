import img_recog


def get_image_label(path, update, context):
    print(img_recog(path))
    context.bot.sendMessage(
        chat_id=update.message.chat_id, text=img_recog(path))
    return img_recog(path)
