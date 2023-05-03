#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.initializeUI()
        self.setUpButton()

    def initializeUI(self):
        self.setWindowTitle("PRESS THIS BUTTON")
        self.resize(256, 144)
        self.moveToCenter()

    def moveToCenter(self):
        qrect = self.frameGeometry()
        center_position = self.screen().availableGeometry().center()
        qrect.moveCenter(center_position)
        self.move(qrect.topLeft())

    def setUpButton(self):
        button = QPushButton(self)
        button.setText("Press to see\nthe best\nGUI homework!")
        button.setStyleSheet("background-color: white; color: black; font-family: Courier New; font-size: 24px;")
        self.setCentralWidget(button)
        button.clicked.connect(self.switchToWeb)

    def switchToWeb(self):
        self.window = WebWindow()
        self.window.show()
        self.close()


class WebWindow(QWebEngineView):
    def __init__(self):
        super(WebWindow, self).__init__()

        self.setUrl(QUrl("https://youtu.be/dQw4w9WgXcQ"))

    # Это попытка удалить кэш
    def closeEvent(self, event):
        event.accept()
        self.page().deleteLater()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
