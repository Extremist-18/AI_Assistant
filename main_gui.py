import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize, QTimer, QTime, QDate
from PyQt6.QtGui import QFont, QMovie, QColor
from main import AIAssistant
from features.weather import get_weather_text 
import time

class AssistantThread(QThread):
    result_signal = pyqtSignal(str)
    exit_signal = pyqtSignal()

    def __init__(self, assistant):
        super().__init__()
        self.assistant = assistant

    def run(self):
        while True:
            command = self.assistant.listen()
            if command:
                self.result_signal.emit(f'You: {command}')
                response = self.assistant.handle_command(command)
                if response is False:
                    self.result_signal.emit(
                        '<div align="center"><span style="font-size:20px; color:#ff4444;">Assistant: Shutting down in 5 seconds...</span></div>'
                    )
                    # QMetaObject.invokeMethod(QApplication.instance(), "processEvents")
                    QApplication.processEvents()
                    time.sleep(5)
                    self.exit_signal.emit()
                    break
                self.result_signal.emit("Assistant: Task complete")


class AssistantGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.assistant = AIAssistant()
        self.thread = AssistantThread(self.assistant)
        self.thread.result_signal.connect(self.update_output)
        self.thread.exit_signal.connect(self.close_app) 
        self.initUI()
        self.thread.start()
    
    def close_app(self):
        self.close()
        # QApplication.quit()  # or self.close()
        
    def initUI(self):
        self.setWindowTitle(" Futuristic AI Assistant")
        self.setGeometry(200, 100, 800, 750)
        self.setStyleSheet("background-color: #101820; color: #00ffe1;")

        # Title
        title = QLabel("NOVA", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Orbitron", 22))
        title.setStyleSheet("color: #00ffe1;")

        self.acronym = QLabel(" Next-gen Operating Virtual Assistant",self)
        self.acronym.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.acronym.setFont(QFont("Orbitron",18))
        self.acronym.setStyleSheet("padding: 8px; color: #00ffe1;")
        # GIF
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        movie = QMovie("media/ai_loop.gif")
        movie.setScaledSize(QSize(300, 200))
        self.gif_label.setMovie(movie)
        movie.start()

        # Output box
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #00ffe1;
                border: 2px solid #00ffe1;
                border-radius: 15px;
                padding: 12px;
            }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 255, 255))
        shadow.setOffset(0, 0)
        self.output.setGraphicsEffect(shadow)

        # Top-right HUD: Time / Date / Weather
        self.hud_label = QLabel("", self)
        self.hud_label.setFont(QFont("Consolas", 11))
        self.hud_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.hud_label.setStyleSheet("padding: 5px; color: #00e6e6;")

        # HUD timer update every 5 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_hud)
        self.timer.start(30000)  # 30 seconds
        self.update_hud()  # Initial load

        # Layout
        main_layout = QVBoxLayout()
        hud_layout = QHBoxLayout()
        hud_layout.addStretch()
        hud_layout.addWidget(self.hud_label)

        main_layout.addLayout(hud_layout)
        main_layout.addWidget(title)
        main_layout.addWidget(self.acronym)
        main_layout.addWidget(self.gif_label)
        main_layout.addWidget(self.output)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(main_layout)

    def update_hud(self):
        now = QTime.currentTime().toString("hh:mm AP")
        date = QDate.currentDate().toString("dddd, MMMM d")
        weather = get_weather_text()
        # print(weather)
        self.hud_label.setText(f"🕒 {now} | 📅 {date}\n🌡️ {weather}")

    def update_output(self, text):
        self.output.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = AssistantGUI()
    gui.show()
    sys.exit(app.exec())
