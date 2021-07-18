""" Userbot module for having some fun with people. """
import random

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SurCat"
SURID = bot.uid

# ================= CONSTANT =================


SLAP_TEMPLATES = [
    "`Dear {victim} 💞 സ്നേഹിക്കാൻ ഒരുപാട് കാരണങ്ങൾ ഉണ്ടായേക്കും.. എന്നാൽ നിന്നിൽ കാരണങ്ങളല്ല 😍 മറിച്ചു ഞാൻ നിന്നിലേക്ക് പകർത്തു നൽകിയ എന്റെ സ്നേഹോപകാരമാണ് എന്റെ പ്രണയം എന്ന് 💘 {user1}`",
    "`Dear {victim} 💗തിരിച്ചറിയാൻ പറ്റാത്ത ഒരു രാത്രിയും നമുക്കു നേരെ തിരിയില്ല💘💓 ഏതൊരു പാതിരാത്രിയിലും നിന്റെ നിഴൽ കണ്ടാൽ  ഞാൻ പറഞ്ഞേക്കും അത് എന്റെ പ്രാണസഖിയാണെന്ന്💝 എന്ന് {user1}`",
    "`Dear {victim} ❤️പ്രണയ സൗരഭ്യം നിറഞ്ഞ  ✨എന്റെ മനസ്സിലെ സ്ഥാനം✨  നിനക്ക് വേണ്ടി ഒഴിച്ചിട്ടിരിക്കുന്നു..💘💘💘 എന്ന് {user1}`",
    "`Dear {victim} 💗ആരും എന്നെ തേടി വന്നില്ലെങ്കിലും 😍😍 നിയെങ്കിലും എന്റെ മനസ്സിലേക്ക് ഓടിച്ചാടി💝 വരുമെന്ന് എനിക്കറിയാം💞💞 എന്ന് {user1}`",
    "`Dear {victim} 🧡സായാഹ്ന ചിന്തകൾ ചിലപ്പോ എന്റെ പ്രണയം💕 നിനക്കു വേണ്ടി ഒരുക്കി വെച്ച 💘പ്രണയഓർമകളാവും 😍🥰😍❤️  എന്ന് {user1}`",
    "`Dear {victim} 💞💕മരുഭൂമിയിലെ പുതുമഴ✨✨ നൽകുന്ന അനുഭൂതി ആയിരിക്കും നീ 😍 എന്നോട് ഇഷ്ടം തുറന്നു പറയുമ്പോ💝💝 എന്ന് {user1}`",
    "`Dear {victim} 💗ആരും എന്നെ തേടി വന്നില്ലെങ്കിലും 😍😍 നിയെങ്കിലും എന്റെ മനസ്സിലേക്ക് ഓടിച്ചാടി💝 വരുമെന്ന് എനിക്കറിയാം💞💞 എന്ന് {user1}`",
    "`Dear {victim} 💕💞സ്നേഹിക്കാൻ പഠിപ്പിച്ചു തരണ്ട😌 നീ എന്നിലേക്ക് അടുത്തപ്പോഴേക്കും🥳🥳 പ്രണയത്തിന്റെ ആദ്യ പാഠങ്ങൾ ഞാൻ മനസ്സിലാക്കി🥰🥰💘💘.... എന്ന് {user1}`",
    "`Dear {victim} 💙💙മനോഹര ചിന്തകൾ വിഫലമായി നമ്മുടെ ഇളം മനസ്സിൽ തഴുകി ഒളിക്കാൻ🥰🥰 നിനക്കു വേണ്ടി ഒരുക്കി വെച്ച  ഒരു തുണി പന്തൽ💘💘 എങ്കിലും നമുക്കു വേണ്ടി പ്രാർത്ഥിക്കും☺️☺️.. എന്ന് {user1}`",
]


@bot.on(admin_cmd(pattern=r"love(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="Llove(?: |$)(.*)", allow_sudo=True))
async def who(event):
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await edit_or_reply(event, caption)
    except BaseException:
        await edit_or_reply(
            event, "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def get_user(event):
    # Get the user from argument or replied message.
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None
    return replied_user


async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)

    caption = temp.format(user1=DEFAULTUSER, victim=slapped, SURID=SURID)

    return caption
