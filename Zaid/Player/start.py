import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zaid.filters import command
from Zaid.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**A Telegram Music Bot Based Mongodb.
 Add Me To Ur Chat For and Help and And Support Click On Buttons  ...
💞  These Features A.I Based 
Powered By [ᴍᴀғɪᴀ](t.me/mafiaking_fed) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏩 ❲ 𝐆ʀᴏᴜᴘ 𝐀ᴅᴅ 𝐏ᴀɴɴᴀᴛʜᴀᴠᴀɴ 𝐑ᴀᴛʜᴀᴍ 𝐊ᴀᴋᴋɪ 𝐒ᴀᴠᴀɴ ❳ 🏩", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🤯 𝐇ᴇʟᴘ & 𝐂ᴍᴅs 🤯", url=f"https://t.me/SUPERIOR_BOTS/160"
                    ),
                    InlineKeyboardButton(
                        "🤧 𝐒ᴏᴜʀᴄᴇ 𝐂ᴏᴅᴇ 🤧", url=f"https://t.me/repo_channeleh"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "😻 𝐒ᴜᴘᴘᴏʀᴛ 😻", url=f"https://t.me/tamil_chat_Junctions"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e06467f9618238f8dbe6b.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/{GROUP_SUPPORT}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/88480ef0fc2481cdff010.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝐑ᴇᴘᴏ 🤫", url=f"https://t.me/repo_channeleh")
                ]
            ]
        ),
    )
