# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 330)
        Form.setMinimumSize(QtCore.QSize(580, 330))
        Form.setMaximumSize(QtCore.QSize(580, 330))
        Form.setAccessibleName("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 551, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 0, 0);\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(198, 198, 198);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: green;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    background-color: rgb(0, 188, 0);\n"
"}\n"
"\n"
"QPushButtonr{\n"
"    color: black;\n"
"    background-color: ;\n"
"    background-color: rgba(0, 255, 0, 100);\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 19, 551, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 2, 91, 16))
        self.label.setStyleSheet("font-size: 11px;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 43, 91, 16))
        self.label_2.setStyleSheet("font-size: 11px;\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 59, 551, 71))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 150, 551, 131))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 133, 141, 16))
        self.label_3.setStyleSheet("font-size: 11px;\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SAH256 - Дешифратор"))
        self.pushButton.setText(_translate("Form", "РАСШИФРОВАТЬ"))
        self.label.setText(_translate("Form", "Файл словаря"))
        self.label_2.setText(_translate("Form", "Хеш (SHA256)"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Form", "Расшифрованный ХЕШ"))
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
# -----------------------------------------------------------------------------------------------------------------------------------------------------

import hashlib
def sha256_func():
    def sha():
        try:
            f = open(str(ui.lineEdit.text()), 'r', encoding='utf-8')
            f1 = f.read()
            f.closed
            exec('global list_sha_no\nlist_sha_no = ' + '[\'' + str(f1).replace('\n', '\', \'') + '\']')
            #global list_sha_no
            find = str(ui.textEdit.toPlainText())
            size = len(list_sha_no)
            for x in range(1, int(size)):
                #global list_sha_no
                exec('global sha\nsha = hashlib.sha256(b\'' + str(list_sha_no[x]) + '\').hexdigest()')
                global sha
                if str(sha) == str(find):
                    print(list_sha_no[x])
                    ui.textEdit_2.setText(str(list_sha_no[x]))
                    break
        except Exception as e:
            print(str(e))
    sha()
ui.pushButton.clicked.connect( sha256_func )

sys.exit(app.exec_())