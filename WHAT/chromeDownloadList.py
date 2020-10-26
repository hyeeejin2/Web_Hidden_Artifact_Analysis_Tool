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

    query="SELECT current_path, received_bytes, last_access_time, last_modified, tab_url FROM downloads;"

    cursor.execute(query)
    data=cursor.fetchall()

    cursor.close()
    db.close()

    down=[]
    for row in data:
        temp=[]
        temp.append(row[0])
        temp.append(str(row[1]))
        temp.append(convertTime(row[2]))
        temp.append(row[3])
        temp.append(row[4])
        down.append(temp)

    return down

chromeDownloadList=main()