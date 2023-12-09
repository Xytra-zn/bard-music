import os
from youtube_dl import YoutubeDL
from spotipy import Spotify
from pydub import AudioSegment
import logging

class MusicPlayer:
    def __init__(self, client):
        self.client = client
        self.current_song = None
        self.queue = []
        self.auto_play = False

    def is_youtube_url(self, url):
        return "youtube.com" in url or "youtu.be" in url

    def is_spotify_url(self, url):
        return "open.spotify.com" in url

    def play_song(self, query):
        try:
            if self.is_youtube_url(query):
                self.play_youtube_song(query)
            elif self.is_spotify_url(query):
                self.play_spotify_song(query)
            else:
                self.client.send_message(self.chat_id, "Unsupported format")
        except Exception as e:
            logging.error(f"Error while playing song: {str(e)}")
            self.client.send_message(self.chat_id, "An error occurred while playing the song.")

    def play_youtube_song(self, url):
        try:
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                self.current_song = info["title"]
                self.queue.append(info["formats"][0]["url"])
                self.play_audio()
        except Exception as e:
            logging.error(f"Error while playing YouTube song: {str(e)}")
            self.client.send_message(self.chat_id, "An error occurred while playing the YouTube song.")

    def play_spotify_song(self, url):
        try:
            sp = Spotify()
            track = sp.track(url)
            audio_url = track["preview_url"]
            self.current_song = track["name"]
            self.queue.append(audio_url)
            self.play_audio()
        except Exception as e:
            logging.error(f"Error while playing Spotify song: {str(e)}")
            self.client.send_message(self.chat_id, "An error occurred while playing the Spotify song.")

    def play_audio(self):
        try:
            if self.queue:
                audio_url = self.queue.pop(0)
                self.client.send_voice_chat(self.chat_id, audio_url)
            else:
                self.current_song = None
                if self.auto_play:
                    self.client.send_message(self.chat_id, "Queue is empty")
                else:
                    self.client.send_voice_chat_ended(self.chat_id)
        except Exception as e:
            logging.error(f"Error while playing audio: {str(e)}")
            self.client.send_message(self.chat_id, "An error occurred while playing the audio.")

    # Add other methods with improved error handling

                                        
