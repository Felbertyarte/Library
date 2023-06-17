from database.db import cursor
import base64



def INPUT_ID(id):
    query = f'SELECT * from borrower WHERE borrower_id = {id}'
    cursor.execute(query)
    batch_size = 1000
    borrower = cursor.fetchmany(batch_size)
    items = []

    if not borrower:
        # Default values if borrower_id does not exist
        items.append((None, None, None, None, None, None, None, None))

    for row in borrower:
        id = row[0]
        firstname = row[1]
        lastname = row[2]
        email = row[3]
        phonenumber = row[4]
        Address = row[5]
        temp = row[6]
        course = row[7]
        avatar = base64.b64encode(temp).decode('utf-8')


        items.append((id,firstname,lastname,email,phonenumber,Address,avatar,course))
    return items