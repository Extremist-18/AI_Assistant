import sys
import psutil
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QFont, QMovie, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS AI SYSTEM")
        self.setGeometry(100, 50, 2000, 1000)
        self.setStyleSheet("background-color: transparent; color: cyan;")

        # Set transparent background
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.Window, QColor(0, 0, 0, 200))  # semi-transparent
        self.setPalette(p)

        # Background GIF
        self.bg_label = QLabel(self)
        self.bg_movie = QMovie("assets/bg.gif")
        self.bg_movie.setCacheMode(QMovie.CacheAll)
        # self.bg_movie.setScaledSize(self.size())  # scales to window size
        self.bg_movie.setSpeed(100)
        self.bg_label.setMovie(self.bg_movie)
        self.bg_label.setAlignment(Qt.AlignCenter)  # Center the gif
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_movie.start()

        # Layouts
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        # Time + Date
        self.time_label = QLabel()
        self.time_label.setFont(QFont("Orbitron", 22))
        self.time_label.setAlignment(Qt.AlignCenter)

        # System Stats
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setFormat("CPU: %p%")
        self.cpu_bar.setAlignment(Qt.AlignCenter)
        self.cpu_bar.setStyleSheet("QProgressBar::chunk { background-color: #00ffff; }")

        self.ram_bar = QProgressBar()
        self.ram_bar.setFormat("RAM: %p%")
        self.ram_bar.setAlignment(Qt.AlignCenter)
        self.ram_bar.setStyleSheet("QProgressBar::chunk { background-color: #ff00ff; }")

        # Assistant Response
        self.assistant_label = QLabel("Awaiting your command, Sir.")
        self.assistant_label.setFont(QFont("Orbitron", 16))
        self.assistant_label.setAlignment(Qt.AlignCenter)
        self.assistant_label.setStyleSheet("color: cyan; background-color: rgba(0,0,0,100);")
        self.assistant_label.setWordWrap(True)

        # Combine layouts
        self.top_layout.addWidget(self.time_label)
        self.bottom_layout.addWidget(self.cpu_bar)
        self.bottom_layout.addWidget(self.ram_bar)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.assistant_label)
        self.main_layout.addLayout(self.bottom_layout)

        # Set main layout on transparent overlay widget
        self.overlay_widget = QWidget(self)
        self.overlay_widget.setLayout(self.main_layout)
        self.overlay_widget.setGeometry(50, 50, 900, 600)
        self.overlay_widget.setStyleSheet("background-color: transparent;")

        # Timer for live updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        current_date = QDate.currentDate().toString("dddd, MMMM d yyyy")
        self.time_label.setText(f"{current_date}\n{current_time}")

        self.cpu_bar.setValue(psutil.cpu_percent())
        self.ram_bar.setValue(psutil.virtual_memory().percent)

    def update_response(self, text):
        self.assistant_label.setText("")
        self.typing_index = 0
        self.response_text = text

        self.typing_timer = QTimer()
        self.typing_timer.timeout.connect(self.animate_typing)
        self.typing_timer.start(30)

    def animate_typing(self):
        if self.typing_index < len(self.response_text):
            self.assistant_label.setText(self.response_text[:self.typing_index + 1])
            self.typing_index += 1
        else:
            self.typing_timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ui = JarvisUI()
    ui.show()
    sys.exit(app.exec_())
