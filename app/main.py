from app.book import Book
from app.book_service import BookServiceReverse, BookServiceConsole
from app.book_serializer import BookXMLSerializer, BookJSONSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if method_type == "console":
            book_service = BookServiceConsole()
        elif method_type == "reverse":
            book_service = BookServiceReverse()
        elif method_type == "xml":
            serializer = BookXMLSerializer()
        elif method_type == "json":
            serializer = BookJSONSerializer()

        if cmd == "display":
            book_service.display(book)
        elif cmd == "print":
            book_service.print_book(book)
        elif cmd == "serialize":
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
