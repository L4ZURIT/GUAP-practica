# -*- coding: utf-8 -*-
from datetime import date, datetime
from time import sleep
from PyQt5.uic import *
from PyQt5.QtWidgets import *
import sys
import os
import socket
from threading import Thread
import webbrowser




txt_start = "Для того чтобы работать с приложением, необходимо запустить сервер на котором находится данное приложение. После запуска приложения у вас появитяс возможность работать с ним из браузера по адресу указанному справа. Для этого просто скопируйте адрес и вставьте в коммандную строку или нажмите кнопку 'Открыть'. Если хотите открыть приложение на другом компьютере подключенном к текущей локальной сети, то просто вбейте эту же ссылку."

txt_off = "Выключен"
txt_on = "Работает"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui_main.ui',self)

        self.closeEvent = self.close_

        self.host = socket.getaddrinfo(socket.gethostname(), None)
        self.ipv4_addresses = [i[4][0] for i in self.host if i[0] == socket.AF_INET]

        self.pb_runserver:QPushButton
        self.pb_stopserver:QPushButton
        self.le_ipv4:QLineEdit
        self.lbl_main.setText(txt_start)
        self.lbl_status:QLabel

        self.pb_runserver.clicked.connect(self.pb_runserver_clicked)
        self.pb_stopserver.clicked.connect(self.pb_stopserver_clicked)
        self.pb_open.clicked.connect(self.pb_open_click)

        self.UIinit()


    def UIinit(self):
        self.le_ipv4.setText(f'http://{self.ipv4_addresses[0]}:8000')

    def run_django(self):
        os.system("venv1\\Scripts\\activate")
        os.system("python studyDB/manage.py runserver 0.0.0.0:8000")

    def pb_runserver_clicked(self):
        self.dj_thread = Thread(target=self.run_django)
        self.dj_thread.start()
        self.pb_runserver.setEnabled(False)
        self.pb_stopserver.setEnabled(True)
        self.pb_open.setEnabled(True)
        self.lbl_status.setText('Работает')


    def pb_open_click(self):
        webbrowser.open_new_tab(self.le_ipv4.text()) 
        
    def pb_stopserver_clicked(self):
        os._exit(0)
        
    def close_(e, self) -> bool:
        os._exit(0)
               


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())