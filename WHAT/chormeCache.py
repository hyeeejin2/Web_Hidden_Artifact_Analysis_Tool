import getpass
import os
import glob

def countInit():
    global count
    count=0

def locationCalculation(blockIndex_, blockunit):
    blockIndex=int.from_bytes(blockIndex_,byteorder='little')
    location=(blockIndex*blockunit)+8192
    return location

def sizeCalculation(data):
    size=int.from_bytes(data,byteorder='little')
    return size

def fileNameCreate(data):
    temp=[]
    for n in range(len(data)):
        temp.append(str('{0:x}'.format(data[n])))
    temp.reverse()
    fileName="f_"+''.join(temp)
    if len(fileName)==8:
        return fileName
    else:
        add=8-len(fileName)
        string="f_"+"%s" %("0"*add)
        fileName=string+''.join(temp)
        return fileName

def urlFiltering(data):
    if chr(data[0])=='h'and chr(data[1])=='t'and chr(data[2])=='t'and chr(data[3])=='p':
        return 1
    else:
        return 0

def metaFiltering(data):
    temp=[]
    meta=""
    for i in range(len(data)):
        if data[i]>32 and data[i]<127:
            temp.append(chr(int(data[i])))
    meta="".join(temp)
    return meta

def main():
    userName=getpass.getuser()
    path="C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache" %userName

    count=0
    data=[]
    files = glob.glob(os.path.join(path, '*'))
    files.sort()
    for x in files:
        if os.path.isfile(x) and count<=3:
            try:
                f=open(files[count],'rb')
                data.append(f.read())
                count+=1
            except FileNotFoundError:
                print("데이터를 불러올 수 없습니다.")
        else:
            countInit()
            break
    f.close()

    URLRecordInfo=[]
    initialOffset=8192
    unit=36
    for i in range(int((len(data[0])-initialOffset)/unit)):
        URLRecordInfo.append(data[0][initialOffset+(24+(unit*i)):initialOffset+(28+(unit*i))])

    data_URLRecordLocation=[[],[],[]]
    for j in range(len(URLRecordInfo)):
        if URLRecordInfo[j][2]==1:
            data_URLRecordLocation[0].append(locationCalculation(URLRecordInfo[j][0:2], 256))
        elif URLRecordInfo[j][2]==2:
            data_URLRecordLocation[1].append(locationCalculation(URLRecordInfo[j][0:2], 1024))
        elif URLRecordInfo[j][2]==3:
            data_URLRecordLocation[2].append(locationCalculation(URLRecordInfo[j][0:2], 4096))
        else:
            continue

    URLRecordStructure=[]
    for a in range(1,4):
        if data_URLRecordLocation[a-1]==[]:
            continue
        for b in range(len(data_URLRecordLocation[a-1])):
            temp=[]
            urlSize = sizeCalculation(data[a][data_URLRecordLocation[a - 1][b] + 32:data_URLRecordLocation[a - 1][b] + 36])
            if urlSize!=0:
                result=urlFiltering(data[a][data_URLRecordLocation[a - 1][b] + 96:data_URLRecordLocation[a - 1][b] + 96+urlSize])
                if result==1:
                    url=data[a][data_URLRecordLocation[a - 1][b] + 96:data_URLRecordLocation[a - 1][b] + 96+urlSize]
                    temp.append(url.decode('utf-8'))
                elif result==0:
                    temp.append(None)
                    pass
            else:
                temp.append(None)

            metaSize=sizeCalculation(data[a][data_URLRecordLocation[a-1][b]+40:data_URLRecordLocation[a-1][b]+44])
            if metaSize!=0:
               temp.append(str(metaSize))
            else:
                temp.append(None)

            dataSize=sizeCalculation(data[a][data_URLRecordLocation[a-1][b]+44:data_URLRecordLocation[a-1][b]+48])
            if dataSize!=0:
                temp.append(str(dataSize))
            else:
                temp.append(None)

            if data[a][data_URLRecordLocation[a-1][b]+59]==128:
                filName=fileNameCreate(data[a][data_URLRecordLocation[a-1][b]+56:data_URLRecordLocation[a-1][b]+59])
                temp.append(str(filName))
            else:
                if data[a][data_URLRecordLocation[a-1][b]+58]==1:
                    metaLocation=locationCalculation(data[a][data_URLRecordLocation[a-1][b]+56:data_URLRecordLocation[a-1][b]+58], 256)
                    metadata=metaFiltering(data[1][metaLocation:metaLocation+metaSize+1])
                    temp.append(metadata)
                elif data[a][data_URLRecordLocation[a-1][b]+58]==2:
                    metaLocation = locationCalculation(data[a][data_URLRecordLocation[a-1][b] + 56:data_URLRecordLocation[a-1][b] + 58], 1024)
                    metadata=metaFiltering(data[2][metaLocation:metaLocation+metaSize+1])
                    temp.append(metadata)
                elif data[a][data_URLRecordLocation[a-1][b]+58]==3:
                    metaLocation = locationCalculation(data[a][data_URLRecordLocation[a-1][b] + 56:data_URLRecordLocation[a-1][b] + 58], 4096)
                    metadata=metaFiltering(data[3][metaLocation:metaLocation+metaSize+1])
                    temp.append(metadata)
                else:
                    temp.append(None)
                    pass

            if data[a][data_URLRecordLocation[a-1][b]+63]==128:
                filName=fileNameCreate(data[a][data_URLRecordLocation[a-1][b]+60:data_URLRecordLocation[a-1][b]+63])
                temp.append(str(filName))
            else:
                if data[a][data_URLRecordLocation[a-1][b]+62]==1:
                    dataLocation=locationCalculation(data[a][data_URLRecordLocation[a-1][b]+60:data_URLRecordLocation[a-1][b]+62], 256)
                    temp.append('data exist')
                    temp.append(data[1][dataLocation:dataLocation+dataSize+1])
                elif data[a][data_URLRecordLocation[a-1][b]+62]==2:
                    dataLocation = locationCalculation(data[a][data_URLRecordLocation[a-1][b] + 60:data_URLRecordLocation[a-1][b] + 62], 1024)
                    temp.append('data exist')
                    temp.append(data[2][dataLocation:dataLocation+dataSize+1])
                elif data[a][data_URLRecordLocation[a-1][b]+62]==3:
                    dataLocation = locationCalculation(data[a][data_URLRecordLocation[a-1][b] + 60:data_URLRecordLocation[a-1][b] + 62], 4096)
                    temp.append('data exist')
                    temp.append(data[3][dataLocation:dataLocation+dataSize+1])
                else:
                    temp.append(None)
                    pass
            URLRecordStructure.append(temp)
    return URLRecordStructure

chromeCache=main()