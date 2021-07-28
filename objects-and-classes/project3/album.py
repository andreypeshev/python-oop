from project3.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.args = list(args)
        self.published = False

    def add_song(self, song: Song):
        if song not in self.args:
            if not song.single:
                if not self.published:
                    self.args.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."
                return "Cannot add songs. Album is published."
            return f"Cannot add {song.name}. It's a single"
        return "Song is already in the album."

    def remove_song(self, song_name):
        for song in self.args:
            if song.name == song_name:
                if not self.published:
                    self.args.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
                return "Cannot remove songs. Album is published."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        songs_list = [f"== {song.get_info()}" for song in self.args]
        nl = "\n"
        return f"Album {self.name}\n" \
               f"{nl.join(songs_list)}"