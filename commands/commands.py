# Commnads

from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ParseMode
from config import Config

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("Like it 馃拹 ",url="https://t.me/PoonyoBot")
]
]

#The Keyboard On Up馃憜
reply_markup = InlineKeyboardMarkup(keyboard)

#Send Start Message
def startMessage(update,context):
 try:
  update.message.reply_text(Config.START_TEXT.format(update.message.from_user.full_name,update.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
 	update.message.reply_text(e)

#Help Message
def helpMessage(update,context):
 try:
   update.message.reply_text(Config.HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
  	update.message.reply_text(e)
