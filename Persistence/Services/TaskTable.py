# TaskRow.py
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QCheckBox, QSpacerItem, QSizePolicy

def create_task_row(task_name):
    layout = QHBoxLayout()
    label = QLabel(task_name)
    checkbox = QCheckBox()
    checkbox.setProperty("task_name", task_name)

    layout.addWidget(label)
    layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    layout.addWidget(checkbox)

    return layout
