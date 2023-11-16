import logging
import os
import time
from pyrogram import filters as Filters
from pyrogram.types import Message
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from ..youtube import GoogleAuth
from ..config import Config
from ..translations import Messages as tr
from ..utubebot import UtubeBot
import httplib2
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)

log = logging.getLogger(__name__)
auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("auth")
    & Filters.user(Config.AUTH_USERS)
)
async def _auth(c: UtubeBot, m: Message) -> None:
    if len(m.command) == 1:
        await m.reply_text(tr.NO_AUTH_CODE_MSG, True)
        return

    code = m.command[1]

    try:
        auth.Auth(code)
        auth.SaveCredentialsFile(Config.CRED_FILE(m.chat.id))

        msg1 = await m.reply_text(tr.AUTH_SUCCESS_MSG, True)
        msg2 = await msg1.reply_text(tr.AUTH_DATA_SAVE_SUCCESS, True)

    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(tr.AUTH_FAILED_MSG.format(e), True)


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("refresh")
    & Filters.user(Config.AUTH_USERS)
)
async def _refresh(c: UtubeBot, m: Message) -> None:
    url = auth.GetAuthUrl()
    try:
        auth.LoadCredentialsFile(Config.CRED_FILE(m.chat.id))
        auth.credentials.refresh(httplib2.Http())
        auth.SaveCredentialsFile(Config.CRED_FILE(m.chat.id))
        await m.reply_text(tr.TOKEN_REFRESH_SUCCESS_MSG, True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(tr.TOKEN_REFRESH_NOT_FOUND_OR_NOTEXPIRED_MSG, quote=True,
                           disable_web_page_preview=True,
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           text="Logout", callback_data='logout'
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="🌎Login🌎", url=url
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           "Help Book📚",
                                           callback_data="help+1",
                                       )
                                   ]
                               ]
                           ),
                           )
