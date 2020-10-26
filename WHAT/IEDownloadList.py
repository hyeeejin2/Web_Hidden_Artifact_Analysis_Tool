import getpass
from datetime import datetime, timedelta

def locationCalculation(blockIndex):
    location = int.from_bytes(blockIndex, byteorder='little')
    return location

def activitySize(block):
    size = 128 * int.from_bytes(block, byteorder='little')
    return size

def sizeCalculation(data):
    size = int.from_bytes(data, byteorder='little')
    return size

def convertTime(data):
    nsTime = int.from_bytes(data, byteorder='little')
    time = (nsTime / 10 ** 7) - 11644473600
    standTime = datetime(1970, 1, 1)
    secondAfter = standTime + timedelta(seconds=time)
    UTC_9 = secondAfter + timedelta(hours=9)
    return UTC_9.strftime('%c')

def parsing(data):
    temp = []
    for i in range(1, int(len(data)) - 1):
        if data[i - 1] == 0 and data[i] == 0 and data[i + 1] == 0:
            temp.append(data[:i - 1])
            break
    return temp

def nullFiltering(data):
    temp = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            test = data[i][j]
            if test != 0:
                temp.append(chr(data[i][j]))
    filterData = "".join(temp)
    return filterData

def main():
    userName = getpass.getuser()
    path = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\IEDownloadHistory\\index.dat" % userName
    data = []
    f = open(path, "rb")
    data.append(f.read())
    f.close()

    activityRecord = []
    for i in range(int(len(data[0]) / 128)):
        if data[0][128 * i: (128 * i) + 4] == bytes([0x55, 0x52, 0x4C, 0x20]):
            size = activitySize(data[0][(128 * i) + 4: (128 * i) + 8])
            activityRecord.append(data[0][128 * i: (128 * i) + size])

    IEDownloadList = []
    for j in range(len(activityRecord)):
        temp = []
        accessed = convertTime(activityRecord[j][16:24])
        temp.append(accessed)
        dataSize = sizeCalculation(activityRecord[j][228:232])
        temp.append(str(dataSize))
        bufferOffset = sizeCalculation(activityRecord[j][52:56])
        url = parsing(activityRecord[j][52 + bufferOffset + 312:])
        urlFilter = nullFiltering(url)
        temp.append(urlFilter)
        path = parsing(activityRecord[j][52 + bufferOffset + 312 + len(url[0]) + 3:])
        pathFilter = nullFiltering(path)
        temp.append(pathFilter)
        IEDownloadList.append(temp)
    return IEDownloadList

IEDownloadList = main()