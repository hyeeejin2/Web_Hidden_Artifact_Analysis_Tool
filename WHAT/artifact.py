import sys
import chromeStatistic
import IEStatistic
import dataToExcel
from chormeCache import chromeCache
from chromeCookie import chromeCookie
from chromeHistory import chromeHistory
from chromeDownloadList import chromeDownloadList
from IECache import IECache
from IECookie import IECookie
from IEHistory import IEHistory
from IEDownloadList import IEDownloadList
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("main.ui")[0]
form_class2=uic.loadUiType("parsing.ui")[0]

class mainWindow(QMainWindow, form_class):
    count=0
    check=[0,0,0,0,0,0,0,0]
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)

        self.groupBox.setStyleSheet('border: 3px solid #000000; border-radius: 10px; font:75 12pt "Dotum.ttf";')
        self.groupBox_2.setStyleSheet('border: 3px solid #000000; border-radius: 10px; font:75 12pt "Dotum.ttf";')

        self.groupBox_3.hide()
        self.groupBox_4.hide()

        self.pushButton.clicked.connect(self.btn_Chrome)
        self.pushButton.setStyleSheet('Image:url(chrome.png); border:None;')
        self.pushButton_2.clicked.connect(self.btn_Ie)
        self.pushButton_2.setStyleSheet('Image:url(IE07.png); border:None;')
        self.pushButton_3.clicked.connect(self.btn_parsing)

        self.checkBox.stateChanged.connect(self.checkBoxState)
        self.checkBox_2.stateChanged.connect(self.checkBox_2State)
        self.checkBox_3.stateChanged.connect(self.checkBox_3State)
        self.checkBox_4.stateChanged.connect(self.checkBox_4State)
        self.checkBox_5.stateChanged.connect(self.checkBox_5State)
        self.checkBox_6.stateChanged.connect(self.checkBox_6State)
        self.checkBox_7.stateChanged.connect(self.checkBox_7State)
        self.checkBox_8.stateChanged.connect(self.checkBox_8State)

    def btn_Chrome(self):
        self.groupBox_3.show()

    def btn_Ie(self):
        self.groupBox_4.show()
        
    def btn_parsing(self):
        if mainWindow.count==0:
            QMessageBox.about(self, "알림", "아티팩트를 선택해주세요.")
        else:
            self.close()
            self.parsingWindow=parsingWindow(self)
            self.parsingWindow.show()
    def checkBoxState(self):
        if self.checkBox.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[0]=1
        elif self.checkBox.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[0]=0
    def checkBox_2State(self):
        if self.checkBox_2.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[1]=1
        elif self.checkBox_2.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[1]=0
    def checkBox_3State(self):
        if self.checkBox_3.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[2]=1
        elif self.checkBox_3.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[2]=0
    def checkBox_4State(self):
        if self.checkBox_4.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[3]=1
        elif self.checkBox_4.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[3]=0
    def checkBox_5State(self):
        if self.checkBox_5.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[4]=1
        elif self.checkBox_5.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[4]=0
    def checkBox_6State(self):
        if self.checkBox_6.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[5]=1
        elif self.checkBox_6.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[5]=0
    def checkBox_7State(self):
        if self.checkBox_7.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[6]=1
        elif self.checkBox_7.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[6]=0
    def checkBox_8State(self):   
        if self.checkBox_8.isChecked() == True:
            mainWindow.count+=1
            mainWindow.check[7]=1
        elif self.checkBox_8.isChecked()==False:
            mainWindow.count-=1
            mainWindow.check[7]=0

