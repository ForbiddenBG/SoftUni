from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}."
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator + '\n'
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += separator + '\n'
        return result.strip()

    @staticmethod
    def __init_photos(pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result
