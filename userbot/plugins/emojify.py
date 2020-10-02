"""
Created by @Jisan7509
modified by  @mrconfused
Userbot plugin for CatUserbot
"""

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP
from . import fonts as emojify


@borg.on(admin_cmd(pattern="emoji(?: |$)(.*)"))
@borg.on(sudo_cmd(pattern="emoji(?: |$)(.*)", allow_sudo=True))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.kakashiemoji[emojify.kakashitext.index(chutiya)]
            string = string.replace(chutiya, bsdk)
    await edit_or_reply(event, string)


@borg.on(admin_cmd(pattern="cmoji(?: |$)(.*)"))
@borg.on(sudo_cmd(pattern="cmoji(?: |$)(.*)", allow_sudo=True))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(
            event, "`What am I Supposed to do with this nibba/nibbi, Give me a text. `"
        )
        return
    emoji, args = args.split(" ", 1)
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.itachiemoji[emojify.kakashitext.index(chutiya)].format(
                cj=emoji
            )
            string = string.replace(chutiya, bsdk)
    await edit_or_reply(event, string)


CMD_HELP.update(
    {
        "emojify": "**Plugin :** `emojify`\
      \n\n**Syntax :** `.emoji` <text>\
      \n****Usage : **Converts your text to big emoji text, with default emoji. \
      \n\n**Syntax :** `.cmoji` <emoji> <text>\
      \n****Usage : **Converts your text to big emoji text, with your custom emoji.\
      "
    }
)
