from chat_action_util import send_typing_action

E_WASTE_RESPONSE = "Most electronic products; must be able to fit through the 470mm x 120mm slot of the bins. To reduce the risk of short-circuits and creation of fire hazard, please tape the ends or wires of rechargeable batteries before recycling them."
E_WASTE_KEYWORDS = ["phone", "keyboard", "mouse", "battery", "batteries"]
E_WASTE_BIZ = (1.292533, 103.774135)
E_WASTE_SOC = (1.297001, 103.776981)
E_WASTE_NUH = (1.296736, 103.782675)
E_WASTE_LOCATION = [E_WASTE_BIZ, E_WASTE_SOC, E_WASTE_NUH]
# Echo any user input
# /KEYWORD
@send_typing_action
def location_text_input(update, context):
    if update.message.text in E_WASTE_KEYWORDS:
        context.bot.send_location(
            chat_id=update.effective_chat.id, latitude=E_WASTE_BIZ[0], longitude=E_WASTE_BIZ[1])
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=E_WASTE_RESPONSE)


