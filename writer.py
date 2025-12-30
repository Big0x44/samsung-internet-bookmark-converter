from bookmark import Bookmark
import time

class BookmarkWriter:
    def __init__(self, file_path: str):
        self.__file_path = file_path
    
    def write(self, bookmarks: list[Bookmark]):      
        with open(self.__file_path, "a") as file:
            self.__write_file_start(file)
            self.__write_bookmarks(file, bookmarks)

    def __write_file_start(self, file):
        lines = [
            "<!DOCTYPE NETSCAPE-Bookmark-file-1>\n",
            "   <Title>Bookmarks</Title>\n",
            "   <H1>Bookmarks</H1>\n"
        ]
        file.writelines(lines)

    def __write_bookmarks(self, file, bookmarks: list[Bookmark]):
        date = int(time.time())

        file.write("    <DL>\n")

        for bookmark in bookmarks:
            file.write(f"       <DT><A HREF=\"{bookmark.get_url()}\" ADD_DATE=\"{date}\" LAST_VISIT=\"{date}\" LAST_MODIFIED=\"{date}\">{bookmark.get_title()}</A></DT>\n")

        file.write("    </DL>\n")
