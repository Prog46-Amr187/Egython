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

@icssbot.on(admin_cmd(pattern="زواج$"))
async def _(event):
    catevent = await edit_or_reply(event, "**جاري جلب بيبي**")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])