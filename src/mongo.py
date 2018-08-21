import pymongo
from pymongo import MongoClient
import datetime

class MyMongoClient:
    def __init__(self, host: str="localhost", port: int=27017):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)

    def get_db(self, name):
        return self.client[name]

class BookManager():

    def print_book(book):
        print("{title}\n-----------\nvon {author} - {time}\n".format(
            title=book["title"],
            author=book["author"],
            time=book["time_create"].year,
            ))

    def __init__(self, mongo: MyMongoClient):
        self.db = mongo.get_db("bookshop")
        self.books = self.db.books

    def _create_book(self, author, title, genre):
        book = {"author": author,
                "title": title,
                "genre": genre,
                "time_create": datetime.datetime.utcnow()}
        book["_id"] = self.books.insert(book)
        return book

    def _get_first_book(self):
        return self.books.find_one()

    def _get_all_books(self):
        return self.books.find()

    def _delete_all_books(self):
        self.books.drop()

    def create_book(self):
        author = input("Author: ")
        title = input("Title: ")
        genre = input("Genre: " )
        return self._create_book(author, title, genre)

    def list_all_books(self):
        for book in self._get_all_books():
            BookManager.print_book(book)

    def show_first_book(self):
        BookManager.print_book(self._get_first_book())

    def delete_all_books(self):
        ask = input("Are you sure? (y/N)")
        if ask.lower() == "y":
            self._delete_all_books()
            print("All Books deleted!")
        else:
            print("No books deleted.")

    def get_menu(self):
        menu = []
        menu.append({"name": "Create Book", "func": self.create_book})
        menu.append({"name": "List all Books", "func": self.list_all_books})
        menu.append({"name": "Show first Book", "func": self.show_first_book})
        menu.append({"name": "Delete Books", "func": self.delete_all_books})
        return menu

    def run(self):
        _exit = False
        while not _exit:
            print("Available options:")
            cnt = 1
            menu = self.get_menu()
            for item in menu:
                print("{}. {}".format(cnt, item["name"]))
                cnt += 1
            cmd = int(input("> "))
            if cmd <= len(menu) and cmd > 0:
                menu[cmd-1]["func"]()
            else:
                _exit = True


if __name__ == "__main__":
    mongo = MyMongoClient()
    bk = BookManager(mongo)
    bk.run()
