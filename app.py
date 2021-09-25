from models import (Base, session, Book, engine)




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


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            pass
        elif choice == '2':
            # view books
            pass
        elif choice == '3':
            #Search for book
            pass
        elif choice == '4':
            #book analysis 
            pass
        else:
            print ('GOODBYE!!')
            app_running = False
            


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()