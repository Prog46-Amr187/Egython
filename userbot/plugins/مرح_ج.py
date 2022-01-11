# edit by: @Egython for Ralls

import asyncio
from collections import deque
from . import ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ralls"


@icssbot.on(admin_cmd(pattern="زرفه$"))
async def _(event):
    catevent = await edit_or_reply(event, "**💦 جاي زرف الشخص تف**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@icssbot.on(admin_cmd(pattern="بيبي$"))
async def _(event):
    catevent = await edit_or_reply(event, "**جاري جلب بيبي**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@icssbot.on(admin_cmd(pattern="هليكوبتر$"))
async def _(event):
    "جاري تشغيل الهليكوبتر"
    animation_interval = 1.0
    animation_ttl = range(60)
    animation_chars = [
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 👞
                      ╬═╬/▌ 
                      ╬═╬/ \"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 👞
                      ╬═╬/ \"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬/ \👞""""",
    ]
    event = await edit_or_reply(event, "جاري تشغيل الهليكوبتر")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])    


@icssbot.on(admin_cmd(pattern="قروده$"))
async def _(event):
    "animation command"
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "قروده....")
    animation_chars = [
        "🐵",
        "🙉",
        "🙈",
        "🙊",
        "🐵",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@icssbot.on(admin_cmd(pattern="ايد$"))
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@icssbot.on(admin_cmd(pattern="قطار$"))
async def _(event):
    animation_interval = 0.2
    animation_ttl = range(30)
    event = await edit_or_reply(event, "قطار")
    animation_chars = [
        "**ت**",
        "**تو**",
        "**توتت**",
        "**توووت**",
        "**تووووت**",
        "**توووووت**",
        "**تووووووت**",
        "**توووووووت**",
        "**توووووووووت**",
        "**توووووووووووت**",
        "**اجه القطار 🚅**",
        "**وخر عن طريق 🚅🚃🚃**",
        "**تووووت 🚅🚃🚃🚃**",
        "**جبنها وجت ويانه 🚅🚃🚃🚃🚃**",
        "**جبناها وجت ويانه 🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**بيباي 🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**مو قطار ضيم**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@icssbot.on(admin_cmd(pattern="رسم$"))
async def _(event):
    event = await edit_or_reply(
        event, "╔═══════════════════╗ \n  \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await event.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )


@icssbot.on(admin_cmd(pattern="تحركات$"))
async def _(event):
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    event = await edit_or_reply(event, "تحركات ....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@icssbot.on(admin_cmd(pattern="ايموجيات$"))
async def _(event):
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "اايموجيات")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@icssbot.on(admin_cmd(pattern="ضحك$"))
async def _(event):
    event = await edit_or_reply(event, "ضحك")
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(20):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern="بوسه$"))
async def _(event):
    event = await edit_or_reply(event, "بوسه")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(20):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern="جوه الدرج$"))
async def _(event):
    animation_interval = 3
    animation_ttl = range(0, 103)
    animation_chars = [
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "😅 @RallsThon `"
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 103]) 


@icssbot.on(admin_cmd(pattern="روميو$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    await event.edit(" 💘 ")
    animation_chars = [
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",    
            "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
            "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
            "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
            ]
    for i in animation_ttl:
        await sleep(animation_interval)
        await event.edit(animation_chars[i % len(animation_chars)])    


@icssbot.on(admin_cmd(pattern="مصاصه$"))
async def _(event):
    "Animation command."
    giveVar = event.text
    sleepValue = 0.5
    lp = giveVar[6:]
    if not lp:
        lp = " 🍭"
    event = await edit_or_reply(event, lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)
    await asyncio.sleep(sleepValue)
    await event.edit(lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)


@icssbot.on(admin_cmd(pattern="تفجير$"))
async def _(event):
    event = await edit_or_reply(event, "جاري تفجير")
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("**بوووووم تم تفجير الضحيه**")
    await asyncio.sleep(2)


@icssbot.on(admin_cmd(pattern="حترك$"))
async def _(event):
    event = await edit_or_reply(event, "جاري اشعال النار")
    await event.edit("تحضر")
    await asyncio.sleep(0.3)
    await event.edit("استعد")
    await asyncio.sleep(0.2)
    await event.edit("ابدا")
    await asyncio.sleep(0.5)
    await event.edit("اخر مره ")
    await asyncio.sleep(0.2)
    await event.edit("اخر مره والله")
    await asyncio.sleep(0.3)
    await event.edit("وين البانزين")
    await asyncio.sleep(0.3)
    await event.edit("🔥🔥🔥")
    await asyncio.sleep(0.3)
    await event.edit("نار حته ابو حطب ممسويها هه 🔥🔥🔥")
    
@icssbot.on(admin_cmd(pattern="اركضلي$"))
async def _(event):
    catevent = await edit_or_reply(event, "**خلنضركص يابه**")
    animation_interval = 0.3
    animation_ttl = range(100)
    animation_chars = ["────██──────▀▀▀██\n──▄▀█▄▄▄─────▄▀█▄▄▄\n▄▀──█▄▄──────█─█▄▄\n─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n─▀───────▀▀─▀───────▀▀",". ────██──────▀▀▀██\n ──▄▀█▄▄▄─────▄▀█▄▄▄\n ▄▀──█▄▄──────█─█▄▄\n ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n ─▀───────▀▀─▀───────▀▀",".  ────██──────▀▀▀██\n  ──▄▀█▄▄▄─────▄▀█▄▄▄\n  ▄▀──█▄▄──────█─█▄▄\n  ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n  ─▀───────▀▀─▀───────▀▀",".   ────██──────▀▀▀██\n   ──▄▀█▄▄▄─────▄▀█▄▄▄\n   ▄▀──█▄▄──────█─█▄▄\n   ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n   ─▀───────▀▀─▀───────▀▀",".    ────██──────▀▀▀██\n    ──▄▀█▄▄▄─────▄▀█▄▄▄\n    ▄▀──█▄▄──────█─█▄▄\n    ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n    ─▀───────▀▀─▀───────▀▀",".     ────██──────▀▀▀██\n     ──▄▀█▄▄▄─────▄▀█▄▄▄\n     ▄▀──█▄▄──────█─█▄▄\n     ─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n     ─▀───────▀▀─▀───────▀▀"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])
