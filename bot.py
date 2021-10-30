from pyrogram import Client ,filters
import os
from py_youtube import Data, Search 
from pyrogram.types import *

TOKEN = os.environ.get("2015236172:AAFhhu493IsFKexWpmmZ9qoNrW6ZcC_Fizg", "")

APP_ID = int(os.environ.get("7744764", ""))

API_HASH = os.environ.get("09fb2bd3ee46019e911149d4970bfc47", "")


app = Client( "yt-search",
    bot_token = 2015236172:AAFhhu493IsFKexWpmmZ9qoNrW6ZcC_Fizg,  api_id =7744764 ,    api_hash =09fb2bd3ee46019e911149d4970bfc47)
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	await message.reply_text("Helo iam Youtube Video Search\nUse in inline mode")
	


@app.on_inline_query()
async def search_video(client,query):
	search = []
	result = Search(query.query.strip()).videos()
	for i in result:
		try:
			title = i["title"]
			id = i["id"]
			thumb = i["thumb"][0]
			data = i["simple_data"]
		except:
			pass
		try:
			search.append(
                InlineQueryResultPhoto(
                    title=title,
                    description=data,
                    caption="https://youtu.be/"+id,
                    photo_url=thumb))
		
		except:
		          pass
            
	await query.answer(search)
	
app.run()
