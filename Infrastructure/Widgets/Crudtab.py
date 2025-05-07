import sqlite3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QLabel, QMessageBox, QPushButton


class CrudTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)  # Ana layout `self`-ə birbaşa əlavə olunur
        layout.addWidget(self.crudRow())

    def crudRow(self):
        database = sqlite3.connect("../Persistence/Database/Database.db")
        cursor = database.cursor()

        container = QWidget()
        layout = QVBoxLayout(container)

        formLayout = QVBoxLayout()

        self.nameInput = QLineEdit()
        formLayout.addWidget(QLabel("Name:"))
        formLayout.addWidget(self.nameInput)

        self.usernameInput = QLineEdit()
        formLayout.addWidget(QLabel("Username:"))
        formLayout.addWidget(self.usernameInput)

        self.descInput = QTextEdit()
        formLayout.addWidget(QLabel("Description:"))
        formLayout.addWidget(self.descInput)

        layout.addLayout(formLayout)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.handle_add)
        layout.addWidget(add_button)

        # cursor.execute(
        #     "CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, name TEXT, description TEXT, username TEXT,Completed BOOL)"
        # )
        database.commit()

        return container

    def validateInput(self, name, descripton, username):
        if not name or not descripton or not username:
            self.showError("Field(s) cannot be empty!")
            return False
        if len(name) > 50:
            self.showError("Name is too long (max 50 characters)")
            return False
        if len(descripton) > 200:
            self.showError("Description is too long (max 200 characters)")
            return False
        if len(username) > 30:
            self.showError("Username is too long (max 30 characters)")
            return False
        return True

    def handle_add(self):
        name = self.nameInput.text()
        description = self.descInput.toPlainText()
        username = self.usernameInput.text()
        if self.validateInput(name, description, username):
            try:
                database = sqlite3.connect("../Persistence/Database/Database.db")

                cursor = database.cursor()

                cursor.execute(
                    "INSERT INTO task (name, description, username,completed) VALUES (?, ?, ?,?)",
                    (name, description, username,0)
                )

            except Exception as e:
                print(f"Database error: {str(e)}")
                QMessageBox.Critical(self, "Error", e)

            database.commit()
            QMessageBox.information(self, "Success", "Task added!")

    def showError(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec_()
