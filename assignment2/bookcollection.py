from typing import TextIO
import os  # To determine if a path exists or not.
from book import Book  # In order to create a book object.


class BookCollection:
    """ This is the BookCollection class. """
    def __init__(self) -> None:
        """ To initialize a book. """
        self.books = []  # The default value for a book collection is empty.

    def load_books(self, x: str) -> None:
        """ This method will load file x into books. """
        if not os.path.exists(x):
            # If the given path doesn't exist, then just return None.
            return  # Return None.
        with open(x, 'r') as f:  # Open file as f.
            line = f.readline()  # Read the first line.
            while line != '':  # To reading all lines in the file.
                info = line.strip('\n').split(',')
                # info is just the information of a
                # book. such as author, pages..
                #  [Title, Author, Pages, r(c)]
                if info[3] == 'r':  # If the third value
                    # (if it's required reading or not.) is r which
                    # indicates that this book is required reading.
                    # Then the following code will be run.
                    book = Book(info[0], info[1], int(info[2]), False)
                    #  create a book with info.
                else:
                    # Which means that this book is completed.
                    assert info[3] == 'c'  # Assert in case we meet an error.
                    book = Book(info[0], info[1], int(info[2]), True)
                    # Create a book with info.
                self.books += [book]
                # Add this book to this book collection.
                line = f.readline()
                # Reading the next line.
        f.close()
        # Close the file.

    def save_books(self, x: str) -> None:
        """ Save this book collection into file (x). """
        with open(x, 'w') as f:  # Open this file as f.
            for i in self.books:  # For every book in this book collection.
                f.write(i.f1() + '\n')  # We write its info into this file (f).

    def add_book(self, x: Book) -> None:
        """ This method will simply add a book to this book collection. """
        self.books += [x]  # Add x (a Book object.) to this book collection.

    def get_required_pages(self) -> int:
        """ Return all the pages that are required reading. """
        n = 0  # Initialize a counter.
        for i in self.books:  # For every book in this book collection.
            if not i.is_completed:  # If this book is required reading.
                # The following code will be run.
                n += i.number_of_pages  # Increase the counter.
        return n  # Return the counter (n) which indicates
        # the total pages that are required reading.

    def sort(self, x: str) -> list:
        """ This method will return a list of book objects
        based on given sort method (x) """
        list0 = []  # Initialize a list.
        list1 = []  # Initialize a list.
        searched = []  # Initialize a list.
        if x == 'author':  # If sort by the name of authors.
            for e in self.books:
                list0 += [e.author]
            # The above for loop is to create a
            # list of names of every book in this book collection.
            list0.sort()
            # Sort this list which will give me a sorted name list.
            for j in list0:  # For every name in the sorted name list.
                for k in self.books:  # For every book in this book collection.
                    if k.author == j and k.title not in searched:
                        # If this book's author's name is j and this
                        # book haven't been searched, the
                        # following code will be run.
                        list1 += [k]  # We add this book in list1
                        # which follows the order of 'Author Sort'.
                        searched += [k.title]  # Add this book the list
                        # (searched.) to keep track of books that had been
                        # searched.
                        break  # If we find this book we break the for
                        # loop in order to be efficient.
            return list1  # Return this list1 which follows the 'Author Sort'.

        # Basically the same as 'Author Sort'
        elif x == 'title':
            for e in self.books:
                list0 += [e.title]
            list0.sort()
            for j in list0:
                for k in self.books:
                    if k.title == j and k.title not in searched:
                        list1 += [k]
                        searched += [k.title]
                        break
            return list1
        # Basically the same as 'Author Sort'
        elif x == 'pages':
            for e in self.books:
                list0 += [e.number_of_pages]
            list0.sort()
            for j in list0:
                for k in self.books:
                    if k.number_of_pages == j and k.title not in searched:
                        list1 += [k]
                        searched += [k.title]
                        break
            return list1
        # Basically the same as 'Author Sort'
        elif x == 'completed':
            for e in self.books:
                if not e.is_completed:
                    list1 += [e]
            for j in self.books:
                if j.is_completed:
                    list1 += [j]
            return list1

