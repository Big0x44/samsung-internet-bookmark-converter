import sys
from reader import BookmarkReader
from writer import BookmarkWriter

def main():
    if len(sys.argv) < 3:
        print("Incorrect command line arguments provided.\nUsage: main.py <input_file> <output_file>")
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Start reading from input file {input_file}.")
    reader = BookmarkReader(input_file)
    bookmarks = reader.convert()
    print(f"{len(bookmarks)} bookmarks provided.")

    print(f"Write to {output_file}")
    writer = BookmarkWriter(output_file)
    writer.write(bookmarks)
    print("Successfully converted all bookmarks!")


if __name__ == '__main__':
    main()