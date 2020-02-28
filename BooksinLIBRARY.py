import sqlite3

def ConnectBookData():
    con = sqlite3.connect("allbooks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS allbooks (searchBookName text, myURL text)")
    con.commit()
    con.close()
    
def searchmyBook(bookName=""):
    con=sqlite3.connect("allbooks.db")
    cur = con.cursor()
    cur.execute("SELECT myURL FROM allbooks WHERE searchBookName=?",(bookName,))
    rows=cur.fetchone()
    con.close()
    return rows

ConnectBookData()
