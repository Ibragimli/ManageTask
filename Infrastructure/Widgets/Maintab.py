# Maintab.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QSpacerItem, QPushButton, QSizePolicy, QLabel, QCheckBox
from Persistence.Services.TaskTable import create_task_row
class MainTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        scrollArea = QScrollArea()
        scrollWidget = QWidget()
        scrollLayout = QVBoxLayout(scrollWidget)

        tasks = ["Buy groceries", "Write report", "Call client", "Fix bug", "Update resume"] * 10

        for task_name in tasks:
            rowLayout = create_task_row(task_name)
            scrollLayout.addLayout(rowLayout)

        scrollArea.setWidget(scrollWidget)
        scrollArea.setWidgetResizable(True)

        buttonLayout = QHBoxLayout()
        buttonLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        completedButton = QPushButton("Completed")
        buttonLayout.addWidget(completedButton)

        layout.addWidget(scrollArea)
        layout.addLayout(buttonLayout)