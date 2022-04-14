from typing import List, Tuple
"""
Reading Tracker 1.0.

Date: 2022 - 04 - 13.

Author:Li Junlu

Description: This program works as a reading tracker that helps the user
to know which book is required to read and they haven't done it yet.

Basic logic explanation: My program is highly rely on methods. As you can see 
methods almost took all the places here while the main program body only took 
a little..

Precondition: Each line of the csv file where the book information is stored
has to follow the following format -->  TITLE, AUTHOR, PAGES, IF IT'S REQUIRED 
For the last one, in this program, we use 'c' to indicate that a book
is completed and 'r' to indicate that a book is required.
----------------------------------------------------------------------------
Violating the precondition will result in this program being crashed.
----------------------------------------------------------------------------

"""
def f01(x: List) -> Tuple:
    """This function will return a tuple which contains three numbers.
    num1 -> The longest length among all the book titles.
    num2 -> The longest length among all the author names.
    num3 -> The longest number among all the book pages.
    """
    b1 = 0  # Initialize a variable.
    b2 = 0
    b3 = 0
    for i in x:  # This for loop will serve to look for the longest length
        # among all the book titles
        if len(i[0]) > b1:
            b1 = len(i[0])
    for i2 in x:  # This for loop will serve to look for The longest length
        # among all the author names.
        if len(i2[1]) > b2:
            b2 = len(i2[1])
    for i3 in x:  # This for loop will serve to look for The longest number
        # among all the book pages.
        if len(i3[2].strip('\n')) > b3:
            b3 = len(i3[2].strip('\n'))

    return b1 + 4, b2 + 1, b3  # Return the result.


def f0(x: str) -> List:
    """
    Return a list based on the content of the given dictionary path.
    This function serves as a file reader.
    """
    c1 = open(x, 'r')
    c2 = c1.readline()
    l1 = []  # Initialize an empty list.
    while c2 != '':  # I read the whole file by using while loop.
        c3 = c2.split(',')
        l1 += [c3]
        c2 = c1.readline()
    c1.close()
    return l1   # Return the final list.


def f1(x: str, y: List, z: str) -> bool:
    """Return True if and only if the user chooses to quit and also this
     function print something to lead the user through this program.
    """
    try:  # To try to run this following codes based on the user's input.
        if x.upper() not in ['L', 'A', 'M', 'Q']:
            print('Invalid menu choice')
        elif x.upper() == 'Q':
            t1 = open(z, 'w')
            for i in y:
                t2 = ''
                for i2 in range(4):
                    if i2 == 3:
                        t2 = t2 + i[i2]
                    else:
                        t2 = t2 + i[i2] + ','
                t1.write(t2)
            t1.close()
            print(f'{len(y)} books saved to {z}')
            return True
        elif x.upper() == 'L':
            f2(y)
    except SyntaxError and AttributeError:  # In case the user inputs a number
        #  which will raise a AttributeError because of x.upper()
        #  Since a number doesn't have upper() as it's attribute.
        print('Invalid menu choice')


def f2(l0: List) -> None:
    """Print a string based on the content of the given list in a particular
    formatting."""
    c0 = 1   # Initialize a variable. This one represents the order of books.
    #  So it starts at 1 to indicate the first book. and so on......
    r00 = 0  # Initialize a variable. This one represents the total page that
    #  the user needs to read in total, so it starts at 0 and will be increased
    #  during the following codes.
    r01 = 0  # Initialize a variable. This one represents the total number of
    #  required books that the users need to read.
    l1 = []  # Initialize a variable. This one represents a list which will be
    #  updated during the following codes. Finally, we use this list to output
    #  something.
    for i in l0:
        if i[3].strip('\n') == 'r':
            c1 = f'*{c0}. '
            for i2 in range(3):
                if i2 == 1:
                    c1 += (f01(l0)[0] - len(c1) + 1) * ' ' + 'by ' + i[i2] + ' '
                elif i2 == 2:
                    c1 += ((f01(l0)[0] + f01(l0)[1]) + 4 - len(c1)) * ' '\
                          + (f01(l0)[2] - len(i[i2])) * ' ' + i[i2] + ' pages '
                    r00 += int(i[i2])
                    r01 += 1
                    #  Codes above may look complicated but only serve to make
                    #  sure that the output is clean.
                else:
                    c1 += i[i2] + ' '
            l1 += [c1]
        else:
            c1 = f' {c0}. '
            for i2 in range(3):
                if i2 == 1:
                    c1 += (f01(l0)[0] - len(c1) + 1) * ' ' + 'by ' + i[i2] + ' '
                elif i2 == 2:
                    c1 += ((f01(l0)[0] + f01(l0)[1]) + 4 - len(c1))*' ' +\
                          + (f01(l0)[2] - len(i[i2])) * ' ' + i[i2] + ' pages '
                    #  Codes above may look complicated but only serve to make
                    #  sure that the output is clean.
                else:
                    c1 += i[i2] + ' '
            l1 += [c1]
        c0 += 1
    if r01 == 0:
        l1 += ['No books left to read. Why not add a new book?']
    else:
        l1 += [f'you need to read {r00} pages in {r01} books.']
    for i3 in l1:  # We output the content of l1 as I described in the
        # beginning.
        print(i3)
    return None


