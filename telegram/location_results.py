from chat_action_util import send_typing_action
import math
from telegram.ext import ConversationHandler

E_WASTE_KEYWORDS = ["phone", "keyboard", "mouse", "battery", "batteries"]
E_WASTE_BIZ = (1.292533, 103.774135, "There is a recycle point near NUS Business School")
E_WASTE_SOC = (1.297001, 103.776981, "There is a recycle point near School of Computing")
E_WASTE_NUH = (1.296736, 103.782675, "There is a recycle point near NUH")
E_WASTE_LOCATION = [E_WASTE_BIZ, E_WASTE_SOC, E_WASTE_NUH]


PEN_KEYWORDS = ["pen", "pens"]
PEN_CLB = (1.296489, 103.772998, "There is a recycle point near Central Library")
PEN_VENTUS = (1.296129, 103.770279, "There is a recycle point near NUS Ventus")
PEN_LOCATION = [PEN_CLB, PEN_VENTUS]

CLOTHES_KEYWORDS = ["clothes", "shoes", "bags"]
CLOTHES_LOCATION = [(1.291175, 103.780761, "There is a recycle point near PGPR")]


HUMAN = (1.297030, 103.773765)

ALL_KEYWORDS =  E_WASTE_KEYWORDS + PEN_KEYWORDS + CLOTHES_KEYWORDS

ALL_LOCATION = [E_WASTE_BIZ, E_WASTE_SOC, E_WASTE_NUH,
                PEN_CLB, PEN_VENTUS, CLOTHES_LOCATION]

@send_typing_action
def get_all_results(update, context):
    user_input = context.user_data['trash']
    if user_input in E_WASTE_KEYWORDS:
        for location in E_WASTE_LOCATION:
            update.message.reply_text(location[2])
            context.bot.send_location(
                chat_id=update.effective_chat.id, latitude=location[0], longitude=location[1])

    if user_input in PEN_KEYWORDS:
        for location in PEN_LOCATION:
            update.message.reply_text(location[2])
            context.bot.send_location(
                chat_id=update.effective_chat.id, latitude=location[0], longitude=location[1])

    if user_input in CLOTHES_KEYWORDS:
        for location in CLOTHES_LOCATION:
            update.message.reply_text(location[2])
            context.bot.send_location(
                chat_id=update.effective_chat.id, latitude=location[0], longitude=location[1])

    return ConversationHandler.END


def get_results_by_location(update, context):
    update.message.reply_text(
        "You can recycle " + context.user_data['trash'] + " here")
    # target = (update.message.location.longitude,
    #           update.message.location.latitude)
    target = update.message.location
    location_tuple = (0, 0)

    if context.user_data['trash'] in E_WASTE_KEYWORDS:
        location_tuple = choose_shortest_location(target, E_WASTE_LOCATION)

    if context.user_data['trash'] in PEN_KEYWORDS:
        location_tuple = choose_shortest_location(target, PEN_LOCATION)

    if context.user_data['trash'] in CLOTHES_KEYWORDS:
        location_tuple = choose_shortest_location(target, CLOTHES_LOCATION)

    update.message.reply_text(location_tuple[2])
    context.bot.send_location(
        chat_id=update.effective_chat.id, latitude=location_tuple[0], longitude=location_tuple[1])

    return ConversationHandler.END


def choose_shortest_location(target, locations):
    distance = float('inf')
    location_tuple = (target.longitude, target.latitude)
    print(locations)
    for location in locations:
        print(location_tuple[0])
        print(location)
        dist = math.sqrt((location_tuple[0] - location[0]) **
                         2 + (location_tuple[1] - location[1]) ** 2)
        if dist <= distance:
            result = location
            distance = dist
    return result
