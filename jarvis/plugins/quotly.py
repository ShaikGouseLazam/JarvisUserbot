"""QuotLy: Avaible commands: .qbot
"""
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from jarvis import bot
from jarvis.utils import admin_cmd, eor, sudo_cmd


# @register(outgoing=True, pattern="^.q(?: |$)(.*)")
@jarvis.on(admin_cmd(pattern=r"qbot(?: |$)(.*)", outgoing=True))
@jarvis.on(sudo_cmd(pattern=r"qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        jevent = await eor(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await jevent.edit("```Reply to text message```")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await jevent.edit("```Reply to actual users message.```")
        return
    await jevent.edit("```Making a Quote```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await jevent.edit("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await jevent.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
