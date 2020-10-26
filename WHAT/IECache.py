import getpass
from datetime import datetime, timedelta

def locationCalculation(blockIndex):
    location = int.from_bytes(blockIndex, byteorder='little')
    return location

def sizeCalculation(block):
    size = 128 * int.from_bytes(block, byteorder='little')
    return size

def convertTime(data):
    nsTime = int.from_bytes(data, byteorder='little')
    time = (nsTime / 1e7) - 11644473600
    standTime = datetime(1970, 1, 1)
    secondAfter = standTime + timedelta(seconds=time)
    UTC_9 = secondAfter + timedelta(hours=9)
    return UTC_9.strftime('%c')

def parsing(data):
    temp = []
    for n in range(len(data)):
        if data[n] == 0:
            temp.append(data[:n])
            break
    return temp

def main():
    userName = getpass.getuser()
    path = "C:\\Users\\%s\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files\\Content.IE5\\index.dat" % userName
    data = []
    f = open(path, 'rb')
    data.append(f.read())
    f.close()

    activityRecord = []
    for i in range(int(len(data[0]) / 128)):
        if data[0][128 * i:(128 * i) + 4] == bytes([0x55, 0x52, 0x4C, 0x20]):
            size = sizeCalculation(data[0][(128 * i) + 4:(128 * i) + 8])
            activityRecord.append(data[0][128 * i:(128 * i) + size])

    activityRecordData = []
    for j in range(len(activityRecord)):
        temp = []
        modified = convertTime(activityRecord[j][8:16])
        temp.append(modified)
        accessed = convertTime(activityRecord[j][16:24])
        temp.append(accessed)
        directoryIndex = int(activityRecord[j][56])
        temp.append(str(directoryIndex))
        urlLocation = locationCalculation(activityRecord[j][52:56])
        fileLocation = locationCalculation(activityRecord[j][60:64])
        httpLocation = locationCalculation(activityRecord[j][68:72])
        url = parsing(activityRecord[j][urlLocation:fileLocation])
        temp.append(url[0].decode('utf-8'))
        fileName = parsing(activityRecord[j][fileLocation:httpLocation])
        if fileName!=[]:
            temp.append(fileName[0].decode('utf-8'))
        else:
            temp.append(None)
        httpHeader = parsing(activityRecord[j][httpLocation:])
        if httpHeader!=[]:
            temp.append(httpHeader[0].decode('utf-8'))
        else:
            temp.append(None)
        activityRecordData.append(temp)
    return activityRecordData

IECache = main()