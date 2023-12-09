from Music_player import MusicPlayer

class Command:
    def __init__(self, name, description, handler):
        self.name = name
        self.description = description
        self.handler = handler

class Commands:
    def __init__(self, client, music_player):
        self.client = client
        self.music_player = music_player
        self.commands = {
            "/play": Command("play", "Plays a song.", self.music_player.play_song),
            "/pause": Command("pause", "Pauses the current song.", self.music_player.pause),
            "/resume": Command("resume", "Resumes the current song.", self.music_player.resume),
            "/skip": Command("skip", "Skips the current song.", self.music_player.skip),
            "/queue": Command("queue", "Shows the current queue.", self.music_player.get_queue),
        }

    def handler(self, message):
        if message.text.startswith("/"):
            command_text = message.text.split()[1]
            if command_text in self.commands:
                command = self.commands[command_text]
                command.handler()
            else:
                self.client.send_message(message.chat.id, "Invalid command")

# Add other commands here if needed
