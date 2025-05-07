import sys
import sqlite3
from Infrastructure.Widgets.Maintab import MainTab
from Infrastructure.Widgets.Crudtab import CrudTab

from PyQt5.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QTabWidget
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Task Manager")
        layout = QVBoxLayout(self)
        tabWidget = QTabWidget(self)

        tabWidget.addTab(MainTab(), "Main")
        tabWidget.addTab(CrudTab(), "Crud")

        layout.addWidget(tabWidget)
        self.setGeometry(600, 300, 400, 300)
        self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
