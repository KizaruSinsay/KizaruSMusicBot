# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Дайте права в вашем канале и попробуйте снова</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "KizaruSinsayMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Я присоеденился сюда по вашей команде")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>помощник готов к присоеденению в вашему чату</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Ошибка, ожидает спада флуда 🛑 \n Участник {user.first_name} не смог присоединиться к вашей группе из-за большого количества запросов на присоединение юзер бота! Проверьте черный список, разбаньте юзер бота если он там."
            "\n\nOr manually add @DaisyXhelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>помощник присоеденился к вашему чату</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Юзер не смог покинуть группу из-за флуда командой."
            "\n\nOr я выгнан в ручную из вашей группы</b>",
        )
        return
