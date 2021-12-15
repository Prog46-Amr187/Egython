#RallsThon

import asyncio
import base64
import os
import random
import shutil
import time
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from . import AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO
from .sql_helper.globals import addgvar, delgvar, gvarstatus

DEFAULTUSERBIO = DEFAULT_BIO or "الحمد الله على كل شئ - @RallsThon"
CHANGE_TIME = Config.CHANGE_TIME
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
ZEDT = Config.CUSTOM_ALIVE_EMZED or " "

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

normzltext = "1234567890"
namerafont = "١٢٣٤٥٦٧٨٩٠"
namerbfont = "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎"
namercfont = "₁₂₃₄₅₆₇₈₉₀"
namerdfont = "¹²³⁴⁵⁶⁷⁸⁹⁰"
namerefont = "➊➋➌➍➎➏➐➑➒✪"
namerffont = "❶❷❸❹❺❻❼❽❾⓿"
namergfont = "➀➁➂➃➄➅➆➇➈⊙"
namerhfont = "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪"
namerifont = "①②③④⑤⑥⑦⑧⑨⓪"
namerjfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
namerkfont = "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶"
namerlfont = "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘"
namermfont = "１２３４５６７８９０"


@bot.on(admin_cmd(pattern="الاسم تلقائي1$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autoaname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي1$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autoabio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي2$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autobname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي2$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autobbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي3$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autocname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي3$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autocbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي4$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autodname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي4$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autodbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي5$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autoename_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي5$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autoebio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي6$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autofname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي6$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autofbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي7$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autogname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي7$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autogbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي8$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autohname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي8$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autohbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي9$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autoiname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي9$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autoibio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي10$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autojname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي10$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autojbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي11$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autokname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي11$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autokbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي12$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await autolname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي12$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autolbio_loop()


@bot.on(admin_cmd(pattern="الاسم تلقائي13$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, f"`الاسم التلقائي ممكّن بالفعل 𓆰`")
    addgvar("autoname", True)
    await edit_delete(event, "**تـم بـدأ الاسـم التـلقائـي 𓆰**")
    await automname_loop()


@bot.on(admin_cmd(pattern="البايو تلقائي13$"))
async def _(event):
    if event.fwd_from:
        return
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, f"** الـنبذة التلقائيه مفعـلة 𓆰**")
    addgvar("autobio", True)
    await edit_delete(event, "** تم تفعيل الـنبذة التلقائيه بنجاح 𓆰**")
    await autombio_loop()


#زلــزال الهيبــه zzzzl1l@

@bot.on(admin_cmd(pattern="انهاء (.*)"))
async def _(event):  # sourcery no-metrics
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "الاسم تلقائي":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**تم إيقاف لاسم التلقائي الآن 𓆰**")
        return await edit_delete(event, "**لم يتم تمكين الاسم التلقائي 𓆰**")
    if input_str == "البايو تلقائي":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "** تم انهاء  البايو التلقائي الان 𓆰**")
        return await edit_delete(event, "** لم يتم تمكين  البايو التلقائي 𓆰**")


async def autoaname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerafont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autoabio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerafont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


async def autobname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerbfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerbfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autocname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namercfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autocbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namercfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autodname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerdfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autodbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerdfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autoename_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerefont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autoebio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerefont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autofname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerffont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autofbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerffont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autogname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namergfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autogbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namergfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autohname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerhfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autohbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerhfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autoiname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerifont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autoibio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerifont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autojname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerjfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autojbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerjfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autokname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerkfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autokbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerkfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def autolname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namerlfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autolbio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namerlfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"

async def automname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
              namefont = namermfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        name = f"{ZEDT}{HM}™"
        LOGS.info(name)
        try:
            await bot(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autombio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%I:%M:%S")
        for normal in HM:
            if normal in normzltext:
              namefont = namermfont[normzltext.index(normal)]
              HM = HM.replace(normal, namefont)
        bio = f"░ {DEFAULTUSERBIO} 𓃬 | {HM}"
        LOGS.info(bio)
        try:
            await bot(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


bot.loop.create_task(autoaname_loop())
bot.loop.create_task(autoabio_loop())
bot.loop.create_task(autobname_loop())
bot.loop.create_task(autobbio_loop())
bot.loop.create_task(autocname_loop())
bot.loop.create_task(autocbio_loop())
bot.loop.create_task(autodname_loop())
bot.loop.create_task(autodbio_loop())
bot.loop.create_task(autoename_loop())
bot.loop.create_task(autoebio_loop())
bot.loop.create_task(autofname_loop())
bot.loop.create_task(autofbio_loop())
bot.loop.create_task(autogname_loop())
bot.loop.create_task(autogbio_loop())
bot.loop.create_task(autohname_loop())
bot.loop.create_task(autohbio_loop())
bot.loop.create_task(autoiname_loop())
bot.loop.create_task(autoibio_loop())
bot.loop.create_task(autojname_loop())
bot.loop.create_task(autojbio_loop())
bot.loop.create_task(autokname_loop())
bot.loop.create_task(autokbio_loop())
bot.loop.create_task(autolname_loop())
bot.loop.create_task(autolbio_loop())
bot.loop.create_task(automname_loop())
bot.loop.create_task(autombio_loop())


CMD_HELP.update(
    {
        "الوقتي 2": """**اسم الاضافـه : **`الوقتي 2`
  **╮•❐ الامـر ⦂ **`.الاسم تلقائي`
•  **الشـرح •• **__لوضـع اسـم وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت__
  **╮•❐ الامـر ⦂ **`.البروفايل تلقائي`
•  **الشـرح •• **__لوضـع بروفايـل وقتـي يتغيـر تلقائيـاً مع حسابـك كل دقيقـه لشرح الامر اذهب الى https://t.me/Ralls_Thon/63 __
  **╮•❐ الامـر ⦂ **`.البايو تلقائي`
•  **الشـرح •• **__لوضـع بايـو وقتـي يتغيـر تلقائـياً مع الوقـت كـل دقيقـه لشرح الامر اذهب الى https://t.me/Ralls_Thon/63 __
  **╮•❐ الامـر ⦂ **`.انهاء + ( الاسم تلقائي/البروفايل تلقائي/البايو تلقائي ) `
•  **الشـرح •• **__لانهـاء الاوامـر الوقتيـه من حسابـك__
"""
    }
)
