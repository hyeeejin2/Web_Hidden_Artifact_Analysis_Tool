import getpass
from datetime import datetime, timedelta

def sizeCalc(block):
    size = 128 * int.from_bytes(block, byteorder='little')
    return size

def offsetCalc(blockIndex):
    offset = int.from_bytes(blockIndex, byteorder='little')
    return offset

def convertTime(Cookies):
    nsTime = int.from_bytes(Cookies, byteorder='little')
    time = (nsTime / 1e7) - 11644473600
    standTime = datetime(1970, 1, 1)
    secondAfter = standTime + timedelta(seconds=time)
    UTC_9 = secondAfter + timedelta(hours=9)
    return UTC_9.strftime('%Y-%m-%d %H:%M:%S')

def filtering(data):
    temp = []
    for n in range(len(data)):
        if 32 < data[n] and data[n] < 127:
            temp.append(chr(data[n]))
        else:
            continue
    name = "".join(temp)
    return name


def main():
    userName = getpass.getuser()
    path = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Cookies\\index.dat' % userName
    Cookies = []

    with open(path, 'rb') as f:
        Cookies.append(f.read())

    activityRecord = []
    for i in range(int(len(Cookies[0]) / 128)):
        if Cookies[0][128 * i:(128 * i) + 4] == bytes([0x55, 0x52, 0x4C, 0x20]):
            size = sizeCalc(Cookies[0][(128 * i) + 4:(128 * i) + 8])
            activityRecord.append(Cookies[0][128 * i:(128 * i) + size])

    activityRecordData = []
    for j in range(len(activityRecord)):
        temp = []
        modifiedTime = convertTime(activityRecord[j][8:16])
        temp.append(modifiedTime)
        accessedTime = convertTime(activityRecord[j][16:24])
        temp.append(accessedTime)
        filenameOffset = offsetCalc(activityRecord[j][52:56])
        fileName = activityRecord[j][filenameOffset:]
        parsing = filtering(fileName)
        temp.append(parsing)
        activityRecordData.append(temp)
    return activityRecordData

IECookie = main()