# config


import os

class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 START_TEXT="Hello [{}](tg://user?id={})🌷\nI am **ANONYMOUS** Sender Bot.\nJust Forward me Some messages or media and I will Erase the sender tag & will give You.\nSend /help To Know More\n "
 HELP_TEXT="Forward Me A File 🗂, Video 📀, Audio 📻,Photo 📷 or Anything And \nI will Send You the File Back.\n\n**How to Set Caption ?**\nReply Caption to a File, Photo, Audio, Media."
	
