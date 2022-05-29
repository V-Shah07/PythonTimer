import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QPushButton
from timing import Clock, Stopwatch


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.clock = Clock()
        self.stopwatch = Stopwatch()

        self.is_stopwatch = False

        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Clock")
        self.setStyleSheet("background-color: #00ffbb;")

        main_layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Comic Sans MS', 120, QFont.Bold))
        main_layout.addWidget(self.label)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.stopwatch.startTime)
        self.start_button.setStyleSheet(
            "background-color: #FF0044; color: white;")

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stopwatch.stopTime)
        self.stop_button.setStyleSheet(
            "background-color: #FF0044; color: white;")

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.stopwatch.resetTime)
        self.reset_button.setStyleSheet(
            "background-color: #FF0044; color: white;")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)
        main_layout.addLayout(button_layout)

        self.mode_button = QPushButton('View Stopwatch')
        self.mode_button.clicked.connect(self.changeState)
        self.mode_button.resize(100, 32)
        self.mode_button.setStyleSheet(
            "background-color: #FF0044; color: white;")
        main_layout.addWidget(self.mode_button)

        timer = QTimer(self)
        timer.timeout.connect(self.showInfo)
        timer.start(10)

        self.setLayout(main_layout)

    def showInfo(self):
        if (self.is_stopwatch):
            label_content = self.stopwatch.getTime()
            self.start_button.show()
            self.stop_button.show()
            self.reset_button.show()
        else:
            label_content = self.clock.getTime()
            self.start_button.hide()
            self.stop_button.hide()
            self.reset_button.hide()

        self.label.setText(label_content)

    def changeState(self):
        self.is_stopwatch = not self.is_stopwatch
        self.mode_button.setText(
            "View Clock" if self.is_stopwatch else "View Stopwatch")


app = QApplication(sys.argv)
home = Window()
home.show()
app.exit(app.exec_())
