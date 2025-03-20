from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np


def show_points(points, colors):  # показать контрольные точки
    glPointSize(10)
    for p in points:
        glColor3f(colors[p][0], colors[p][1], colors[p][2])
        glBegin(GL_POINTS)
        glVertex2f(points[p][0], points[p][1])
        glEnd()


def show_curve(points):  # показать кривую
    glPointSize(3)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(1, len(points)):
        glBegin(GL_LINES)
        glVertex2f(points[i - 1, 0], points[i - 1, 1])
        glVertex2f(points[i, 0], points[i, 1])
        glEnd()
    pass


def bezier_curve(p0, p1, p2, p3, p4, p5, p6):  # кривая Безье
    curve_points = np.zeros((200, 2))
    for i, t in enumerate(np.linspace(0, 1, 100)):
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        curve_points[i] = [x, y]
    for i, t in enumerate(np.linspace(0, 1, 100)):
        z = (1 - t) ** 3 * p3[0] + 3 * (1 - t) ** 2 * t * p4[0] + 3 * (1 - t) * t ** 2 * p5[0] + t ** 3 * p6[0]
        w = (1 - t) ** 3 * p3[1] + 3 * (1 - t) ** 2 * t * p4[1] + 3 * (1 - t) * t ** 2 * p5[1] + t ** 3 * p6[1]
        curve_points[i + 100] = [z, w]
    return curve_points
