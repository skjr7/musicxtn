## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCN4X4pQest0KqFvL7sthu2qJVb1AnK0DQusSQ28dPnSGXYVIH9zH5MdECiwPnIGH0Lf2CtNp4I0Tf5Qh8Tj53K7TzGKbaodS8ViAbhTV8WOC3mGO0itZIlAfAM5BrcwHEZVLYJfpiLjiFGCTpGW1r3aeSL9FTNMPIxX0J5jI6fV7LvycM0-TjTeeK9Wtj3vBzOd-dBAv1eHd9SiPoSiUshGoeUcwIbOBobcpw2VV8DGDdsb5XLbFjO1zN5JKNp_HYUBygSHVQ79Nirk7b_iKzTG48cleJYeMM6IcckgC0Ig52Gmvefwu1HW3HHy5AIqHEvCF1ItUm0JAhKr0MiFujuAAAAAUr0aIEAL")
BOT_TOKEN = getenv("BOT_TOKEN", "5396553905:AAGTjeHg3KX77lt0-WZ-m5deoiK0k06K08w")
BOT_NAME = getenv("BOT_NAME", "One love music")
API_ID = int(getenv("API_ID", "10069388"))
API_HASH = getenv("API_HASH", "87c1643359aed164979679e4c3475c1d")
OWNER_NAME = getenv("OWNER_NAME", "Izzy")
OWNER_USERNAME = getenv("OWNER_USERNAME", "king_of_izzy")
ALIVE_NAME = getenv("ALIVE_NAME", "Ronaldo")
BOT_USERNAME = getenv("BOT_USERNAME", "One_love_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME" , "One Love")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mafia_kings_tg")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mafiaking_fed")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1782402849").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/88480ef0fc2481cdff010.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/eb5c8960da2c2f22f8303.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/skjr7/musicxtn")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/ed69743673752c8380957.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/152a3def02458d6617306.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
