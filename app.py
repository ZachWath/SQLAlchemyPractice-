from models import (Base, session, Book, engine)
import datetime
import csv
import time



def menu():
    while True:
        print('''
            \nProgramming Books:
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book analysis
            \r5) exit''')
        choice = input ('What would you like to do?   ')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''please choose one of the options above.
                    A number 1-5
                    press enter to try again   ''')
# main menu -add , search , analysis , exit, view
# add books to database
# edit books
# delete books
# search books
# data cleaning 
# loop runs programe

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
            \n***** DATE ERROR *****
            \r The date format should include a valid month day and year from the past
            \r EX: January 13, 2003
            \r Press enter to try again
            \r ************************''')
        return 
    else:
        return return_date



def clean_price(price_str):
    try:
        price_float = float(price_str)
        
    except ValueError:
        input('''
        \n***** PRICE ERROR ******
        \r the price format should be a number without a currency symbol
        \r EX: 10.99
        \r Press enter to try again
        \r************************''')
    else:
        return int(price_float * 100)

def clean_id(id_str, options):
    try:
        book_id = int(id_str)
    except ValueError:
        input('''
            \n***** ID ERROR *****
            \r The ID format should be a number
            \r Press enter to try again
            \r ************************''')
        return
    else:
        if book_id in options:
            return book_id
        else:
            input(f'''
            \n***** ID ERROR *****
            \r Options: {options}
            \r Press enter to try again
            \r ************************''')
        return

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author= author, published_date= date, price= price)
                session.add(new_book)
        session.commit()





def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: October 25, 2017):  ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error= False
            price_error = True
            while price_error:
                price = input('Price (Ex: 25.64):  ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, published_date=date, price=price)
            session.add(new_book)
            session.commit()
            print('Book added')
            time.sleep(1.5)
        elif choice == '2':
            for book in session.query(Book):
                print(f'{book.id}  |  {book.title}  |  {book.author}  |  {book.published_date}  |  {book.price}')
            input ('\nPress enter to return to the main menu...  ')
        elif choice == '3':
            #Search for book
            id_options = []
            for book in session.query(Book):
                id_options.append(book.id)
            id_error = True
            while id_error:
                id_choice = input(f'''
                \nID Options: {id_options}
                \rBook ID:   ''')
                id_choice = clean_id(id_choice, id_options)
                if type(id_choice) == int:
                    id_error = False
            the_book = session.query(Book).filter(Book.id==id_choice).first()
            print(f'''
            \n{the_book.title} by {the_book.author}
            \rPublished: {the_book.published_date}
            \rPrice: ${the_book.price / 100}''')
            time.sleep(1.5)
            input('\nPress enter to return to the main menu...  ')
        elif choice == '4':
            #book analysis 
            pass
        else:
            print ('GOODBYE!!')
            app_running = False
            


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()
    

    for book in session.query(Book):
        print(book)
    

    
