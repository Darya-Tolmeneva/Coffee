import sys
import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5 import uic


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(250)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена, руб", "объем упаковки, г"])
        for i in range(len(result)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())