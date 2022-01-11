# whois code for Egython edit by ~ @Egython

import os

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
Egy_TEXT = Config.CUSTOM_ALIVE_TEXT or "• 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑫𝑬𝑨𝑹 ."
ZEDM = Config.CUSTOM_ALIVE_EMOJI or " • "

@bot.on(admin_cmd(pattern="ايدي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ايدي(?: |$)(.*)", allow_sudo=True))
async def who(event):
    ics = await eor(event, "⏳")
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await eor(ics, "لايمكنني العثور ع المستخدم")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await ics.delete()
    except TypeError:
        await ics.edit(caption, parse_mode="html")


async def get_user(event):
    if event.reply_to_msg_id and not event.pattern_match.group(1):
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
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "لاتوجد صوره بروفايل"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except:
        pass
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("لايوجد معرف")
    user_bio = "لاتوجد نبذه" if not user_bio else user_bio
    rotbat = ".مطـور السورس ." if user_id == 2019189055 or user_id == 1290321198 or user_id == 1337732405 or user_id == 1985220043 or user_id == 1944479661 or user_id == 1441837187 or user_id == 1993573528 or user_id == 1355571767 or user_id == 1850008091 or user_id == 1933191679 or user_id == 1691343402 else (".「 العضـو 𓅫 」.") 
    rotbat = "مـالك الحساب" if user_id == (await event.client.get_me()).id and user_id != 2019189055 and user_id != 1290321198 and user_id != 1337732405 and user_id != 1985220043 and user_id != 1944479661 and user_id != 1441837187 and user_id != 1993573528 and user_id != 1355571767 and user_id != 1850008091 and user_id != 1933191679 and user_id != 1691343402 else rotbat
    caption = f"<b> {Egy_TEXT} </b>\n"
    caption += f"<b> 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 </b>\n"
    caption += f"<b> {ZEDM}| 𝑵𝑨𝑴𝑬    » </b> {first_name} {last_name}\n"
    caption += f"<b> {ZEDM}| 𝑼𝑺𝑬𝑹  » </b> {username}\n"
    caption += f"<b> {ZEDM}| 𝑰𝑫   » </b> <code>{user_id}</code>\n"
    caption += f"<b> {ZEDM}| 𝑹𝑶𝑼𝑻𝑩𝑨  » {rotbat} </b>\n"
    caption += f"<b> {ZEDM}| 𝑵𝑼𝑴𝑩𝑹 𝑷𝑰𝑪   » </b> {replied_user_profile_photos_count}\n"
    caption += f"<b> {ZEDM}| 𝑷𝑹𝑶 𝑳𝑰𝑵𝑲 » </b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"\n<b> {ZEDM}| 𝑮𝑹𝑶𝑼𝑷𝑺 » </b> {common_chat} \n"
    caption += f"<b> {ZEDM}| 𝑩𝑰𝑶    » </b> {user_bio} \n"
    caption += f"<b> 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 </b>\n"
    caption += f"<b> 𝑺𝑶𝑼𝑹𝑪𝑬 𝑬𝑮𝒀𝑻𝑯𝑶𝑵 » </b> - @Egython"
    return photo, caption


@bot.on(admin_cmd(pattern="ا(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ا(?: |$)(.*)", allow_sudo=True))
async def who(event):
    ics = await eor(event, "⇆")
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await eor(ics, "لايمكنني العثور ع المستخدم")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await ics.delete()
    except TypeError:
        await ics.edit(caption, parse_mode="html")


async def get_user(event):
    if event.reply_to_msg_id and not event.pattern_match.group(1):
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
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "لاتوجد صوره بروفايل"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except:
        pass
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("لايوجد معرف")
    user_bio = "لاتوجد نبذه" if not user_bio else user_bio
    rotbat = "مطـور السورس" if user_id == 2019189055 or user_id == 1290321198 or user_id == 1337732405 or user_id == 1985220043 or user_id == 1944479661 or user_id == 1441837187 or user_id == 1993573528 or user_id == 1355571767 or user_id == 1850008091 or user_id == 1933191679 or user_id == 1691343402 else ("العضـو") 
    rotbat = "مـالك الحساب" if user_id == (await event.client.get_me()).id and user_id != 2019189055 and user_id != 1290321198 and user_id != 1337732405 and user_id != 1985220043 and user_id != 1944479661 and user_id != 1441837187 and user_id != 1993573528 and user_id != 1355571767 and user_id != 1850008091 and user_id != 1933191679 and user_id != 1691343402 else rotbat
    caption = f"<b> {Egy_TEXT} </b>\n"
    caption += f"<b> 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 </b>\n"
    caption += f"<b> {ZEDM}| 𝑵𝑨𝑴𝑬    » </b> {first_name} {last_name}\n"
    caption += f"<b> {ZEDM}| 𝑼𝑺𝑬𝑹  » </b> {username}\n"
    caption += f"<b> {ZEDM}| 𝑰𝑫   » </b> <code>{user_id}</code>\n"
    caption += f"<b> {ZEDM}| 𝑹𝑶𝑼𝑻𝑩𝑨  » {rotbat} </b>\n"
    caption += f"<b> {ZEDM}| 𝑵𝑼𝑴𝑩𝑹 𝑷𝑰𝑪   » </b> {replied_user_profile_photos_count}\n"
    caption += f"<b> {ZEDM}| 𝑷𝑹𝑶 𝑳𝑰𝑵𝑲 » </b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"\n<b> {ZEDM}| 𝑮𝑹𝑶𝑼𝑷𝑺 » </b> {common_chat} \n"
    caption += f"<b> {ZEDM}| 𝑩𝑰𝑶    » </b> {user_bio} \n"
    caption += f"<b> 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 </b>\n"
    caption += f"<b> 𝑪𝑯 𝑬𝑮𝒀𝑻𝑯𝑶𝑵 » </b> - @Egython"
    return photo, caption


@bot.on(
    icss_cmd(pattern="رابط الحساب(?: |$)(.*)")
)
@bot.on(
    sudo_cmd(pattern="رابط الحساب(?: |$)(.*)", allow_sudo=True)
)
async def permalink(tosh):
    user, custom = await get_user_from_event(tosh)
    if not user:
        return
    if custom:
        await eor(
            tosh, f"**┦ رابط الحساب ↫** [{custom}](tg://user?id={user.id}) **.**"
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await eor(
            tosh, f"**┦ رابط الحساب ↫** [{tag}](tg://user?id={user.id}) **.**"
        )


async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("اكتب اسم المستخدم أو المعرف أو قم برد على رسالة المستخدم!‌‌")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "ايدي": "**Plugin : **`ايدي`\n\n"
        "**⌔∮ الامر : `.ايدي`\n**"
        "**⌔∮ الفائده منه :** لعرض معلومات الحساب\n\n"
        "**⌔∮ الامر : `.رابط الحساب`\n**"
        "**⌔∮ الفائده منه :** لعرض رابط الحساب"
    }
)
