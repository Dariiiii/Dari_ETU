from PyQt6 import QtCore, QtWidgets
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from commands import commands

class MyGLWidget(QOpenGLWidget):
    def __init__(self,parent):
        super(MyGLWidget, self).__init__(parent)
        self.current_mode = 'GL_POINTS'

    def paintGL(self):
        if self.current_mode in commands:
            commands[self.current_mode]()
        self.update()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.glWidget = MyGLWidget(parent=self.centralwidget)
        self.glWidget.setGeometry(QtCore.QRect(0, 0, 541, 600))
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(570, 20, 221, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setCurrentText(_translate("MainWindow", "GL_POINTS"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GL_POINTS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "GL_LINES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GL_LINE_STRIP"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GL_LINE_LOOP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GL_TRIANGLES"))
        self.comboBox.setItemText(5, _translate("MainWindow", "GL_TRIANGLE_STRIP"))
        self.comboBox.setItemText(6, _translate("MainWindow", "GL_TRIANGLE_FAN"))
        self.comboBox.setItemText(7, _translate("MainWindow", "GL_QUADS"))
        self.comboBox.setItemText(8, _translate("MainWindow", "GL_QUAD_STRIP"))
        self.comboBox.setItemText(9, _translate("MainWindow", "GL_POLYGON"))
    
    def onComboBoxChanged(self):
        print(self.comboBox.currentText())
        self.glWidget.current_mode = self.comboBox.currentText()
        self.glWidget.update()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.comboBox.currentIndexChanged.connect(ui.onComboBoxChanged)
    MainWindow.show()
    sys.exit(app.exec())
