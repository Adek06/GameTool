'''
the surface of onmyoji_assist.py
'''

import sys
import time
import onmyoji_assistant as oa
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
                            QLineEdit, QPushButton, \
                            QHBoxLayout, QVBoxLayout, QLCDNumber,\
                            QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

class Click(QThread):
    """
    Control game client to execute script
    """

    def click(self):
        """No meaning, just for fucking pylint"""
        pass

    def run(self):
        """Control game client"""
        oa.shua_game(shua_times=oa.calculate_times(int(HP_LINE.text())),\
                        wait_time=int(FIGHT_TIME_LINE.text()))
        oa.colse_game()

class Timer(QThread):
    """
    Display remaining time
    """
    signal = pyqtSignal()
    def run(self):
        """Control display remaining time"""
        fight_time = int(FIGHT_TIME_LINE.text())
        hp_num = int(HP_LINE.text())
        need_time = oa.calculate_times(health=hp_num)*(fight_time+18)
        LCD_NUMBER.display(need_time)
        display_time = need_time
        for _ in range(need_time):
            self.sleep_one()
            if (display_time % (fight_time+18)) == 0:# or (display_time == fight_time and (int(HP_LINE.text()) > 6)):
                hp_num -= 6
                HP_LINE.setText(str(hp_num))
            display_time -= 1
            LCD_NUMBER.display(display_time)
        self.signal.emit()

    def sleep_one(self):
        """sleep 1 seconds"""
        time.sleep(1)
        return

def work():
    """start thread"""
    CLICK_THREAD.start()
    TIMER_THREAD.start()

def show_end():
    """when the remaining time equal zero, dislpay the successful information"""
    QMessageBox.information(GUI, "结束", "现有体力已经刷完，于{}结束。".format(\
                            time.asctime(time.localtime(time.time()))))

def end():
    """exit application"""
    sys.exit()

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    GUI = QWidget()
    GUI.setGeometry(300, 300, 500, 500)
    GUI.setWindowTitle("阴阳师觉醒材料辅助")
    FIGHT_TIME_LABEL = QLabel("每场战斗的时间（秒）：(需要自己估算，计时结束后才可更改)")
    FIGHT_TIME_LINE = QLineEdit(GUI)
    FIGHT_TIME_LINE.setText(str(150))
    HP_LABEL = QLabel("剩余体力：（计时结束后才可更改）")
    HP_LINE = QLineEdit(GUI)
    TIME_LABEL = QLabel("剩余时间（秒）：")
    ENTER_BUTTON = QPushButton("开始", GUI)
    END_BUTTON = QPushButton("结束", GUI)

    SUB_LAYOUT = QHBoxLayout()
    SUB_LAYOUT.addWidget(END_BUTTON)
    SUB_LAYOUT.addStretch(1)
    SUB_LAYOUT.addWidget(ENTER_BUTTON)

    BODY_LAYOUT = QVBoxLayout()
    BODY_LAYOUT.addWidget(FIGHT_TIME_LABEL)
    BODY_LAYOUT.addWidget(FIGHT_TIME_LINE)
    BODY_LAYOUT.addWidget(HP_LABEL)
    BODY_LAYOUT.addWidget(HP_LINE)
    BODY_LAYOUT.addWidget(TIME_LABEL)
    LCD_NUMBER = QLCDNumber()
    BODY_LAYOUT.addWidget(LCD_NUMBER)
    BODY_LAYOUT.addLayout(SUB_LAYOUT)

    CLICK_THREAD = Click()
    TIMER_THREAD = Timer()
    TIMER_THREAD.signal.connect(show_end)
    ENTER_BUTTON.clicked.connect(work)
    END_BUTTON.clicked.connect(end)
    GUI.setLayout(BODY_LAYOUT)

    GUI.show()
    sys.exit(APP.exec_())
