import getpass
import sqlite3
import datetime
from datetime import timedelta

def convertTime(data):
    epoch_start=datetime.datetime(1601,1,1)
    delta=datetime.timedelta(microseconds=int(data))
    UTC_9=epoch_start+delta+timedelta(hours=9)
    return UTC_9.strftime('%c')

def main():
    userName=getpass.getuser()
    path="C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History" %userName

    db=sqlite3.connect(path)
    cursor=db.cursor()

    query="SELECT url, title, visit_count, last_visit_time FROM urls;"

    cursor.execute(query)
    data=cursor.fetchall()

    cursor.close()
    db.close()

    history=[]
    for row in data:
        temp=[]
        temp.append(row[0])
        temp.append(row[1])
        temp.append(str(row[2]))
        temp.append(convertTime(row[3]))
        history.append(temp)

    return history

chromeHistory=main()