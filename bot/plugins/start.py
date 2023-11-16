from pyrogram import filters as Filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from typing import Union
from pyrogram import enums

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        parse_mode=enums.ParseMode.DEFAULT,
        quote=True,

        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Help Book📚",
                        callback_data="help+1",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Visit Website!💫", url="https://lethargic-sol.netlify.app"
                    ),
                    InlineKeyboardButton(
                        text="Help and Support😌", url="https://t.me/LethargicBots"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌟GITHUB🌟", url="https://github.com/alpha-alexxx/"
                    )
                ],
            ]
        ),
    )
