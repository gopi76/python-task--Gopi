import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = 
    Select * from Customers;
    OUTER JOIN
    Select * from Orders;
    OUTER JOIN
    Select price*quantity from Order_Items;
    
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
