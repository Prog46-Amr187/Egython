#    Egy - Userbot
#    Owner - @Egython

from telethon import events, Button
from ..Config import Config
from . import TOSH, K, mention


@asst_cmd("/repo|#repo")
async def dev(kimo):
    await kimo.reply(
        "᥀︙ 𝖲𝗈𝗎𝗋𝖼𝗋 𝖤𝗀𝗒𝗍𝗁𝗈𝗇 𝖱𝖾𝗉𝗈",
        buttons=[[Button.url("𝖱𝖾𝗉𝗈", K)]]
    )
   

TOSH_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/b4a17055dafc1adfd226c.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        if query.startswith("بوت") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("قناه السورس🔺.", "https://t.me/Egython"),
                    Button.url("لتنصيب السورس🔻.", "https://github.com/EG-THON/EGYTHON"),
                ]
            ]
            if TOSH_PIC and TOSH_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    TOSH_PIC,
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False
                )
            elif TOSH_PIC:
                result = builder.document(
                    TOSH_PIC,
                    title="Egy - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Egy - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="بوت"))
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(KIM, "بوت")
    await response[0].click(event.chat_id)
    await event.delete()

