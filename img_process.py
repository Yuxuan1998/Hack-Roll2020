import img_recog

def image_reg(image_path, update, context):
    path = image_path

    print(img_recog(path))
    context.bot.sendMessage(chat_id=update.message.chat_id, text=img_recog(path))
    return img_recog(path)
