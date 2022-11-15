"""
:return: Instructions of library class,
:parameter: Requirements to make
            1. Lend a book method
                -- If a book is not present in the library then
                   return a statement that book is not present
                   in the library and also tells that, who owns
                   the book.

            2. Return a book method.
            3. Add a book method
            4. Display a book method
:method-template: Library(list-of-books, library_name)
:params: Run an infinite loop and get the information time to time

"""


class Library:
    _current_book_stock = 1000
    lend_books_from_library = 200
    no_of_books_returned = 300

    def __init__(self, _current_book_stock):
        self.book_stock = self._current_book_stock

    @property
    def current_book_stock(self):
        return self._current_book_stock


print(f"Welcome to my library we have currently {Library.current_book_stock} books.")
print("Choose any one option!")


def _main__func():
    print('''
    [1] - Lend a book
    [2] - Return a book
    [3] - Register as a student
    [4] - Add your own book 
    [5] - Get a details about any book.
    ''')

    choose__any_option = int(input("Which option you wanted to choose : "))

    if choose__any_option == 1:
        print("Which book do you want from library...!")
        name_of_lend_book = input("Enter book name > ")
        print(f"Okay, you taken {name_of_lend_book} on lend Please, return it after 10 days")
        print("bye")

    if choose__any_option == 2:
        print("Which book do you wanna return ?")
        name_of_return_book = input("Enter book name > ")
        print(f"Thanks, you returned {name_of_return_book} book on time")


_main__func()
