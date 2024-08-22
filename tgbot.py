import telegram
updater = Updater(token='<YOUR TOKEN HERE>')    
dispatcher = updater.dispatcher
from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest

#YOUR TOKEN(ID)
TOKEN = 'TOKEN'

# If a member is not an administrator, exclude him or her / Wenn ein Mitglied kein Administrator ist, schließen Sie ihn oder sie aus
CHANNEL_ID = '@testtttttttttadsa'

def kick_non_admins(update, context):
    bot = context.bot
    chat = update.message.chat
    admins = [admin.user.id for admin in bot.get_chat_administrators(chat.id)]
    
    
    # We get a list of all channel participants / Wir erhalten eine Liste aller Kanalteilnehmer
    members = bot.get_chat_members(chat.id)
    
    for member in members:
        user_id = member.user.id
        # If a member is not an administrator, exclude him or her / Wenn ein Mitglied kein Administrator ist, schließen Sie ihn oder sie aus
        if user_id not in admins:
            try:
                bot.kick_chat_member(chat.id, user_id)
            except BadRequest as e:
                print(f"Failed to kick {user_id}: {e}")

def start(update, context):
    update.message.reply_text('The bot is active and ready to go!')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("clean", kick_non_admins))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()