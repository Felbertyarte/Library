from database.db import cursor,connection

def borrID(borrowerID):
    query = f'''
    SELECT borrowedbook.id, book.title, borrowedbook.issueDate, borrowedbook.returndate, borrowedbook.daysLate, borrower.firstname,
    borrower.lastname, borrower.email, borrower.phone_number, borrower.Address, borrower.Avatar, borrower.Course
    FROM borrowedbook
    JOIN book ON borrowedbook.bookID = book.BID
    JOIN borrower ON borrowedbook.borrowerID = borrower.borrower_id
    WHERE borrowedbook.borrowerID = {borrowerID}
    '''
    cursor.execute(query)
    Books = cursor.fetchall()
    return Books

def returnbook(ID):
    query2 = f'DELETE FROM borrowedbook WHERE id = {ID}'
    cursor.execute(query2)
    connection.commit()

# DELETE FROM books
# WHERE book_id = 1001;


# SELECT book.BID, book.title, book_category.title AS category_name, book.author, book.image, book.price
# FROM book
# JOIN book_category ON book.category_id = book_category.CID
# WHERE book.BID = {ID}
