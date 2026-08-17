import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = Select email,Orders.order_date where Orders.status == 'Pending';

    
    
    cursor.execute(query)
    return cursor.fetchall()
