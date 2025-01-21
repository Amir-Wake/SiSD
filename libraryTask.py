"""
Description: Create a library system that can store books, magazines, and DVDs. 
Each item should have a title and additional properties based on the type of item. 
The system should allow users to view all items or search for a specific item by title.
"""

class LibraryItem:
    library_items = []

    def __init__(self, title):
        self._title = title
        LibraryItem.library_items.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def print_item(self):
        print(f"Title: {self.title}")

class Book(LibraryItem):
    def __init__(self, title, author, isbn, num_of_copies):
        super().__init__(title)
        self._author = author
        self._isbn = isbn
        self._num_of_copies = num_of_copies

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def num_of_copies(self):
        return self._num_of_copies

    @num_of_copies.setter
    def num_of_copies(self, value):
        self._num_of_copies = value

    def print_item(self):
        super().print_item()
        print(f"Author: {self.author} \nISBN: {self.isbn} \nNumber of copies: {self.num_of_copies}")

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, publication_date):
        super().__init__(title)
        self._issue_number = issue_number
        self._publication_date = publication_date

    @property
    def issue_number(self):
        return self._issue_number

    @property
    def publication_date(self):
        return self._publication_date

    def print_item(self):
        super().print_item()
        print(f"Issue Number: {self.issue_number} \nPublication Date: {self.publication_date}")

class Dvd(LibraryItem):
    def __init__(self, title, director, genre, running_time):
        super().__init__(title)
        self._director = director
        self._genre = genre
        self._running_time = running_time

    @property
    def director(self):
        return self._director

    @property
    def genre(self):
        return self._genre

    @property
    def running_time(self):
        return self._running_time

    def print_item(self):
        super().print_item()
        print(f"Director: {self.director} \nGenre: {self.genre} \nRunning Time: {self.running_time}")

# Some sample data
books = [
    Book("The Alchemist", "Paulo Coelho", "978-0062315007", 5),
    Book("1984", "George Orwell", "978-0451524935", 3),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 4)
]

magazines = [
    Magazine("National Geographic", 1, "2021-01-01"),
    Magazine("Time", 2, "2021-02-01"),
    Magazine("Forbes", 3, "2021-03-01")
]

dvds = [
    Dvd("Inception", "Christopher Nolan", "Science Fiction", "2h 28m"),
    Dvd("The Matrix", "Lana Wachowski, Lilly Wachowski", "Action", "2h 16m"),
    Dvd("Interstellar", "Christopher Nolan", "Science Fiction", "2h 49m")
]

# View all items or search for a specific item
choice = input("Do you want to view all items? (yes/no): ")
if choice.lower() == "yes":
    for item in LibraryItem.library_items:
        print("\n")
        item.print_item()
else:
    found = False
    while not found:
        title = input("Enter the title of the item you are looking for: ")
        for item in LibraryItem.library_items:
            if item.title.lower() == title.lower():
                found = True
                print(f"Title: {item.title}")
                if isinstance(item, Book):
                    print(f"--Book--\nAuthor: {item.author} \nISBN: {item.isbn} \nNumber of copies: {item.num_of_copies}")
                elif isinstance(item, Magazine):
                    print(f"--Magazine--\nIssue Number: {item.issue_number} \nPublication Date: {item.publication_date}")
                elif isinstance(item, Dvd):
                    print(f"--Dvd--\nDirector: {item.director} \nGenre: {item.genre} \nRunning Time: {item.running_time}")
                break