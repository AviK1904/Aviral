
 

import telegram.ext
from telegram import *
from telegram.ext import *

def start(update, context):
    update.message.reply_text("Hello! Welcome to a Trainee Bot")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the Trainee Bot
    /help -> This message
    /content -> Here are many playlist that i recomment that can help others
    /Python  -> FULL Python Playlist
    /SQL -> The first video from SQL Playlist
    /CPP -> Full C++ Playlist
    /LinkedIN -> My linkedIN for increasing our reach 
    /contact -> contact information 
     """)
    
def content(update, context):
    update.message.reply_text("I have various playlists and articles to recommend!")

def Python(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg")

def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/pFq1pgli0OQ")
    
def CPP(update, context):
    update.message.reply_text("tutorial link : https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL")
    
def LinkedIN(update, context):
    update.message.reply_text("My LinkedIN link : www.linkedin.com/in/aviral-kumar-b355a422b")
    
def contact(update, context):
    update.message.reply_text("You can contact on my official mail id: aviralkumar1904@gmail.com")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = "5806226964:AAEnF0yo0smdChUeLbA0zIswrbQTjKUJ72Q"
#print(bot.get_me())
updater = telegram.ext.Updater("5806226964:AAEnF0yo0smdChUeLbA0zIswrbQTjKUJ72Q", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('content',content))
disp.add_handler(telegram.ext.CommandHandler('Python',Python))
disp.add_handler(telegram.ext.CommandHandler('SQL',SQL))
disp.add_handler(telegram.ext.CommandHandler('CPP',CPP))
disp.add_handler(telegram.ext.CommandHandler('LinkedIN',LinkedIN))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()