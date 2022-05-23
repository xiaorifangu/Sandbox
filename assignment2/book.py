class Book:
    """This is the book class.
    """
    def __init__(self, title: str = '', author: str = '',
                 pages: int = 0, required: bool = False) -> None:
        """ To get a book, we need it's title and author and pages,
        and if it's required. Default value are above."""
        self.title = title  # To initialize this book's title.
        self.author = author  # To initialize this book's author.
        self.number_of_pages = pages  # To initialize this book's pages.
        self.is_completed = required  # To initialize if this book is required.

    def __str__(self) -> str:
        """ Simply return this book's
         title when print is called on this book. """
        return self.title

    def mark_completed(self) -> None:
        """ This method will change this book is
        _completed attribute to True which indicates that
         this book is completed."""
        self.is_completed = True  # To set this book'
        # s is_completed value to True.

    def mark_required(self) -> None:
        """ This method will change this book is
        _completed attribute to False which indicates that
         this book is required reading. """
        self.is_completed = False  # To set is_completed to False.

    def is_long(self) -> bool:
        """ This method will return if this book is
        considered long. (pages >= 500.)"""
        return self.number_of_pages >= 500  # Return a bool.

    def f1(self):
        """ This method will return a string which is formatted
         as same as a book in the csv file"""
        if self.is_completed:  # If this book is completed.
            # The following code will be run.
            return f'{self.title},{self.author},{self.number_of_pages},c'
            # format a string and return it.
        else:  # if this book is not completed the following code will be run.
            return f'{self.title},{self.author},{self.number_of_pages},r'
            # format a string and return it.


