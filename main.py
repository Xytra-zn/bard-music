import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Commands import Commands
from Genre import Genre
from Music_player import MusicPlayer

app = Client(
    "Music Bot",
    api_id=os.environ["API_ID"],
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

music_player = MusicPlayer(app)
commands = Commands(app, music_player)
genre = Genre(app)

# /start command
@app.on_message(filters.command("start"))
def start(client, message):
    client.send_message(
        message.chat.id,
        "Welcome to the Music Bot! Use /help to see available commands."
    )

# /help command
@app.on_message(filters.command("help"))
def help(client, message):
    client.send_message(
        message.chat.id,
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/play - Play a song\n"
        "/pause - Pause the current song\n"
        "/resume - Resume the current song\n"
        "/skip - Skip the current song\n"
        "/queue - Show the current queue\n"
        "/playlist - Create a new playlist\n"
        "/add_to_playlist - Add a song to the playlist\n"
        "/remove_from_playlist - Remove a song from the playlist\n"
        "/get_playlist - Get the playlist\n"
        "/play_playlist - Play the playlist\n"
        "/delete_playlist - Delete the playlist\n"
        "/genre - Get available genres\n"
        "/play_genre - Play songs based on genre"
    )

# /genre command
@app.on_message(filters.command("genre"))
def show_genres(client, message):
    genre.get_genres()

# Callback function for inline buttons
@app.on_callback_query()
def callback_query(client, callback_query):
    query_data = callback_query.data
    if query_data.startswith("play_genre_"):
        selected_genre = query_data.replace("play_genre_", "")
        genre.play_genre(selected_genre)

if __name__ == "__main__":
    app.run()
