from database.db import cursor,connection
def Login (password):
    query=f'''
    SELECT * FROM admin_account WHERE ad_password = '{password}'
    '''
    cursor.execute(query)
    verify = cursor.fetchone()
    return verify
