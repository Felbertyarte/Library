from database.db import cursor,connection

def AddBook(title,categoty,author,image_path,price,qty):
    with open(image_path, 'rb') as file:
        blob_data = file.read()
    for i in range(int(qty)):
        query = f'''
        INSERT INTO book (title, category, author, image, price)
        VALUES ('{title}', '{categoty}', '{author}',(%s), {price})
        '''
        cursor.execute(query, (blob_data,))
    connection.commit()
    getid = f'''
    SELECT BID, title
    FROM book
    ORDER BY BID DESC
    LIMIT {int(qty)};
    '''
    cursor.execute(getid)

    # Check for any warnings
    warnings = cursor.fetchwarnings()
    if warnings:
        print("MySQL Warnings:", warnings)
    return cursor.fetchall()


def AddBorrower(fname,lname,email,pnumber,address,avatar_path,course):
    with open(avatar_path, 'rb') as file:
        blob_data = file.read()

    query = f'''
    INSERT INTO borrower (firstname,lastname,email,phone_number,Address,Avatar,Course)
    VALUES ('{fname}','{lname}','{email}','{pnumber}','{address}',(%s),'{course}')
    '''
    cursor.execute(query, (blob_data,))
    connection.commit()
    borrowerID = cursor.lastrowid
    return borrowerID