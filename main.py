from utils import *
from timing import *

class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.stopwatch = Stopwatch()


		self.setStyleSheet("background-color: #00ffbb;")
		self.setWindowTitle("Clock")
		# setting geometry of main window
		self.setGeometry(100, 100, 800, 400)

		# creating a vertical layout
		layout = QVBoxLayout()

		# creating font object
		font = QFont('Comic Sans MS', 120, QFont.Bold)

		# creating a label object
		self.label = QLabel()

		# setting centre alignment to the label
		self.label.setAlignment(Qt.AlignCenter)

		# setting font to the label
		self.label.setFont(font)

		# adding label to the layout
		layout.addWidget(self.label)

		# setting the layout to main window
		self.setLayout(layout)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showInfo)

		# update the timer every second
		timer.start(10)

		self.isStopwatch = False



		self.startButton = QPushButton('Start', self)
		self.startButton.clicked.connect(self.stopwatch.startTime)
		self.startButton.setStyleSheet("background-color: #FF0044; color: white;")

		self.stopButton = QPushButton('Stop', self)
		# self.stopButton.resize(100,32)
		# self.stopButton.move(120, 550)        
		self.stopButton.clicked.connect(self.stopwatch.stopTime)
		self.stopButton.setStyleSheet("background-color: #FF0044; color: white;")

		self.restartButton = QPushButton('Reset', self)
		# self.restartButton.resize(100,32)
		# self.restartButton.move(220, 550)        
		self.restartButton.clicked.connect(self.stopwatch.resetTime)
		self.restartButton.setStyleSheet("background-color: #FF0044; color: white;")

		buttonLayout = QHBoxLayout()

		buttonLayout.addWidget(self.startButton)
		buttonLayout.addWidget(self.stopButton)
		buttonLayout.addWidget(self.restartButton)

		layout.addLayout(buttonLayout)

		
		self.modeButton = QPushButton('View Stopwatch')
		self.modeButton.clicked.connect(self.changeState)
		self.modeButton.resize(100,32)
		self.modeButton.setStyleSheet("background-color: #FF0044; color: white;")
		layout.addWidget(self.modeButton)
		
		
	# method called by timer
	def showInfo(self):
		if (self.isStopwatch):
			label_content = self.stopwatch.getTime()
			self.startButton.show()
			self.stopButton.show()
			self.restartButton.show()
		else:
			label_content = Clock.getTime()
			self.startButton.hide()
			self.stopButton.hide()
			self.restartButton.hide()
		self.label.setText(label_content)

	def changeState(self):
		self.isStopwatch = not self.isStopwatch
		self.modeButton.setText("View Clock" if self.isStopwatch else "View Stopwatch")




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
home = Window()

# showing all the widgets
home.show()


# start the app
App.exit(App.exec_())
