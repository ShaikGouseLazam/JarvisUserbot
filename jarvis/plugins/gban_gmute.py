# GOT FROM HERE https://t.me/pldhsys/358 ( JAVES USERBOT ) ( MAIN CREATOR )
# PORTED BY SPIDY
from jarvis import bot, CMD_HELP
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import GetCommonChatsRequest
from telethon.events import ChatAction
 


@command(outgoing=True, pattern="^.gmute(?: |$)(.*)")
async def gmute(userbot): 
   lol = userbot ; sender = await lol.get_sender() ; me = await lol.client.get_me()
   if not sender.id == me.id:
        jarvis = await lol.reply("Wait ! Let Me Process Your Request")
   else:
    	jarvis = await lol.edit("Oh ! Wait Let Me Try")   
   me = await userbot.client.get_me() ; await jarvis.edit(f"Gmuting This Nigga") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await userbot.get_chat() ; a = b = 0
   if userbot.is_private:       
   	user = userbot.chat ; reason = userbot.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = userbot.chat.title  
   try:       
    user, reason = await get_user_from_event(userbot)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await jarvis.edit("**This Plugin Can't Work On P.V.T chats ! **")
   if user:      
        if user.id == 1263617196:     
    	             return await jarvis.edit("**You Can't GMUTE a Dev**")
        try:
          from jarvis.modules.sql_helper.globelmute_sql import globelmute          
        except:
   	     pass        
   else:
       return await jarvis.edit(f" **Reply to a user !!**")        
   try:
     if globelmute(user.id) is False:
            return await jarvis.edit(f"**User Has Tape On His Mouth Already !**")
   except:
    	pass
   return await jarvis.edit(f"`Globelly taped on Mouth`") 
 
@command(outgoing=True, pattern="^.ungmute(?: |$)(.*)")
async def gspider(userbot):    
   lol = userbot ; sender = await lol.get_sender() ; me = await lol.client.get_me()
   if not sender.id == me.id:
        jarvis = await lol.reply("Ya Wait Let Me Process Your Request")
   else:
    	jarvis = await lol.edit("Hmm , Wait Let Me Process")   
   me = await userbot.client.get_me() ; await jarvis.edit(f"`Removing Tape From Mouth !`") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await userbot.get_chat() ; a = b = 0   
   try:
     from jarvis.modules.sql_helper.globelmute_sql import unglobelmute
   except:
   	return
   if userbot.is_private:       
   	user = userbot.chat ; reason = userbot.pattern_match.group(1) ; chat_title = 'PM'  
   else:   	   	
   	chat_title = userbot.chat.title  
   try:       
    user, reason = await get_user_from_event(userbot)    
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await jarvis.edit(f"**This Plugin Won't Work In Pvt Groups / Chats?**")
   if not user:       
       return await jarvis.edit(f" **Reply to a user To Ungmute !**")        
   try:
     if unglobelmute(user.id) is False:
            return await jarvis.edit(f"**Error! User probably already ungmuted.**")
   except:
    	pass
   return await jarvis.edit(f"`Ungmute Sucessfull`") 
        

#@javes.on(rekcah05(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
@command(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gspider(userbot): 
   lol = userbot ; sender = await lol.get_sender() ; me = await lol.client.get_me()
   if not sender.id == me.id:
        jarvis = await lol.reply("Gbanning This User !")
   else:
    	jarvis = await lol.edit("Wait Processing.....")      
   me = await userbot.client.get_me() ; await jarvis.edit(f"Global Ban Is Coming ! Wait And Watch You Nigga") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await userbot.get_chat() ; a = b = 0
   if userbot.is_private:       
   	user = userbot.chat ; reason = userbot.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = userbot.chat.title  
   try:       
    user, reason = await get_user_from_event(userbot)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await jarvis.edit(f"**You Cant Use In Pvt Chats // Group!**")
   if user:      
        if user.id == 1263617196:     
    	             return await jarvis.edit(f"**Didn't , Your Father Teach You ? That You Cant Gban Dev**")
        try:
          from jarvis.modules.sql_helper.gmute_sql import gmute            
        except:
   	     pass
        try:
          await userbot.client(BlockRequest(user))
          block = 'True'
        except:      
           pass
        testuserbot = [d.entity.id for d in await userbot.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testuserbot:
            try:
                 await userbot.client.edit_permissions(i, user, view_messages=False)          
                 a += 1
                 await jarvis.edit(f"**GBANNED // Total Affected Chats **: `{a}`")
            except:
                 b += 1                     
   else:
       await jarvis.edit(f"**Reply to a user !!**")        
   try:
     if gmute(user.id) is False:
            return await jarvis.edit(f"**Error! User probably already gbanned.**")
   except:
    	pass
   return await jarvis.edit(f"**Gbanned [{user.first_name}](tg://user?id={user.id}) Affected Chats : {a} **") 
        



#@javes.on(rekcah05(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
@command(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gspider(userbot):
   lol = userbot ; sender = await lol.get_sender() ; me = await lol.client.get_me()
   if not sender.id == me.id:
        jarvis = await lol.reply("`Wait Let Me Process`")
   else:
    	jarvis = await lol.edit("One Min ! ")   
   me = await userbot.client.get_me() ; await jarvis.edit(f"Trying To Ungban User !") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await userbot.get_chat() ; a = b = 0
   if userbot.is_private:       
   	user = userbot.chat ; reason = userbot.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = userbot.chat.title  
   try:       
    user, reason = await get_user_from_event(userbot)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await jarvis.edit("Use In Public Chats , Or In PM")
   if user:      
        if user.id == 1263617196:     
    	             return await jarvis.edit("**You Cant Ungban A Dev !**")
        try:
          from jarvis.modules.sql_helper.gmute_sql import ungmute
        except:
   	     pass
        try:
          await userbot.client(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testuserbot = [d.entity.id for d in await userbot.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testuserbot:
            try:
                 await userbot.client.edit_permissions(i, user, send_messages=True)          
                 a += 1
                 await jarvis.edit(f"**UNGBANNING // AFFECTED CHATS - {a} **")
            except:
                 b += 1                     
   else:
       await jarvis.edit("**Reply to a user !!**")        
   try:
     if ungmute(user.id) is False:
            return await jarvis.edit("**Error! User probably already ungbanned.**")
   except:
    	pass
   return await jarvis.edit(f"**UNGBANNED // USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **") 
        


CMD_HELP.update({
    "gban-gmute":
    ".gban <username> / <userid> / <reply to a user>\
\n**Usage**: Globel ban the person in all groups, channels , block in pm , add gban watch (use with solution) \
\n\n.ungban <username> / <userid> / <reply to a user>\
\n**Usage**: unban user from all groups, channels , remove user from gban watch.\
\n\n.gmute <username> / <userid> / <reply to a user>\
\n**Usage**: Globel mute the user  \
\n\n.ungmute <username> / <userid> / <reply to a user>\
\n**Usage**: Remove user form gmute list \
\n\n**All commands support sudo**\
"
})
