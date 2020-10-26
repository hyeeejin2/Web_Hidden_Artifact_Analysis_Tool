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
    path="C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies" %userName

    db=sqlite3.connect(path)
    cursor=db.cursor()

    query="SELECT name, creation_utc, expires_utc, last_access_utc FROM cookies;"

    cursor.execute(query)
    data=cursor.fetchall()

    cursor.close()
    db.close()

    cookie=[]
    for row in data:
        temp=[]
        temp.append(row[0])
        temp.append(convertTime(row[1]))
        temp.append(convertTime(row[2]))
        temp.append(convertTime(row[3]))
        cookie.append(temp)

    return cookie

chromeCookie=main()

