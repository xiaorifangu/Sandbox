from kivy.app import App
from kivy.app import Builder
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from book import Book
from bookcollection import BookCollection
b0 = BookCollection()  # Initialize a BookCollection object.
file_name = 'books.csv'  # Change this file name in order
# to load books from another csv file.
b0.load_books(file_name)
# Load books from file_name.
"""
This is my reading tracker 2.0 which classes got involved. I used kivy to 
generate an user interface to keep track of books which is more elegant and 
efficient. 

    Precondition:
        app.kv must exists to make sure this program can work. However, csv file 
        can be omitted in which case a new file will be generated when user shut
        the program. 
"""


class ReadingTrackerApp(App):
    """This is the main app."""
    current_sort = StringProperty()  # This is the current sort method.
    sort_list = ListProperty()  # This is the options of sort method.

    def __init__(self, **kwargs) -> None:
        """To give a attribute to self. --> books. """
        super().__init__(**kwargs)
        self.books = b0.books  # Give an value to self.books.

    def build(self) -> None:
        """ The main method to build my GUI."""
        self.title = 'Reading Tracker 2.0'  # This is the name of my window.
        self.root = Builder.load_file('app.kv')  # This is the root.
        self.current_sort = 'Author'  # The default sort method is by author.
        self.sort_list = ['Author', 'Title', 'Pages', 'Completed']
        # Above is a list of sort options.
        self.updated_book_list = b0.books
        # To keep track of new added books.
        # for i in range(5):
        #     self.root.ids['id01'].add_widget(Button(text='Button' + str(i)))
        self.add_widgets()
        # self.root.ids['spin'].bind(on_text = self.sort)
        return self.root  # Return self.root.

    def add_widgets(self) -> None:
        """ This method will build two
        labels on the right_top and right_bottom where the first label
         will tell the user how many pages are required reading
         and the second will output some messages of this program. """
        if not self.books:  # If there is no books which can only be
            # the case where books.csx doesn't exist,
            # the following code will be run.
            self.root.ids['to_read'].text = 'Pages to read:' + str(0)
            # ID to_read indicates the right_top label.
            # I assign a new value to its text value.
            self.root.ids['output'].text = 'welcome to Reading Tracker 2.0.' \
                                           ' Unable to load books.csv'
            # ID output indicates the right_bottom label,
            # and I assign a new value to its text value.
        else:  # If there are at least one book exists then
            # the following code will be run.
            self.root.ids['to_read'].text = 'Pages to read:' + \
                                            str(b0.get_required_pages())
            # Same as above.
            self.root.ids['output'].text = 'welcome to Reading Tracker 2.0.'
            # Same as above.

    def clear(self) -> None:
        """ This method will be called when the clear button is pressed. """
        for i in range(1, 4):
            # The above for loop is just to be convenient.
            self.root.ids[f'Text0{i}'].text = ''
            # Clear all three TextInput widget.

    def press_book_button(self, b) -> None:
        """ This method will be called when any book button is pressed. """
        l0 = b.text.strip().split(',')
        # l0 is just a list that stores a book's information.
        title_01 = l0[0]
        # l0[0] is the title of a book, and I assign it to title_01.
        if b.background_color == [1, 1, 1, 1]:  # Changed to uncompleted.
            for i in self.updated_book_list:  # For every book in the book list.
                if i.title == title_01:
                    # If its title == itle_01 Then
                    # the following code will be run.
                    i.is_completed = False
                    # Set its is_completed value to False
                    # which indicates that this book is required reading.
                    if i.is_long():
                        # If this book is a long book
                        # then the following code will be run.
                        self.root.ids['output'].text = f'You need' \
                                                       f' to read' \
                                                       f' {i.title}.' \
                                                       f' Get started!'
                        # To output a string.
                    else:  # If this book is a short book, the
                        # following code will be run.
                        self.root.ids['output'].text = f'You need ' \
                                                       f'to read {i.title}.'
                        # To output a string.
            b.background_color = [0, 1, 1, 1]
            # Change it's background color.
            self.sort(self.root.ids['spin'])
        else:  # Change to complete.
            # Basically the same as above.
            assert b.background_color == [0, 1, 1, 1]
            for i in self.updated_book_list:
                if i.title == title_01:
                    i.is_completed = True
                    if i.is_long():
                        self.root.ids['output'].text = f'You ' \
                                                       f'completed{i.title}' \
                                                       f'. Great job!'
                    else:
                        self.root.ids['output'].text = f'You completed' \
                                                       f'{i.title}.'
            b.background_color = [1, 1, 1, 1]
            self.sort(self.root.ids['spin'])
        self.root.ids['to_read'].text = f'Pages to rea' \
                                        f'd:{b0.get_required_pages()}'

    def sort(self, current) -> None:
        """ This method will re-format the booklist widget and
         will be called when the user choose to change sore method.  """
        if current.text.lower() == 'author':
            # If the user choose to sort based on author's name,
            # Then the following code will be run.
            self.root.ids['book_list'].clear_widgets()
            # I first clear the book list widget.
            self.load_book_01(b0.sort('author'))
            # Then I reload the book list widget.
        elif current.text.lower() == 'title':
            # basically the same as above.
            self.root.ids['book_list'].clear_widgets()
            self.load_book_01(b0.sort('title'))
        elif current.text.lower() == 'pages':
            # basically the same as above.
            self.root.ids['book_list'].clear_widgets()
            self.load_book_01(b0.sort('pages'))
        elif current.text.lower() == 'completed':
            # basically the same as above.
            self.root.ids['book_list'].clear_widgets()
            self.load_book_01(b0.sort('completed'))

    def load_book_01(self, l0) -> None:
        """ This method will be called to create
         a button for every book object in the book collection. """
        for i in l0:  # For every book in list (l0).
            if i.is_completed:  # If it's completed then
                # the button will be assigned a unique color.
                b = Button(text=f'{i.title},by {i.author}, {i.number_of_pages} '
                                f'pages (completed)',
                           background_color=(1, 1, 1, 1))
                # Create a button with a specific color.
                b.bind(on_press=self.press_book_button)
                # When it's pressed then the method
                # self.press_book_button will be called.
            else:
                # basically the same as above.
                assert not i.is_completed
                b = Button(text=f'{i.title},by {i.author}, {i.number_of_pages} '
                                f'pages', background_color=(0, 1, 1, 1))
                b.bind(on_press=self.press_book_button)
            self.root.ids['book_list'].add_widget(b)

    def add_book(self) -> None:
        """ This method will add a book into the book list widget. """
        for i in range(1, 4):  # This for loop is just for convenience.
            if not self.root.ids[f'Text0{i}'].text:
                # If the 'Add Book' Button is pressed and
                # any of the three TextInput widget remains empty
                # the following code will be run.
                self.root.ids['output'].text = 'All fields must be completed'
                # Output a message to remind the user.
                return # Stop this method.
        if not self.root.ids['Text03'].text.strip('-').isnumeric():
            # If the user didn't input a number for a book's page,
            # The following code will be run.
            self.root.ids['output'].text = 'Please enter a valid number'
            # To output a message to remind the user.
            return  # Stop this method.
        if int(self.root.ids['Text03'].text) <= 0:
            # If the user inputted a negative number or 0 for
            # a book's pages, the following code will be run.
            self.root.ids['output'].text = 'Pages must be > 0'
            # To output a message to remind the user.
            return  # Stop this method.
        # If all the information entered by the user for
        # a book object is correct, the following code will be run.
        book = Book(self.root.ids['Text01'].text,
                    self.root.ids['Text02'].text,
                    int(self.root.ids['Text03'].text), False)
        # Create a book object.
        b0.add_book(book)
        # Add this book to the book collection.
        self.sort(self.root.ids['spin'])
        # By calling the self.sort() the book list widget will be re-formatted.
        self.root.ids['to_read'].text = 'Pages to read:' + \
                                        str(b0.get_required_pages())
        # Update the total pages that are required reading and output
        # it by updating the text value of the right_top label.
        for i in range(1, 4):
            self.root.ids[f'Text0{i}'].text = ''
        # The above for loop will clear all three TextInput widget.

    def on_stop(self) -> None:
        """ This method will be called when the user chooses
         to exit this program and will update the csv
          file based on the user's actions. """
        l0 = []  # Initialize an empty list.
        for i in b0.books:
            l0 += [i.f1() + '\n']
        # The above for loop will create a
        # list where values inside it are information of books.
        with open(file_name, 'w') as f:
            # Open the file as f.
            for e in l0:
                # For every information in the list.
                f.write(e)
                # Write it to the file.
        f.close()
        # Close the file.


if __name__ == '__main__':  # If this python file is the
    # main window, the following code will be run.
    ReadingTrackerApp().run()
    # Run the app.


# End of program.
