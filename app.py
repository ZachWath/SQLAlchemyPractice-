from models import (Base, session, Book, engine)




# import models
# main menu -add , search , analysis , exit, view
# add books to database
# edit books
# delete books
# search books
# data cleaning 
# loop runs programe



if __name__ == '__main__':
    Base.metadata.create_all(engine)