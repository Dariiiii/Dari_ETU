from PyQt6 import QtCore, QtWidgets
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt
import numpy as np
from bezier_curve import show_points, bezier_curve, show_curve

colors = {
    'Красная': [1.0, 0.0, 0.0],
    'Синяя': [0.0, 0.0, 1.0],
    'Желтая': [1.0, 1.0, 0.0],
    'Зеленая': [0.0, 1.0, 0.0],
    'Розовая': [1.0, 0.5, 0.5],
    'Фиолетовая': [0.5, 0.0, 1.0],
    'Оранжевая': [1.0, 0.5, 0.0]
}


class MyGLWidget(QOpenGLWidget):  # OpenGL виджет
    def __init__(self, parent):
        super(MyGLWidget, self).__init__(parent)
        self.current_mode = 'GL_POINTS'
        self.control_points = {
            'Желтая': [-0.8, 0.0, 0.9],
            'Розовая': [-0.5, -0.7, 0.9],
            'Красная': [-0.3, -0.7, 0.8],
            'Синяя': [0.0, 0.0, 0.1],
            'Зеленая': [0.3, 0.7, 0.3],
            'Оранжевая': [0.5, 0.7, 0.3],
            'Фиолетовая': [0.8, 0.0, 0.3]
        }
        self.selected_point = None
        self.bezier_points = []

    def initializeGL(self):  # инициализация
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glPointSize(10)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        width, height = self.width(), self.height()
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def paintGL(self):  # рисование
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        show_points(self.control_points, colors)
        points = np.array(list(self.control_points.values()))
        self.bezier_points = bezier_curve(*points)
        show_curve(self.bezier_points)
        self.update()

    def calculate_coordinate(self, pos, total, type: bool):
        if type:
            reflect = 1
        else:
            reflect = -1
        if pos <= total / 2:
            return reflect * (-1 + (pos / (total / 2.0)))
        else:
            return reflect * (pos - total / 2.0) / (total / 2.0)

    def mousePressEvent(self, event):
        x = self.calculate_coordinate(event.pos().x(), self.width(), True)
        y = self.calculate_coordinate(event.pos().y(), self.height(), False)

        for i, point in enumerate(self.control_points.values()):
            if abs(x - point[0]) < 0.1 and abs(y - point[1]) < 0.1:
                self.selected_point = i
                break

    def mouseMoveEvent(self, event):  # перемещение контрольной точки на экране
        if self.selected_point is not None:
            x = self.calculate_coordinate(event.pos().x(), self.width(), True)
            y = self.calculate_coordinate(event.pos().y(), self.height(), False)
            key = list(self.control_points.keys())[self.selected_point]
            self.control_points[key][0] = x
            self.control_points[key][1] = y
            self.update()

    def mouseReleaseEvent(self, event):  # отмена выбора контрольной точки
        self.selected_point = None
