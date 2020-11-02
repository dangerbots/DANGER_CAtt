# By Surv_ivor
# Set SUR_PIC and SUR_USERNAME in heroku Var

import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

SUR_PIC = os.environ.get("SUR_PIC", None)
if SUR_PIC is None:
    SUR_PIC = "https://telegra.ph/file/b2cea1712ebaca603e6f4.jpg"
else:
    SUR_PIC = SUR_PIC
SUR_USERNAME = os.environ.get("SUR_USERNAME", None)
SUR_USERNAME = str(SUR_USERNAME) if SUR_USERNAME else "SurCat"


@bot.on(admin_cmd(pattern="spp$"))
async def autopic(event):
    await event.edit(f"Autopic by @Surv_ivor")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(SUR_PIC, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    while True:
        shutil.copy(downloaded_file_name, photo)
        img = Image.open(photo)
        current_time = datetime.now().strftime(
            f"{SUR_USERNAME} \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return
