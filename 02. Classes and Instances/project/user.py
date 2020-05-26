class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        # {usernames: {book names: days left}}
        # {author:[title1, title2...]}
        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)

            if self.username not in library.rented_books:
                library.rented_books[self.username] = {book_name: days_to_return}
            library.rented_books[self.username][book_name] = days_to_return

            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f"The book \"{book_name}\" is already rented and will be available in {library.rented_books[self.username][book_name]} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]

    def info(self):
        return ", ".join(sorted(self.books))