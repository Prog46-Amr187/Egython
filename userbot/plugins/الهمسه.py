from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/file/ac4949a11dfca1d647973.jpg"
T = "𝐒𝐨𝐮𝐫𝐜𝐞 𝐄𝐠𝐲𝐭𝐡𝐨𝐧 - 𝐇𝐚𝐦𝐬𝐚.\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**᥀︙ قائـمه اوامر الهمسه :** \n◄ `.الهمسه` لعرض كيفيه ارسال الهمسه من بوتك\n◄ `.همسه` لارسال همسه عن طريق بوت الهمسه  \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐨𝐮𝐫𝐜𝐞 - [𝐋𝐢𝐧𝐤](t.me/Egython) ."

@bot.on(admin_cmd(pattern="م21"))
@bot.on(sudo_cmd(pattern="م21", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, T)


# Wespr - همسه
@bot.on(admin_cmd(pattern="الهمسه$"))
@bot.on(sudo_cmd(pattern="الهمسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا معرف البوت ثم secret ثم تكتب معرف اللي عايز تهمسله ثم الرساله وستضهر ايقونه وتضغط عليها وبس.\n"
        ics_c += f"**- قم بنسخ :**\n `{TBOT} secret @JAI6H الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)


# Wespr - همسه
@bot.on(admin_cmd(pattern="همسه$"))
@bot.on(sudo_cmd(pattern="همسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**- يمكنك ارسال همسة لعده اشخاص مره واحده**\n**- يمكنك همس ( ملصق - صوره - صوت - متحرك - فيديو ) فقط ارسل كلمة همسه للبوت** @BYYiBoT \n**اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا معرف البوت ثم secret ثم تكتب معرف اللي عايز تهمسله ثم الرساله وستضهر ايقونه وتضغط عليها وبس.\n"
        ics_c += f"**- قم بنسخ :**`{TBOT} secret @JAI6H الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)
