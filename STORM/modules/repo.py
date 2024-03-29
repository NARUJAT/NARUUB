from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["repo"], ["."]))
async def repo(client, message):
    msg = f"""
    ** ɴᴀʀᴜᴊᴀᴀᴛ ᴜꜱᴇʀʙᴏᴛ **

    • **ʀᴇᴘᴏ** » [click here](https://te.legra.ph/file/ebc3fc421b8776e29ad98.mp4) 
    • **ꜱᴜᴘᴘᴏʀᴛ** » [click here](https://t.me/shayrigalibki) 
    • **ᴜᴘᴅᴀᴛᴇꜱ** » [click here](https://t.me/brokenshayri1)
    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » [click here](https://t.me/mr_naru)
    
    **ʙʏ @mr_naru**
    """
    await message.edit(msg)
