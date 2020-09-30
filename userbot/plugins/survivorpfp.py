"""
Time In Profile Pic.....
Command: `.survivorpfp`,.alandp,.epp

Custom / Modified Plugin for some magical effects by this Legendary Guy @Sur_vivor


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_FILE_TO_USEE = "userbot/helpers/styles/digital.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/2eab4f64ead6fbf41bf87.jpg",
    "https://telegra.ph/file/6bef1ffbaddc5230c2ae1.jpg",
    "https://telegra.ph/file/a03f035e83098a7c5bded.jpg",
    "https://telegra.ph/file/f0a230a30b9952f56d2cd.jpg",
    "https://telegra.ph/file/d00e6bb4b4a483099c992.jpg",
    "https://telegra.ph/file/1270ed675db61e6c84eea.jpg",
    "https://telegra.ph/file/32743c9389915b02fdea7.jpg",
    "https://telegra.ph/file/8c02a1430502bea931ff7.jpg",
    "https://telegra.ph/file/1ec37d367bb59ac56131d.jpg",
    "https://telegra.ph/file/e9aeef4fd2e3d0b9e9f24.jpg",
    "https://telegra.ph/file/28c242ea9f8cf32db4c21.jpg",
    "https://telegra.ph/file/c089426ca031d1f6297b0.jpg",
    "https://telegra.ph/file/a196b6c07f0a659daf058.jpg",
    "https://telegra.ph/file/69f19acd13b1eaf3fc120.jpg",
]

TELEGRAPH_MEDIA_LINKSS = [
    "https://telegra.ph/file/b2cea1712ebaca603e6f4.jpg",
]

TELEGRAPH_MEDIA_LINKSSS = [
    "https://telegra.ph/file/b20273be27aeea4e8fcac.jpg",
]


@borg.on(admin_cmd(pattern="survivorpfp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "@Sur_vivor \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((350, 400), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(30)
        except:
            return


@borg.on(admin_cmd(pattern="alandp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKSS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKSS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass
        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime("@Sur_vivor \n\n  %H:%M:%S \n %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USEE, 35)
        drawn_text.text((10, 40), current_time, font=fnt, fill=(255, 0, 0))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(90)
        except:
            return


@borg.on(admin_cmd(pattern="epp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKSSS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKSSS[piclink]
        downloaded_file_name = "./userbot/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "@Sur_vivor \n \nTime: %H:%M:%S \nDate: %d/%m/%y"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((50, 600), current_time, font=fnt, fill=(230, 230, 250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(90)
        except:
            return


@borg.on(admin_cmd(pattern="cname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%y")
        HM = time.strftime("%H:%M")
        name = f"{HM}🔥Տմɾѵíѵօɾ🔥{DMY}"
        logger.info(name)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    last_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Changed Profile Picture"
        # )
        await asyncio.sleep(60)