def f3(x: List) -> List:
    """
    Add a new book(x) to the tracker.
    This function also checks if the user inputs a valid answer.
    """
    n0 = 0  # This variable indicates the step of storing a book.
    # 1 --> store it's title.
    # 2 --> store it's author.
    # 3 --> store it's pages.
    # when n0 == 0, the following while loop will stop.
    l1 = []
    while n0 != 3:  # As described above.
        if n0 == 0:  # The first step.
            n1 = input('Title: ')
            while not n1:
                n1 = input('Input can not be blank\nTitle: ')
            l1 += [n1]
            n0 += 1
        elif n0 == 1:  # The second step.
            n2 = input('Author: ')
            while not n2:
                n2 = input('Input can not be blank\nAuthor: ')
            while n2.isnumeric():
                n2 = input('Input can not a number\nAuthor: ')
            l1 += [n2]
            n0 += 1
        elif n0 == 2:  # The third step.
            m0 = True
            while m0:
                try:
                    n3 = int(input('Pages: '))
                    while n3 <= 0:
                        n3 = int(input('Number must be > 0\nPages: '))
                    l1 += [str(n3)]
                    n0 += 1
                    print(f'{l1[0]} by {l1[1]},  ({int(l1[2])} pages) added '
                          f'to Reading Tracker')
                    m0 = False
                except ValueError:
                    print('Invalid input; enter a valid number')
    l1 += ['r\n']
    return x + [l1]  # Return the result.


def f4(x: List) -> List:
    """
    Return a List which is updated.
    This function will be called when the user choose to mark a book
    as completed.
    """
    m2 = 0  # This variable indicates that how many books that are
    # required reading.
    for i in x:  # I use a for loop to see how many books that are
        # required reading.
        if i[3].strip('\n').upper() == 'R':
            m2 += 1
    if m2 == 0:  # If there is no books that are required reading.
        #  Then the program will remind the user.
        print('No required books')
        return x
    f2(x)  # I first output the current book list.
    # I didn't use f2(x) because that f2(x) will remind the user how many books
    # are left for them to read which violates the style as specified in the
    # assignment examples.
    m0 = input('Enter the number of a book to mark as completed\n')
    m1 = True
    while m1:  # While m1 is ture, run this following codes.
        try:  # In case that a user inputs a str. Which will make int(m0) fail.
            while int(m0) <= 0 or int(m0) > len(x):
                #  All codes here are to check if the user inputs a
                #  valid answer.
                if int(m0) <= 0:
                    m0 = input('Number must be > 0\n')
                elif int(m0) > len(x):
                    m0 = input('Invalid book number\n')
            if x[int(m0) - 1][3].strip('\n').upper() == 'C':
                print('That book is already completed')
                #  All codes here are to check if the user inputs a
                #  valid answer.
                return x
            else:
                assert x[int(m0) - 1][3].strip('\n').upper() == 'R'
                x[int(m0) - 1][3] = 'c\n'
                print(f'{x[int(m0) - 1][0]} by {x[int(m0) - 1][1]} completed!')
                #  Remind the user that they completed a book.
                return x
        except ValueError:  # In case that a user inputs str. We remind them
            # to input a valid answer.
            m0 = input('Invalid input; enter a valid number\n')


def f5(x: str) -> bool:
    """Return ture if and only if x.upper() is in ['A', 'M'] .
    """
    try:  # This function is simple.
        if x.upper() in ['A', 'M']:  # If the user's answer is in 'AM'.
            # This program will return true otherwise return False.
            return True
        else:
            return False
    except SyntaxError and AttributeError:
        return False


r0 = 'books.csv'  # This is the dictionary path of the csv file. Can change this
# in order to load books from another file.
r1 = 'Li Junlu.'
_l1 = f0(r0)  # I first read the given file and form a list.
print(f'Reading Tracker 1.0 - by {r1}\n{len(_l1)} books loaded')
# Output a string to remind the user how many books are loaded.
r2 = f'Menu:\nL - List all books\nA - Add new book\nM - Mark a book as' \
     f' completed\nQ - Quit\n'
# r2 is just a str that outputs the menu.
r3 = input(r2)
# Ask the user to input.
while f5(r3):  # While the user wants to add a book or mark a book.
    # The following codes will run.
    if r3.upper() == 'A':  # If the user wants to add a book.
        # I update _l1 by calling f3 which will serve the user to add a book.
        _l1 = f3(_l1)
        r3 = input(r2)
    elif r3.upper() == 'M':  # If the user wants to mark a book.
        # I update _l1 by calling f4 which will serve the user to mark a book
        # as completed.
        _l1 = f4(_l1)
        r3 = input(r2)
while not f1(r3, _l1, r0):  # While the user never choose to quit.

    r3 = input(r2)
    while f5(r3):  # While the user wants to add a book or mark a book.
        if r3.upper() == 'A':  # If the user wants to add a book.
            # I update _l1 by calling f3 which will serve the
            # user to add a book.
            _l1 = f3(_l1)
            r3 = input(r2)
        elif r3.upper() == 'M':  # If the user wants to mark a book.
            # I update _l1 by calling f4 which will serve the user to mark
            # a book as completed.
            _l1 = f4(_l1)
            r3 = input(r2)
# End of program.

