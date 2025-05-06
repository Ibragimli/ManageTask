import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout, QTabWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Crypto App")
        layout = QVBoxLayout(self)
        tabWidget = QTabWidget(self)

        # Main tab
        mainPage = QWidget()
        mainPageLayout = QVBoxLayout()
        mainPageLayout.addWidget(QLabel("Main Page"))
        mainPage.setLayout(mainPageLayout)

        # 2 tab
        completedTask = QWidget()
        completedTask_layout = QVBoxLayout()
        completedTask_layout.addWidget(QLabel("Tab 1: Main Page"))
        completedTask.setLayout(completedTask_layout)

        # 3 tab
        manageTask = QWidget()
        manageTaskLayout = QVBoxLayout()
        manageTaskLayout.addWidget(QLabel("Tab 2: Main Page"))
        manageTask.setLayout(manageTaskLayout)

        # 4 tab
        statisticTab = QWidget()
        statisticTabLayout = QVBoxLayout()
        statisticTabLayout.addWidget(QLabel("Tab 3: Main Page"))
        statisticTab.setLayout(statisticTabLayout)

        # Tabları əlavə edirik
        tabWidget.addTab(mainPage, "Main")
        tabWidget.addTab(completedTask, "Settings")
        tabWidget.addTab(manageTask, "Manage Tasks")
        tabWidget.addTab(statisticTab, "Statistics")

        # Tab widget-i layout-a əlavə edirik
        layout.addWidget(tabWidget)
        # Pəncərə ölçüsünü təyin edirik
        self.setGeometry(1400, 400, 400, 400)
        self.show()


app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())

#
#     def init_ui(self):
#
#         self.checkbox = QCheckBox("Python'ı seviyor musunuz ?")
#         self.yazi_alani = QLabel("")
#         self.buton = QPushButton("Bana Tıkla")
#
#         v_box = QVBoxLayout()
#
#         v_box.addWidget(self.checkbox)
#         v_box.addWidget(self.yazi_alani)
#         v_box.addWidget(self.buton)
#
#         self.setLayout(v_box)
#
#         self.setWindowTitle("Check Box")
#
#         self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(), self.yazi_alani))
#
#         self.show()
#
#     def click(self, checkbox, yazi_alani):
#         if checkbox:
#             yazi_alani.setText("Python'ı seviyorsun çok güzel")
#         else:
#             yazi_alani.setText("Niye Sevmiyorsun ? ")
#
#
# app = QApplication(sys.argv)
#
# pencere = Pencere()
#
# sys.exit(app.exec_())
