class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {} # {author:[title1, title2...]}
        self.rented_books = {} # ({usernames: {book names: days left}})

    def add_user(self, user):
        for u in self.user_records:
            if u == user:
                return f"User with id = {u.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        for u in self.user_records:
            if u.username == user.username:
                self.user_records.remove(user)
                # del self.rented_books[user.username]
                # self.books_available[author].append(book_name)
                return
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        for u in self.user_records:
            if u.user_id == user_id and u.username != new_username:
                u.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            elif u.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"