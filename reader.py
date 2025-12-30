import os
from bookmark import Bookmark

class BookmarkReader:    
    def __init__(self, file_path: str):
        self.__file_path = file_path
    
    def convert(self) -> list[Bookmark]:
        with open(self.__file_path) as file:
            return self.__extract_bookmarks(file)        

    def __extract_bookmarks(self, file) -> list[Bookmark]:
        bookmarks: list[Bookmark] = []

        title: str = None
        url: str = None

        for line in file:
            striped_line = line.rstrip()
            if title is None:
                title = striped_line
            else:
                url = striped_line

            if title is not None and url is not None:
                bookmark = Bookmark(title, url)
                bookmarks.append(bookmark)

                title = None
                url = None

        return bookmarks

            



