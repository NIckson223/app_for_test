from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QSpinBox, QWidget, QPushButton,
                            QLabel, QHBoxLayout,QVBoxLayout, QRadioButton, QButtonGroup,
                             QGroupBox, QLineEdit)

app = QApplication([])
main_win = QWidget()
question_label = QLabel('Введіть запитання')
corect_answer_label = QLabel('Введіть правильну відповідь')
answer1_label = QLabel('Введіть першу хибну відповідь')
answer2_label = QLabel('Введіть другу хибну відповідь')
answer3_label = QLabel('Введіть третю хибну відповідь')

question = QLineEdit()
corect_answer = QLineEdit()
answer1 = QLineEdit()
answer2 = QLineEdit()
answer3 = QLineEdit()

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()

line1.addWidget(question_label)
line1.addWidget(question)

line2.addWidget(corect_answer_label)
line2.addWidget(corect_answer)

line3.addWidget(answer1_label)
line3.addWidget(answer1)

line4.addWidget(answer2_label)
line4.addWidget(answer2)

line5.addWidget(answer3_label)
line5.addWidget(answer3)

edit_layout =  QVBoxLayout()
edit_layout.addLayout(line1)
edit_layout.addLayout(line2)
edit_layout.addLayout(line3)
edit_layout.addLayout(line4)
edit_layout.addLayout(line5)

btn_add = QPushButton('Додати запитання')
btn_clean = QPushButton('Очистити')
line6 = QHBoxLayout()
line6.addWidget(btn_add)
line6.addWidget(btn_clean)

edit_layout.addLayout(line6)

stat_title =QLabel('Статистика')
amount_atempt = QLabel('Разів відповіли')
amount_correct = QLabel('Вірних відповідей')
sucsessful = QLabel('Успішність')

stat_line= QVBoxLayout()
stat_line.addWidget(stat_title, alignment=Qt.AlignLeft)
stat_line.addWidget(amount_atempt, alignment=Qt.AlignLeft)
stat_line.addWidget(amount_correct, alignment=Qt.AlignLeft)
stat_line.addWidget(sucsessful, alignment=Qt.AlignLeft)

edit_layout.addLayout(stat_line)

btn_back = QPushButton('Назад')
line7 = QHBoxLayout()
line7.addWidget(btn_back)
edit_layout.addLayout(line7)

main_win.setLayout(edit_layout)
main_win.show()
app.exec_()