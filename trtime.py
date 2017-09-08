class MyWindow(QMainWindow, form_class):
    def __init__(self):
        self.calltime = []

    self.count = 0
    ...  # 생략

    def timeout(self):
        ...  # 생략
        self.stime = 1000 * (
        current_time.hour() * 3600 + current_time.minute() * 60 + current_time.second()) + current_time.msec()
        self.tcalltime = self.calltime  # 임시저장
        for i in self.calltime:
            if i + 1000 < self.stime:
                self.count += -1  # calltime시간보다 stime(현재시간)이 1초 지났다면 count 줄임
        if self.count <= 0:
            self.count = 0
            self.calltime = []
        else:
            self.calltime = self.tcalltime[
                            len(self.tcalltime) - self.count:len(self.tcalltime)]  # 1초가 지나지 않은게 있다면 calltime에 다시 저장


# 사용법
def trcall(self):
    if self.count < 5:
        self.kiwoom.call_opt10085()  # 원하는tr요청
        self.calltime.append(self.stime)
        self.count += 1