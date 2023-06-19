from database.db import cursor,connection

def deletebook(bookID):
    query = f'''
    DELETE FROM book
    WHERE BID = {bookID};
    '''
    cursor.execute(query)
    connection.commit()

def deleteborrower(borrrowerID):
    query2 = f'''
    DELETE FROM borrower
    WHERE borrower_id = {borrrowerID};
    '''
    cursor.execute(query2)
    connection.commit()
