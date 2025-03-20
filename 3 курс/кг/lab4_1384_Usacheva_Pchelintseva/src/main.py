import sys
import numpy as np
from PyQt6 import QtCore, QtWidgets
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class MyGLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super(MyGLWidget, self).__init__(parent)
        self.faze = 0
        self.coef = 3 / np.sqrt(3)
        self.angle = 90
        self.base_polygon = np.array([
            [0.0, np.sqrt(3) / 3],   # Вершина верхнего угла
            [-0.5, -np.sqrt(3) / 6], # Левый нижний угол
            [0.5, -np.sqrt(3) / 6]   # Правый нижний угол
        ])/2

    def paintGL(self):
        self.fractal = []
        self.fractal.append(self.base_polygon)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очистка буферов цвета и глубины
        if self.faze > 0:  # Если фаза больше нуля, рисуем фрактал
            self.fractal_step()  # Выполняем шаг фрактализации
        draw_fractal(self.fractal)  # Рисуем фрактал

    def fractal_step(self):
        # print("------------------------------------------------")
        for i in range(self.faze):  # Проходим по всем фигурам во фрактале
            new_figure = np.array([self.rotate_dots(dot, np.deg2rad(self.angle + ((i %2)*self.angle))) for dot in self.fractal[i]])
            if i == 0 or i == 2:
                self.fractal.append(new_figure * self.coef)  # Масштабируем фигуру
            else:
                self.fractal.append(new_figure)  # Добавляем новую фигуру без масштабирования

    def rotate_dots(self, dot, angle):
        x_new = dot[0] * np.cos(angle) - dot[1] * np.sin(angle)
        y_new = dot[0] * np.sin(angle) + dot[1] * np.cos(angle)
        return [x_new, y_new]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 600)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.openGLWidget = MyGLWidget(parent=self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.openGLWidget.setObjectName("openGLWidget")
        
        self.minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(670, 120, 93, 28))
        self.minus.setObjectName("minus")
        self.minus.clicked.connect(self.press_minus)
        
        self.plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(670, 380, 93, 28))
        self.plus.setObjectName("plus")
        self.plus.clicked.connect(self.press_plus)
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 240, 55, 16))
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Фаза 0"))

    def press_plus(self):
        self.openGLWidget.faze += 1
        self.label.setText("Фаза " + str(self.openGLWidget.faze))
        self.openGLWidget.update()

    def press_minus(self):
        if self.openGLWidget.faze >= 1:
            self.openGLWidget.faze -= 1
            self.label.setText("Фаза " + str(self.openGLWidget.faze))
            self.openGLWidget.update()

def draw_fractal(fractal):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLineWidth(3) 
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) 
    
    for f in fractal:
        glColor4f(1.0, 1.0, 1.0, 1.0) 
        glBegin(GL_TRIANGLES)  
        for i in range(len(f)): 
            glVertex2f(f[i][0], f[i][1]) 
            
        glEnd()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())