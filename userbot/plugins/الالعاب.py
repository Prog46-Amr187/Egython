""" ยฉEgythonโข - @JAI6H """

import asyncio
import random
import pyfiglet
from telethon.tl.types import InputMediaDice
from time import sleep
from datetime import datetime
from telethon import Button, events
from telethon.events import CallbackQuery
from telethon.utils import get_display_name
from collections import deque
from random import choice
from . import ALIVE_NAME
from ..helpers import fonts as emojify
from ..helpers.utils import reply_id, _icssutils, parse_pre, install_pip, get_user_from_event, _format
from . import deEmojify
from ..helpers import get_user_from_event
# EMOJI CONSTANTS
DART_E_MOJI = "๐ฏ"
DICE_E_MOJI = "๐ฒ"
BALL_E_MOJI = "๐"
FOOT_E_MOJI = "โฝ๏ธ"
SLOT_E_MOJI = "๐ฐ"
# EMOJI CONSTANTS

U = "๐๐จ๐ฎ๐ซ๐๐ ๐๐ ๐ฒ๐ญ๐ก๐จ๐ง - ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ.\n\n\n**แฅ๏ธ ูุงุฆููู ุงูุงูุฑ ุงูุงูุนุงุจ :** \n\nโ  `.ุจูุงู` ูุนุฑุถ ูุงุฆููุฉ ุงูุงูุนูุงุจ ุงูุงุญุชุฑุงูููู\nโ  `.ูุช` ูุนุจูุฉ ููุช ุชูููุช \nโ  `.ุงูุณ ุงู`\nโ  `.ุณูู`\nโ  `.ูุฑุฏ`\nโ  `.ุณูุฉ`\nโ  `.ูุฏู`\nโ  `.ุญุธ` \n\nโข ๐ข๐ง : @EGYTHON"

