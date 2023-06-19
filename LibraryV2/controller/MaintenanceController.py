from database.db import cursor,connection

def maintenance(borrowedlimit):
    query = f'''
    UPDATE maintenance
    SET BorrowedLimit = {borrowedlimit}
    WHERE id = 1;
    '''
    cursor.execute(query)
    connection.commit()

def setborrowlimit():
    query = 'SELECT * FROM maintenance WHERE id = 1'
    cursor.execute(query)

    return cursor.fetchone()

setborrowlimit()[1]