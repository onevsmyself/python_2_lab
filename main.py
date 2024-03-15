from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *


def set_window():
    window.setWindowTitle("Графическое приложение")
    window.setFixedSize(800, 700)
    window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 182, 119, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(187, 13, 142, 255));")


def make_input_line(window):
    input_line = QLineEdit(window)
    
    input_line.resize(750, 80)
    input_line.move(25, 25)
    input_line.setFont(QFont("Arial", 34))
    input_line.setAlignment(Qt.AlignmentFlag(4))

    input_line.setMaxLength(36)
    input_line.setStyleSheet("background-color: rgba(0, 95, 141, 100); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px;")
    input_line.setPlaceholderText("Ваша функция")


def make_sound():
    player = QMediaPlayer()
    audio = QAudioOutput()
    player.setAudioOutput(audio)
    fullpath = QDir.current().absoluteFilePath("music/music1.mp3")
    url = QUrl.fromLocalFile(fullpath)
    player.setSource(url)
    player.play()


def set_label_with_buttons(window):
    label = QLabel("Границы отрезка", window)
    label.setStyleSheet(u"color: white;\n"
"font-size: 22pt;\n"
"background-color: none;\n"
"border: none;")
    label.resize(230, 40)
    label.move(50, 120)

    start_section_line = QLineEdit(window)
    start_section_line.setFont(QFont("Ariel", 20))
    start_section_line.resize(120, 40)
    start_section_line.move(30, 175)
    start_section_line.setPlaceholderText("a")

    end_section_line = QLineEdit(window)
    end_section_line.setFont(QFont("Ariel", 20))
    end_section_line.resize(120, 40)
    end_section_line.move(170, 175)
    end_section_line.setPlaceholderText("b")

    start_section_line = QLineEdit(window)
    start_section_line.setFont(QFont("Ariel", 20))
    start_section_line.resize(150, 40)
    start_section_line.move(30, 285)

    start_section_line = QLineEdit(window)
    start_section_line.setFont(QFont("Ariel", 20))
    start_section_line.resize(150, 40)
    start_section_line.move(30, 340)

    eps_section_line = QLineEdit(window)
    eps_section_line.setFont(QFont("Ariel", 20))
    eps_section_line.resize(150, 40)
    eps_section_line.move(30, 395)
  








app = QApplication([])
window = QMainWindow()

set_window()
make_sound()
set_label_with_buttons(window)
input_line = make_input_line(window)


window.show()
app.exec()