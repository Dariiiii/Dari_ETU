from OpenGL.GL import *
from OpenGL.GLUT import *

colors = [[1.0, 0.0, 0.0, 1.0],  
          [0.0, 1.0, 0.0, 0.8],   
          [0.0, 0.0, 1.0, 0.9],   
          [1.0, 1.0, 0.0, 0.5],   
          [0.0, 1.0, 1.0, 1.0],   
          [1.0, 0.0, 1.0, 0.1]]   

vertex = [[0.3, 0.5],
          [0.6, 0],
          [0.4, -0.3],
          [0, -0.5],
          [-0.4, -0.3],
          [-0.6, 0],
          [-0.4, 0.3],
          [0, 0.5]]

def points():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()
    
def lines():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def lineStrip():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(3)
    glBegin(GL_LINE_STRIP)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def lineLoop():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def triangles():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glBegin(GL_TRIANGLES)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def triangleStrip():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def triangleFan():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])  
    glEnd()

def quads():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glBegin(GL_QUADS)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def quadStrip():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_QUAD_STRIP)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

def polygon():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(4)
    glBegin(GL_POLYGON)
    for i in range(len(vertex)):
        glColor4f(*colors[i%len(colors)])
        glVertex2f(vertex[i][0], vertex[i][1])
    glEnd()

commands = {
    "GL_POINTS" : points,
    "GL_LINES" : lines,
    "GL_LINE_STRIP" : lineStrip,
    "GL_LINE_LOOP" : lineLoop,
    "GL_TRIANGLES": triangles,
    "GL_TRIANGLE_STRIP": triangleStrip,
    "GL_TRIANGLE_FAN" : triangleFan,
    "GL_QUADS" : quads,
    "GL_QUAD_STRIP" : quadStrip,
    "GL_POLYGON" : polygon
}

func = {
    'GL_ALWAYS': GL_ALWAYS,
    'GL_NEVER': GL_NEVER,
    'GL_LESS': GL_LESS,
    'GL_EQUAL': GL_EQUAL,
    'GL_LEQUAL': GL_LEQUAL,
    'GL_GREATER': GL_GREATER,
    'GL_NOTEQUAL': GL_NOTEQUAL,
    'GL_GEQUAL': GL_GEQUAL,
    'GL_NEVER': GL_NEVER
}

sfactor = {
    'GL_ONE': GL_ONE,
    'GL_ZERO': GL_ZERO,
    'GL_DST_COLOR': GL_DST_COLOR,
    'GL_ONE_MINUS_DST_COLOR': GL_ONE_MINUS_DST_COLOR,
    'GL_SRC_ALPHA': GL_SRC_ALPHA,
    'GL_ONE_MINUS_SRC_ALPHA': GL_ONE_MINUS_SRC_ALPHA,
    'GL_DST_ALPHA': GL_DST_ALPHA,
    'GL_ONE_MINUS_DST_ALPHA': GL_ONE_MINUS_DST_ALPHA,
    'GL_SRC_ALPHA_SATURATE': GL_SRC_ALPHA_SATURATE
}

dfactor = {
    'GL_ZERO': GL_ZERO,
    'GL_ONE': GL_ONE,
    'GL_SRC_COLOR': GL_SRC_COLOR,
    'GL_ONE_MINUS_SRC_COLOR': GL_ONE_MINUS_SRC_COLOR,
    'GL_SRC_ALPHA': GL_SRC_ALPHA,
    'GL_ONE_MINUS_SRC_ALPHA': GL_ONE_MINUS_SRC_ALPHA,
    'GL_DST_ALPHA': GL_DST_ALPHA,
    'GL_ONE_MINUS_DST_ALPHA': GL_ONE_MINUS_DST_ALPHA
}