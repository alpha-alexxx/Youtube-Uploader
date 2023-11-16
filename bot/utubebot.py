from pyrogram import Client

from .config import Config


class UtubeBot(Client):
    def __init__(self):
        name = "Youtube_uploader"
        super().__init__(
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins=dict(root="bot.plugins"),
            workers=6,
            name=name

        )
        self.DOWNLOAD_WORKERS = 6
        self.counter = 0
        self.download_controller = {}