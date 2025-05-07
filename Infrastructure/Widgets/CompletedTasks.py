import sqlite3

from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QScrollArea


class CompletedTasks(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        layout = QVBoxLayout(self)
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollWidget = QWidget()
        scrollLayout = QVBoxLayout(scrollWidget)



        scrollArea.setWidget(scrollWidget)
        layout.addWidget(scrollArea)


    def compTasks(self):
        database = sqlite3.connect("../../Persistence/Database/database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM tasks")