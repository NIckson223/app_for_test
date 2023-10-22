from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QSpinBox, QWidget, QPushButton,
                            QLabel, QHBoxLayout,QVBoxLayout, QRadioButton, QButtonGroup,
                             QGroupBox)

from memo_app import app

main_win = QWidget()
main_win.setWindowTitle("Тестування")
main_win.resize(400,400)

qtext=QLabel('Питання')
v_line = QVBoxLayout()

rbtn_1=QRadioButton('')
rbtn_2=QRadioButton('')
rbtn_3=QRadioButton('')
rbtn_4=QRadioButton('')

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

btn_Menu=QPushButton('Меню')
btn_Sleep=QPushButton('Відпочити')
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok=QPushButton('Відповісти')

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line4=QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)

layout_line2.addWidget(qtext,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line4.addWidget(btn_Ok,alignment=Qt.AlignCenter)

layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)


def show_result():
    RadioGroupBox.hide()
    btn_Ok.setText('Наступне питання')


def show_question():
    RadioGroupBox.show()
    btn_Ok.setText('Відповісти')
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)