@bot.on(admin_cmd(pattern="ู22"))
@bot.on(sudo_cmd(pattern="ู22", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, U)

@bot.on(admin_cmd(pattern="ุงูุณ ุงู$"))
@bot.on(sudo_cmd(pattern="ุงูุณ ุงู$", allow_sudo=True))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@bot.on(admin_cmd(pattern=f"({DART_E_MOJI}|ุณูู)( ([1-6])|$)"))
@bot.on(
    sudo_cmd(
        pattern=f"({DART_E_MOJI}|ุณูู)( ([1-6])|$)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "ุณูู":
        emoticon = "๐ฏ"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@bot.on(admin_cmd(pattern=f"({DICE_E_MOJI}|ูุฑุฏ)( ([1-6])|$)"))
@bot.on(
    sudo_cmd(
        pattern=f"({DICE_E_MOJI}|ูุฑุฏ)( ([1-6])|$)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "ูุฑุฏ":
        emoticon = "๐ฒ"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@bot.on(admin_cmd(pattern=f"({BALL_E_MOJI}|ุณูุฉ)( ([1-5])|$)"))
@bot.on(
    sudo_cmd(
        pattern=f"({BALL_E_MOJI}|ุณูุฉ)( ([1-5])|$)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "ุณูุฉ":
        emoticon = "๐"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@bot.on(admin_cmd(pattern=f"({FOOT_E_MOJI}|ูุฏู)( ([1-5])|$)"))
@bot.on(
    sudo_cmd(
        pattern=f"({FOOT_E_MOJI}|ูุฏู)( ([1-5])|$)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "ูุฏู":
        emoticon = "โฝ๏ธ"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


@bot.on(admin_cmd(pattern=f"({SLOT_E_MOJI}|ุญุธ)( ([1-64])|$)"))
@bot.on(
    sudo_cmd(
        pattern=f"({SLOT_E_MOJI}|ุญุธ)( ([1-64])|$)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    if emoticon == "ุญุธ":
        emoticon = "๐ฐ"
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while r.media.value != required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass
    else:
        if event.sender_id == event.client.uid:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))


kettuet = [  
  "ุงูุซุฑ ุดู ููุฑูุฒู .. ุ!",
  "ุงุฎุฑ ููุงู ุฑุญุชูู ..ุ!",
  "ุณููู ุชูุงู @ ูู ุดุฎุต ุชุฑููุฏ ุชุนุชุฑูููู ุจุดู ุ",
  "ุชุบุงุฑ ..ุ!",
  "ููู ุชุนุชููุฏ ุงู ูู ุฃุญูุฏ ูุฑุงูุจูู ๐ฉ๐ผโ๐ป..ุ!",
  "ุฃุดุฎุงุต ุฑุฏุชูู ูุจููู ููุงู ููู ุนุฑูู ููุดู ุณูู ุงูุนูุณ ุตุงุฑุช ูุนูุ",
  "ููุงุฏุชู ุจููุณ ุงูููุงู ุงูู ูุณุฉ ุนุงูุด ุจู ุงู ูุงุ",
  "ุงูุซุฑ ุดู ููุฑูุฒู ุ",
  "ุชุบุงุฑ ุ",
  "ูู ุชุจูุบ ุฐุงูุฑุฉ ูุงุชููุ",
  "ุตูุฏูู ุงุณุฑุงุฑู ุ",
  "ุดุฎุต @ ุชุนุชุฑููุฉ ุจุดู ุ",
  "ูููู ุถุงุน ุนูู ุ",
  "ุงุบุฑุจ ุดูุก ุญุฏุซ ูู ุญูุงุชู ุ",
  " ูุณุจุฉ ุญุจู ููุงูู ุ",
  " ุญููุฉ ุชุฃูุงู ุจููุง ุ",
  " ุงูุซุฑ ุดู ููุฑูุฒู ุ",
  " ูู ุชุนุฑุถุช ููุธูู ูู ูุจูุ",
  " ุฎุงููู ุ",
  " ุชุฒุนูู ุงูุฏููุง ููุฑุถูู ุ",
  " ุชุงุฑูุฎ ุบูุฑ ุญูุงุชู ุ",
  " ุฃุฌูู ุณูุฉ ูููุงุฏูุฉ ูุฑุช ุนููู ุ",
  " ููุงุฏุชู ุจููุณ ุงูููุงู ุงูู ูุณุฉ ุนุงูุด ุจู ุงู ูุงุ",
  " ุชุฒุนูู ุงูุฏููุง ููุฑุถูู ุ",
  " ูุงูู ููุงูุชูุ",
  " ุฏููู ูุฏูุช ุงูู ุณุงูุฑุช ููุง ุ",
  "ุดุฎุต ุงุฐุง ุฌุงู ุจูุทูุนุฉ ุชุชููุณ ุจูุฌูุฏุ",
  " ุชุงุฎุฐ ููููู ุฏููุงุฑ ู ุชุถุฑุจ ุฎูููุ",
  " ุชุงุฑูุฎ ูููุงุฏูุ",
  "ุงุดูู ูุฑู ุญุจูุช ุ",
  " ูููููู ุงู ุงูุญูุงุฉ ุฏุฑูุณ ุ ูุงูู ุฃููู ุฏุฑุณ ุชุนููุชู ูู ุงูุญูุงุฉ ุ",
  " ูู ุชุซู ูู ููุณู ุ",
  " ูู ูุฑู ููุช ูุน ูุงุญุฏู ุ",
  " ุงุณูู ุงูุซูุงุซู ุ",
  "ูููุฉ ูุดุฎุต ุฎุฐููุ",
  "ูู ุงูุช ูุชุณุงูุญ ุ",
  "ุทุฑููุชู ุงููุนุชุงุฏุฉ ูู ุงูุชุฎููุต ูู ุงูุทุงูุฉ ุงูุณูุจูุฉุ",
  "ุนุตูุฑ ูู ูููุฉุ",
  " ุตุฏูู ุฃูู ููุง ุฃุจูู. ุ",
  "ุชุซู ุจู ุงุญุฏ ุ",
  "ูู ูุฑู ุญุจูุช ุ",
  "ุงููู ุงูุฌููุฉ ุงูุชุงููุฉ..... ูุงู ุฑุณูู ุงููู ุตุุ ุงูุง ูุฏููุฉ ุงูุนูู ูุนูู ุ",
  " ุงูุตู ุญูุงุชู ุจูููุชูู ุ",
  " ุญูุงุชู ูุญููุง ุจุฏูู ุ",
  " ูุด ุฑูุชููู ุงูููููุ",
  " ุดู ุชุณูู ูู ุชุญุณ ุจููููุ",
  " ููู ูููุงุฏู ุ",
  " ุงูุซุฑ ูุดุงููู ุจุณุจุจ ุ",
  " ุชุฒุนูู ุงูุฏููุง ููุฑุถูู ุ",
  " ุชุชููุน ููู ุงุญุฏ ุญุงูุฏ ุนููู ูููุฑูู ุ",
  "ูููุฉ ุบุฑูุจุฉ ูู ููุฌุชู ููุนูุงูุงุ",
"   ูู ุชุญุจ ุงุณูู ุฃู ุชุชููู ุชุบููุฑู ูุฃู ุงูุฃุณูุงุก ุณุชุฎุชุงุฑ" ,
"  ููู ุชุดูู ุงูุฌูู ุฐุงุ",
"  ุชุงุฑูุฎ ูู ุชูุณุงู๐ุ",
"  ูู ูู ุงููููู ุฃู ุชูุชู ุฃุญุฏูู ูู ุฃุฌู ุงููุงูุ",
"  ุชุคูู ุงู ูู ุญูุจ ูู ุฃูู ูุธุฑุฉ ููุง ูุง ุ.",
"  โูุงุฐุง ุณุชุฎุชุงุฑ ูู ุงููููุงุช ูุชุนุจุฑ ููุง ุนู ุญูุงุชู ุงูุชู ุนุดุชูุง ุงูู ุงูุขูุ๐ญ",
"  ุทุจุน ูููู ูุฎููู ุชูุฑู ุดุฎุต ุญุชู ูู ููุช ุชูุญุจู๐๐ปโโ๏ธุ",
"  ูุง ูู ููุน ุงูููุณููู ุงูููุถู ูุฏูู ูุงูุฐู ุชุณุชูุน ุฅููู ุฏุงุฆููุงุ ูููุงุฐุง ููุช ุจุงุฎุชูุงุฑู ุชุญุฏูุฏูุงุ",
"  ุฃุทูู ูุฏุฉ ููุช ูููุง ูู ุณุงุนุฉุ",
"  ูููุฉ ุบุฑูุจุฉ ูู ููุฌุชู ููุนูุงูุงุ๐ค",
"  ุฑุฏุฉ ูุนูู ูู ูุฒุญ ูุนู ุดุฎุต ู ุชุนุฑูู ุ",
"  ุดุฎุต ุชุญุจ ุชุณุชูุฒู๐ุ",
"  ุชุดูู ุงูุบูุฑู ุงูุงููู ุงู ุญุจุ",
"  ูุน ุงู ุถุฏ : ุงูููู ุงูุถู ุญู ูู ูุดุงูู ุงูุญูุงุฉุ",
"  ุงุฐุง ุงูุชุดูุช ุฃู ุฃุนุฒ ุฃุตุฏูุงุฆู ูุถูุฑ ูู ุงูุณูุกุ ููููู ุงูุตุฑูุญุ",
"  โููุดุจุงุจ | ุขุฎุฑ ูุฑุฉ ูุตูู ุบุฒู ูู ูุชุงุฉุ๐",
"  ุฃูุตู ููุณู ุจูููุฉุ",
"  ุดูุก ูู ุตุบุฑู ูุงุชุบูุฑ ูููุ",
"  ุฑุฏุฉ ูุนูู ูู ูุฒุญ ูุนู ุดุฎุต ู ุชุนุฑูู ุ",
"  | ุงุฐุง ุดูุช ุญุฏ ูุงุนุฌุจู ูุนูุฏู ุงูุฌุฑุฃู ุงูู ุชุฑูุญ ูุชุชุนุฑู ุนููู ุ ููุฏูุฉ ุงูุญุฏูุซ ุดู ุฑุงุญ ุชููู ุ.",
"  ูููุฉ ูุดุฎุต ุฃุณุนุฏู ุฑุบู ุญุฒูู ูู ูููู ูู ุงูุฃูุงู ุ",
"  ุญุงุฌุฉ ุชุดูู ููุณู ูุจุฏุน ูููุง ุ",
"  ูููู ููุงุจุณู ุชููู ูุงุฑูุฉ ุ",
"  ูููู ุถุงุน ุนููุ",
"  ุงุฐุง ุงูุชุดูุช ุฃู ุฃุนุฒ ุฃุตุฏูุงุฆู ูุถูุฑ ูู"," ุงูุณูุกุ ููููู ุงูุตุฑูุญุ",
"  ูู ูู ุงููููู ุฃู ุชูุชู ุฃุญุฏูู ูู ุฃุฌู ุงููุงูุ",
"  ูููู ูุงุณูู ูุนู ุงููุชุฑุฉ ูุฐู ุ",
"  ููู ูู ุฃุญูุงู ููุจูุ",
"  ุตุฑูุญุ ูุดุชุงูุ",
"  ุงุบุฑุจ ุงุณู ูุฑ ุนููู ุ",
"  ุชุฎุชุงุฑ ุฃู ุชููู ุบุจู ุฃู ูุจูุญุ",
"  ุขุฎุฑ ูุฑุฉ ุฃููุช ุฃููุชู ุงูููุถููุฉุ",
"  ุฏููู ูุฏูุช ุงูู ุณุงูุฑุช ููุง๐ุ",
"  ุงุดูุงุก ุตุนุจ ุชุชูุจููุง ุจุณุฑุนู ุ",
"  ูููุฉ ูุดุฎุต ุบุงูู ุงุดุชูุช ุฅูููุ๐",
"  ุงูุซุฑ ุดูุก ุชุญุณ ุงูู ูุงุช ู ูุฌุชูุนูุงุ",
"  ูู ููููู ูุณุงูุญุฉ ุดุฎุต ุฃุฎุทุฃ ุจุญูู ูููู ูุฏู ุงูุงุนุชุฐุงุฑ ูุดุนุฑ ุจุงููุฏูุ",
"  ุขุฎุฑ ุดูุก ุถุงุน ูููุ",
"  ุชุดูู ุงูุบูุฑู ุงูุงููู ุงู ุญุจุ",
"  ูู ูุฒุนุช/ู ูุตุฏูู/ู ููุงูู ูุงูู ุฏุฎู ูุด ุจุชุณูู/ููุ",
"  ุดูุก ูู ู ุชุฐูุฑุชู ุชุจุชุณู ...",
"  ูู ุชุญุจูุง ูููุงุฐุง ููุช ุจุงุฎุชูุงุฑูุงุ",
"  ูู ุชููู ูุฑุชุจู ุจุงููุงูู ุฃู ุฃูู ุชูุชูู ูุฏู ูุฌุนูู ุชููุฑ ุงููุงูุ",
"  ูุชู ุชูุฑู ุงูุดุฎุต ุงูุฐู ุฃูุงูู ุญุชู ูู ููุช ููู ุฃุดุฏ ูุนุฌุจูููุ",
"  ุฃูุจุญ ุงููุจุญูู ูู ุงูุนูุงูุฉ: ุงูุบุฏุฑ ุฃู ุงูุฅููุงู๐คท๐ผุ", 
"  ูู ูุตูู ุฑุณุงูุฉ ุบูุฑ ูุชููุนุฉ ูู ุดุฎุต ูุฃุซุฑุช ููู ุ",
"  ูู ุชุดุนุฑ ุฃู ููุงูู ููู ููุญุจูุ",
"  ูุด ุงูุดูุก ุงูู ุชุทูุน ุญุฑุชู ููู ู ุฒุนูุช ุ",
"  ุตูุช ูุบูู ู ุชุญุจู",
"  ูู ูู ุญุณุงุจู ุงูุจููู ุ",
"  ุงุฐูุฑ ูููู ูุงุชูุณุงู ุจุนูุฑูุ",
"  ุฑุฏุฉ ูุนูู ูู ูุฒุญ ูุนู ุดุฎุต ู ุชุนุฑูู ุ",
"  ุนูุฏู ุญุณ ููุงูู ููุง ููุณูุฉุ",
"  ูู ูุฌูุฉ ูุธุฑู ูุง ูู ุงูุฃุดูุงุก ุงูุชู ุชุญุงูุธ ุนูู ููุฉ ูุซุจุงุช ุงูุนูุงูุฉุ",
"  ูุง ูู ููุน ุงูููุณููู ุงูููุถู ูุฏูู ูุงูุฐู ุชุณุชูุน ุฅููู ุฏุงุฆููุงุ ูููุงุฐุง ููุช ุจุงุฎุชูุงุฑู ุชุญุฏูุฏูุงุ",
"  ูู ุชููู ูุฑุชุจู ุจุงููุงูู ุฃู ุฃูู ุชูุชูู ูุฏู ูุฌุนูู ุชููุฑ ุงููุงูุ",
"  ูู ูุตูู ุฑุณุงูุฉ ุบูุฑ ูุชููุนุฉ ูู ุดุฎุต ูุฃุซุฑุช ููู ุ",
"  ุดูุก ูู ุตุบุฑู ูุงุชุบูุฑ ูููุ",
"  ูู ููููู ุฃู ุชุถุญู ุจุฃูุซุฑ ุดูุก ุชุญุจู ูุชุนุจุช ููุญุตูู ุนููู ูุฃุฌู ุดุฎุต ุชุญุจูุ",
"  ูู ุชุญุจูุง ูููุงุฐุง ููุช ุจุงุฎุชูุงุฑูุงุ",
"  ูู ูุฒุนุช/ู ูุตุฏูู/ู ููุงูู ูุงูู ุฏุฎู ูุด ุจุชุณูู/ููุ",
"  ูููุฉ ูุดุฎุต ุฃุณุนุฏู ุฑุบู ุญุฒูู ูู ูููู ูู ุงูุฃูุงู ุ",
"  ูู ูุฑู ุชุณุจุญ ุจุงูููู",
"  ุฃูุถู ุตูุฉ ุชุญุจู ุจููุณูุ",
"  ุฃุฌูู ุดูุก ุญุตู ูุนู ุฎูุงู ูุงููููุ",
"  โุดูุก ุณูุนุชู ุนุงูู ูู ุฐููู ูุงููููููุ",
"  ูู ููููู ุชุบููุฑ ุตูุฉ ุชุชุตู ุจูุง ููุท ูุฃุฌู ุดุฎุต ุชุญุจู ูููู ูุง ูุญุจ ุชูู ุงูุตูุฉุ",
"  โุฃุจุฑุฒ ุตูุฉ ุญุณูุฉ ูู ุตุฏููู ุงูููุฑุจุ",
"  ูุง ุงูุฐู ูุดุบู ุจุงูู ูู ุงููุชุฑุฉ ุงูุญุงููุฉุ",
"  ุขุฎุฑ ูุฑุฉ ุถุญูุช ูู ูู ููุจูุ",
"  ุงุญูุฑ ุงููุงุณ ูู ูู ...",
"  ุงูุซุฑ ุฏููู ูุฏู ุชุณุงูุฑ ููุง๐ุ",
"  ุขุฎุฑ ุฎุจุฑ ุณุนูุฏุ ูุชู ูุตููุ",
"  โูุณุจุฉ ุงุญุชูุงุฌู ููุนุฒูุฉ ูู 10๐ุ",
"  ูู ุชููู ูุฑุชุจู ุจุงููุงูู ุฃู ุฃูู ุชูุชูู ูุฏู ูุฌุนูู ุชููุฑ ุงููุงูุ",
"  ุฃูุซุฑ ุฌููุฉ ุฃุซุฑุช ุจู ูู ุญูุงุชูุ",
"  ูู ูุงููุง ูู  ุชูุงูู ุตูู ูุงุญุฏ ููุท ูู ุงูุทุนุงู ููุฏุฉ ุดูุฑ .",
"  ูู ุชููู ูุฑุชุจู ุจุงููุงูู ุฃู ุฃูู ุชูุชูู ูุฏู ูุฌุนูู ุชููุฑ ุงููุงูุ",
"  ุขุฎุฑ ูุฑุฉ ุถุญูุช ูู ูู ููุจูุ",
"  ูุด ุงูุดูุก ุงูู ุชุทูุน ุญุฑุชู ููู ู ุฒุนูุช ุ",
"  ุชุฒุนูู ุงูุฏููุง ููุฑุถูู ุ",
"  ูุชู ุชูุฑู ุงูุดุฎุต ุงูุฐู ุฃูุงูู ุญุชู ูู ููุช ููู ุฃุดุฏ ูุนุฌุจูููุ",
"  ุชุนุชูุฏ ููู ุฃุญุฏ ูุฑุงูุจู๐ฉ๐ผโ๐ปุ",
"  ุงุญูุฑ ุงููุงุณ ูู ูู ...",
"  ุดูุก ูู ุตุบุฑู ูุงุชุบูุฑ ูููุ",
"  ููู ูููู ุงูุณุนุงุฏู ุจุฑุงููุ",
"  ูู ุชุบุงุฑูู ูู ุตุฏููุงุชูุ",
"  ุฃูุซุฑ ุฌููุฉ ุฃุซุฑุช ุจู ูู ุญูุงุชูุ",
"  ูู ุนุฏุฏ ุงููู ูุนุทููู ุจููู๐นุ",
"  ุฃุฌูู ุณูุฉ ูููุงุฏูุฉ ูุฑุช ุนููู ุ",
"  ุฃูุตู ููุณู ุจูููุฉุ",
 ]

@bot.on(admin_cmd(pattern="ูุช(?: |$)(.*)"))
async def permalink(mention):
    Egythont = random.choice(kettuet)
    await edit_or_reply(mention, f"**แฅ๏ธ{Egythont} **")


CMD_HELP.update(
    {
        "ุงูุงูุนุงุจ": "**Syntax :** `.๐ฏ [1-6]` or `.ุณูู [1-6]`\
    \n**Usage : **each number shows different animation for dart\
    \n\n**Syntax : **`.๐ฒ [1-6]` or `.ูุฑุฏ [1-6]`\
    \n**Usage : **each number shows different animation for dice\
    \n\n**Syntax : **`.๐ [1-5]` or `.ุณูุฉ [1-5]`\
    \n**Usage : **each number shows different animation for basket ball\
    \n\n**Syntax : **`.โฝ๏ธ [1-5] `or `.ูุฏู [1-5]`\
    \n**Usage : **each number shows different animation for football\
    \n\n**Syntax : **`.๐ฐ [1-64] `or `.ุญุธ [1-64]`\
    \n**Usage : **each number shows different animation for slot machine(jackpot)\
    "
    }
)
