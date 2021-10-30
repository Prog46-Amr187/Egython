"""
©Ralls : @RallsThon
  - Commends of All Wallpapers
"""

from . import *

@bot.on(admin_cmd(pattern="م31"))
@bot.on(sudo_cmd(pattern="م31", allow_sudo=True))
async def icss(aloosh):
    await eor(aloosh, W)

@bot.on(admin_cmd(pattern="خلفيات1"))
@bot.on(sudo_cmd(pattern="خلفيات1", allow_sudo=True))
async def icss(aloosh):
    await eor(aloosh, WL)
    
@bot.on(admin_cmd(pattern="خلفيات2"))
@bot.on(sudo_cmd(pattern="خلفيات2", allow_sudo=True))
async def icss(aloosh):
    await eor(aloosh, BN)

