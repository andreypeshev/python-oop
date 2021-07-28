class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        for user in library.rented_books:
            for rented_books in library.rented_books[user]:
                if book_name == rented_books:
                    return f'The book "{book_name}" is already rented and will be available in {library.rented_books[user][book_name]} days!'

        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.rented_books[self.username] = {library.books_available[author].pop(library.books_available[author].index(book_name)): days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            library.books_available[author].append(book_name)
            library.rented_books[self.username].pop(book_name, None)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        ordered_books = sorted(self.books, reverse=False)
        return ", ".join(ordered_books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"



