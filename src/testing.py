# playing around

import sys
from creature import *
from player import *
from helperfunctions import *
from colors import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(300, 300)
    w.setWindowTitle('Chompers!')

    startbutton = QPushButton('Start new game!')
    c = Creature()
    startbutton.clicked.connect(c.handle_clicked)
    layout = QVBoxLayout()
    layout.addWidget(startbutton)
    w.setLayout(layout)
    w.show()
    sys.exit(app.exec_())
