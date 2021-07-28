class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        page_sep = "-"*11
        result = f"{page_sep}\n"
        for _ in self.photos:
            photos_str = ['[]' for photo in _ if photo]
            result += f"{' '.join(photos_str)}\n" + f'{page_sep}\n'
        return result
