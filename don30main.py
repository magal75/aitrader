#파일명 main.py
#이 파일을 실행시키면 됩니다. 같은 프로젝트 안에 realtimekiwoom.py 파일이 있어야 합니다.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from realtimekiwoom import * #kiwoom.py에 해당
# git 테스트
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kiwoomconnect()
        self.kiwoom.res_set_real("1001")      #####실시간 연결 시작
        print("실시간연결")
    def kiwoomconnect(self):
        self.kiwoom = Kiwoom()
        self.kiwoom._comm_connect()
        self.kiwoom.OnReceiveRealData.connect(self.real_check)
#이벤트 처리하는곳
    def real_check(self, sRealKey, sRealType, sRealData):
        if self.kiwoom._get_comm_real_data(sRealKey, 27)!='':
            print('매도호가 : ',abs(int(self.kiwoom._get_comm_real_data(sRealKey, 27))))
        if self.kiwoom._get_comm_real_data(sRealKey, 27)!='':
            print('매수호가 : ',abs(int(self.kiwoom._get_comm_real_data(sRealKey, 28))))
        #27 : 매도호가 , 28 : 매수호가 , 20: 체결시간    기타번호는 KOA 스튜디오 실시간목록 참조
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()