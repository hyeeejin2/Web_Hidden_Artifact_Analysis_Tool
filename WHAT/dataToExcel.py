import getpass
from pandas import DataFrame
from chormeCache import chromeCache
from chromeCookie import chromeCookie
from chromeHistory import chromeHistory
from chromeDownloadList import chromeDownloadList
from IECache import IECache
from IECookie import IECookie
from IEHistory import IEHistory
from IEDownloadList import IEDownloadList

userName=getpass.getuser()
path="C:\\Users\\%s\\Desktop\\" %userName

def chromeCacheToExcel():
    global path
    columns=['url','메타데이터 크기','데이터 크기','메타데이터 or 캐시 파일명','데이터 존재여부 or 캐시 파일명', '실제 데이터']
    data=DataFrame(chromeCache, columns=columns)
    data.to_excel(path+'chromeCacheData.xlsx',sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def chromeCookieToExcel():
    global path
    columns=['쿠키 이름','쿠키 생성 시간','쿠키 만료 시간','마지막 접근 시간']
    data=DataFrame(chromeCookie, columns=columns)
    data.to_excel(path+'chromeCookieData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def chromeHistoryToExcel():
    global path
    columns=['url','웹페이지 제목','방문 횟수','마지막 방문 시간']
    data=DataFrame(chromeHistory, columns=columns)
    data.to_excel(path+'chromeHistoryData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def chromeDownloadListToExcel():
    global path
    columns=['현재 경로','다운로드 데이터 크기','마지막 접근 시간','마지막 수정 시간','소스 url']
    data=DataFrame(chromeDownloadList, columns=columns)
    data.to_excel(path+'chromeDownloadListData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def IECacheToExcel():
    global path
    columns=['마지막 수정 시간','마지막 접속 시간','캐시 디렉터리 인덱스','url','캐시 파일명','http 헤더']
    data=DataFrame(IECache, columns=columns)
    data.to_excel(path+'IECacheData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def IECookieToExcel():
    global path
    columns=['마지막 수정 시간','마지막 접속 시간','쿠키 파일명']
    data=DataFrame(IECookie, columns=columns)
    data.to_excel(path+'IECookieData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def IEHistoryToExcel():
    global path
    columns=['url','방문 횟수','마지막 수정 시간','마지막 방문 시간']
    data=DataFrame(IEHistory, columns=columns)
    data.to_excel(path+'IEHistoryData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1

def IEDownloadListToExcel():
    global path
    columns=['마지막 접속 시간', '다운로드 데이터 크기','소스 url', '저장 경로']
    data=DataFrame(IEDownloadList, columns=columns)
    data.to_excel(path+'IEDownloadListData.xlsx', sheet_name='Sheet1', engine='xlsxwriter')
    return 1