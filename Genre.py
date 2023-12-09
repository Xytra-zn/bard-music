import logging
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Genre:
    def __init__(self, client):
        self.client = client

    def get_genres(self):
        try:
            # Available genres
            genres = ["पॉप", "रॉक", "हिप हॉप", "इ.डी.एम.", "देश", "भोजपुरी", "दुखद गाने", "लोफाई", "बास बूस्ट"]

            # Create inline buttons for each genre
            buttons = [
                InlineKeyboardButton(genre, callback_data=f"play_genre_{genre}") for genre in genres
            ]

            # Create keyboard markup
            reply_markup = InlineKeyboardMarkup([buttons])

            # Send message with inline buttons
            self.client.send_message(self.chat_id, "उपलब्ध जेनर का चयन करें:", reply_markup=reply_markup)
        except Exception as e:
            logging.error(f"जेनर प्राप्त करने में त्रुटि: {str(e)}")
            self.client.send_message(self.chat_id, "जेनर प्राप्त करने में कोई त्रुटि आई।")

    def play_genre(self, genre_name):
        try:
            # Implement logic to play songs based on the selected genre
            self.client.send_message(self.chat_id, f"आपने {genre_name} जेनर का चयन किया है। गाने बजा रहा हूँ!")
        except Exception as e:
            logging.error(f"जेनर आधारित गाने बजाने में त्रुटि: {str(e)}")
            self.client.send_message(self.chat_id, "जेनर आधारित गाने बजाने में कोई त्रुटि आई।")
