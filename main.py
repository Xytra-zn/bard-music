import os
from pyrogram import Client

app = Client(
    "Music Bot",
    api_id=os.environ["API_ID"],
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

from Music_player import MusicPlayer
from Commands import Commands

music_player = MusicPlayer(app)
commands = Commands(app, music_player)

@app.on_message()
def handle_message(client, message):
    commands.handler(message)

if __name__ == "__main__":
    app.run()
  
