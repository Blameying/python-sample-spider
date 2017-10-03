# -*- coding: utf-8 -*-

from lxml import etree
import requests
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont, QPalette, QColor
import sys


class downloadHtml(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel('None')
        self.draw()

    def getHtml(self):
        req = requests.Session()
        req.headers.clear()
        text = req.get('http://today.hitwh.edu.cn/news_more_list.asp?id=7')
        text.encoding = 'utf-8'
        html = etree.HTML(text.text)

        results = html.xpath("//li/a[@target='_blank']")
        count = html.xpath("//li//span/font")
        date = html.xpath("//div/ul/li/font")

        strs = []

        for i in range(len(date)):
            strs.append(date[i].text + '\n' +
                        results[i].text + '\n' + count[i].text + '\n')

        self.label.setText(strs[0] + strs[1] + strs[2] + '----------')

    def draw(self):
        layout = QVBoxLayout()
        button = QPushButton(r'FLASH', self)
        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowTitle("HIT-News-718")

        font = QFont()
        font.setFamily('black')
        font.setBold(True)
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        button.setFont(font)

        self.setStyleSheet(
            "QLabel{background:rgb(223, 181, 183,255);}  QLabel{color:rgb(255, 255,255,255);}  QPushButton{background:rgb(29,176,184,255);}  QPushButton{color:rgb(255,255,255,255);}")
        self.label.setAutoFillBackground(True)

        button.clicked.connect(self.getHtml)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = downloadHtml()
    w.show()
    sys.exit(app.exec_())


# print(text.text)