class parsingWindow(QMainWindow, form_class2):
    browser=[0,0]
    def __init__(self, parent=None):
        super(parsingWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(800, 600)
        
        chromeCount=0
        ieCount=0
        for i in range(8):
            if i<4 and mainWindow.check[i]==1:
                chromeCount+=1
            elif i>=4 and mainWindow.check[i]==1:
                ieCount+=1

        if chromeCount==0 and ieCount!=0:
            self.ieView()
        elif ieCount==0 and chromeCount!=0:
            self.chromeView()
        elif chromeCount!=0 and ieCount!=0:
            self.chromeView()

        if mainWindow.check[0]==1:
            self.checkBox.setChecked(True)
            self.checkBoxState()
        if mainWindow.check[1]==1:
            self.checkBox_2.setChecked(True)
            self.checkBox_2State()
        if mainWindow.check[2]==1:
            self.checkBox_3.setChecked(True)
            self.checkBox_3State()
        if mainWindow.check[3]==1:
            self.checkBox_4.setChecked(True)
            self.checkBox_4State()
        if mainWindow.check[4]==1:
            self.checkBox_5.setChecked(True)
            self.checkBox_5State()
        if mainWindow.check[5]==1:
            self.checkBox_6.setChecked(True)
            self.checkBox_6State()
        if mainWindow.check[6]==1:
            self.checkBox_7.setChecked(True)
            self.checkBox_7State()
        if mainWindow.check[7]==1:
            self.checkBox_8.setChecked(True)
            self.checkBox_8State()

        self.actionChrome.triggered.connect(self.chromeView)
        self.actionInternet_Explorer.triggered.connect(self.ieView)
        self.actionstatistic.triggered.connect(self.historyStatistic)
        self.actionexcel.triggered.connect(self.dataToExcel)

        self.checkBox.stateChanged.connect(self.checkBoxState)
        self.checkBox_2.stateChanged.connect(self.checkBox_2State)
        self.checkBox_3.stateChanged.connect(self.checkBox_3State)
        self.checkBox_4.stateChanged.connect(self.checkBox_4State)
        self.checkBox_5.stateChanged.connect(self.checkBox_5State)
        self.checkBox_6.stateChanged.connect(self.checkBox_6State)
        self.checkBox_7.stateChanged.connect(self.checkBox_7State)
        self.checkBox_8.stateChanged.connect(self.checkBox_8State)

        self.pushButton.clicked.connect(self.btn_close)

    def chromeView(self):
        self.browser[0]=1
        self.browser[1]=0
        self.groupBox_2.hide()
        self.groupBox.show()
        self.frame_2.hide()
        self.frame.show()

    def ieView(self):
        self.browser[0]=0
        self.browser[1]=1
        self.groupBox.hide()
        self.groupBox_2.show()
        self.frame.hide()
        self.frame_2.show()

    def checkBoxState(self):
        if self.checkBox.isChecked() == True:
            self.chromeCacheOutput()
            mainWindow.check[0]=1
        elif self.checkBox.isChecked() == False:
            self.treeWidget.clear()
            mainWindow.check[0]=0

    def checkBox_2State(self):
        if self.checkBox_2.isChecked() == True:
            self.chromeCookieOutput()
            mainWindow.check[1]=1
        elif self.checkBox_2.isChecked() == False:
            self.treeWidget_2.clear()
            mainWindow.check[1]=0

    def checkBox_3State(self):
        if self.checkBox_3.isChecked() == True:
            self.chromeHistoryOutput()
            mainWindow.check[2]=1
        elif self.checkBox_3.isChecked() == False:
            self.treeWidget_3.clear()
            mainWindow.check[2]=0

    def checkBox_4State(self):
        if self.checkBox_4.isChecked() == True:
            self.chromeDownloadListOutput()
            mainWindow.check[3]=1
        elif self.checkBox_4.isChecked() == False:
            self.treeWidget_4.clear()
            mainWindow.check[3]=0

    def checkBox_5State(self):
        if self.checkBox_5.isChecked() == True:
            self.ieCacheOutput()
            mainWindow.check[4]=1
        elif self.checkBox_5.isChecked() == False:
            self.ieCache.clear()
            mainWindow.check[4]=0

    def checkBox_6State(self):
        if self.checkBox_6.isChecked() == True:
            self.ieCookieOutput()
            mainWindow.check[5]=1
        elif self.checkBox_6.isChecked() == False:
            self.ieCookie.clear()
            mainWindow.check[5]=0

    def checkBox_7State(self):
        if self.checkBox_7.isChecked() == True:
            self.ieHistoryOutput()
            mainWindow.check[6]=1
        elif self.checkBox_7.isChecked() == False:
            self.ieHistory.clear()
            mainWindow.check[6]=0

    def checkBox_8State(self):
        if self.checkBox_8.isChecked() == True:
            self.ieDownloadListOutput()
            mainWindow.check[7]=1
        elif self.checkBox_8.isChecked() == False:
            self.ieDownloadList.clear()
            mainWindow.check[7]=0
            
    def chromeCacheOutput(self):
        self.root=self.treeWidget.invisibleRootItem()
        for i in range(len(chromeCache)):
            item=QTreeWidgetItem()
            for j in range(len(chromeCache[i])-1):
                item.setText(j, chromeCache[i][j])
            self.root.addChild(item)

    def chromeCookieOutput(self):
        self.root=self.treeWidget_2.invisibleRootItem()
        for i in range(len(chromeCookie)):
            item=QTreeWidgetItem()
            for j in range(len(chromeCookie[i])):
                item.setText(j, chromeCookie[i][j])
            self.root.addChild(item)

    def chromeHistoryOutput(self):
        self.root=self.treeWidget_3.invisibleRootItem()
        for i in range(len(chromeHistory)):
            item=QTreeWidgetItem()
            for j in range(len(chromeHistory[i])):
                item.setText(j, chromeHistory[i][j])
            self.root.addChild(item)

    def chromeDownloadListOutput(self):
        self.root=self.treeWidget_4.invisibleRootItem()
        for i in range(len(chromeDownloadList)):
            item=QTreeWidgetItem()
            for j in range(len(chromeDownloadList[i])):
                item.setText(j, chromeDownloadList[i][j])
            self.root.addChild(item)

    def ieCacheOutput(self):
        self.root=self.ieCache.invisibleRootItem()
        for i in range(len(IECache)):
            item=QTreeWidgetItem()
            for j in range(len(IECache[i])):
                item.setText(j, IECache[i][j])
            self.root.addChild(item)

    def ieCookieOutput(self):
        self.root=self.ieCookie.invisibleRootItem()
        for i in range(len(IECookie)):
            item=QTreeWidgetItem()
            for j in range(len(IECookie[i])):
                item.setText(j, IECookie[i][j])
            self.root.addChild(item)

    def ieHistoryOutput(self):
        self.root=self.ieHistory.invisibleRootItem()
        for i in range(len(IEHistory)):
            item = QTreeWidgetItem()
            for j in range(len(IEHistory[i])):
                item.setText(j, IEHistory[i][j])
            self.root.addChild(item)

    def ieDownloadListOutput(self):
        self.root=self.ieDownloadList.invisibleRootItem()
        for i in range(len(IEDownloadList)):
            item=QTreeWidgetItem()
            for j in range(len(IEDownloadList[i])):
                item.setText(j, IEDownloadList[i][j])
            self.root.addChild(item)
    
    def historyStatistic(self):
        if self.browser[0]==1:
            chromeStatistic.main()
        elif self.browser[1]==1:
            IEStatistic.main()

    def dataToExcel(self):
        if self.browser[0]==1:
            count=0
            result=0
            for i in range(4):
                if mainWindow.check[i]==1:
                    count+=1
            if count==0:
                QMessageBox.about(self, "알림", "아티팩트를 선택해주세요.")
            elif count!=0:
                if mainWindow.check[0]==1:
                    result+=dataToExcel.chromeCacheToExcel()
                if mainWindow.check[1]==1:
                    result+=dataToExcel.chromeCookieToExcel()
                if mainWindow.check[2]==1:
                    result+=dataToExcel.chromeHistoryToExcel()
                if mainWindow.check[3]==1:
                    result+=dataToExcel.chromeDownloadListToExcel()
                if result==count:
                    QMessageBox.about(self,"알림","추출 성공")
                elif result!=count:
                    QMessageBox.about(self,"알림", "성공 %d 실패 %d" %(result,count-result))

        elif self.browser[1]==1:
            count=0
            result=0
            for i in range(4,8):
                if mainWindow.check[i]==1:
                    count+=1
            if count==0:
                QMessageBox.about(self, "알림", "아티팩트를 선택해주세요.")
            elif count!=0:
                if mainWindow.check[4]==1:
                    result+=dataToExcel.IECacheToExcel()
                if mainWindow.check[5]==1:
                    result+=dataToExcel.IECookieToExcel()
                if mainWindow.check[6]==1:
                    result+=dataToExcel.IEHistoryToExcel()
                if mainWindow.check[7]==1:
                    result+=dataToExcel.IEDownloadListToExcel()
                if result==count:
                    QMessageBox.about(self,"알림","추출 성공")
                elif result!=count:
                    QMessageBox.about(self,"알림", "성공 %d 실패 %d" %(result,count-result))

    def btn_close(self):
        self.close()
app = QApplication(sys.argv)
main=mainWindow()
main.show()
app.exec_()