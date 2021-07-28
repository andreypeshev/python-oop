from project3.album import Album
from project3.song import Song

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if not album.published:
                    self.albums.remove(album)
                    return f"Album {album_name} has been removed."
                return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        album_list = [album.details() for album in self.albums]
        nl = '\n'
        return f"Band {self.name}\n" \
               f"{nl.join(album_list)}"



