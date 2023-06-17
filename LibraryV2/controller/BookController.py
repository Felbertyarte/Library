from database.db import cursor
def Books(ID):
    query = f'SELECT * from book WHERE BID = {ID} AND book.borrowed'
    cursor.execute(query)
    book = cursor.fetchone()
    return book if book else (None,None,None,None,None,None)

# SELECT b.BID, b.title, c.name AS category_name, b.author, b.image, b.price
# FROM book b
# JOIN book_category c ON b.category_id = c.CID
# WHERE b.BID = 10245;