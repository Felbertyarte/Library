from database.db import cursor,connection

def borrowed_check():
    checker = f'''
    UPDATE book
    SET borrowed = CASE
        WHEN EXISTS (SELECT * FROM borrowedbook WHERE bookID = book.BID) THEN 0
        ELSE 1
    END;

    '''
    cursor.execute(checker)
    connection.commit()
def borrow(borrowerID,bookID,daylimit):
    addborrow = f'''
    INSERT INTO borrowedbook (bookID, borrowerID, issueDate, returnDate, daysLate)
    VALUES ({bookID}, {borrowerID}, CURRENT_DATE(), CURRENT_DATE() + INTERVAL {daylimit} DAY, 0);
    '''
    cursor.execute(addborrow)
    connection.commit()


def checklatereturn():
    timecheck = f'''
    UPDATE borrowedbook
    SET daysLate = DATEDIFF(CURRENT_DATE(), returnDate)
    WHERE returnDate < CURRENT_DATE();
    '''
    cursor.execute(timecheck)
    connection.commit()



