import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from PyQt6.QtCore import QTimer
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import shaders

vertex_shader_source = """
#version 330
in vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

fragment_shader_source = """
#version 330
out vec4 fragColor;

uniform float time;
uniform vec2 resolution;

float snoise(vec3 uv, float res)
{
    const vec3 s = vec3(1e0, 1e2, 1e3);
    uv *= res;
    vec3 uv0 = floor(mod(uv, res)) * s;
    vec3 uv1 = floor(mod(uv + vec3(1.0), res)) * s;
    vec3 f = fract(uv); 
    f = f * f * (3.0 - 2.0 * f);
    vec4 v = vec4(uv0.x + uv0.y + uv0.z, uv1.x + uv0.y + uv0.z,
                  uv0.x + uv1.y + uv0.z, uv1.x + uv1.y + uv0.z);

    vec4 r = fract(sin(v * 1e-1) * 1e3);
    float r0 = mix(mix(r.x, r.y, f.x), mix(r.z, r.w, f.x), f.y);
    r = fract(sin((v + uv1.z - uv0.z) * 1e-1) * 1e3);
    float r1 = mix(mix(r.x, r.y, f.x), mix(r.z, r.w, f.x), f.y);
    return mix(r0, r1, f.z) * 2.0 - 1.0;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord)
{
    vec2 p = -0.5 + fragCoord.xy / resolution.xy;
    p.x *= resolution.x / resolution.y;
    float color = 3.0 - (3.0 * length(2.0 * p));
    vec3 coord = vec3(atan(p.x, p.y) / 6.2832 + 0.5, length(p) * 0.4, 0.5);
    for (int i = 1; i <= 7; i++)
    {
        float power = pow(2.0, float(i));
        color += (1.5 / power) * snoise(coord + vec3(0.0, time * 0.05, time * 0.01), power * 16.0);
    }
    fragColor = vec4(color, pow(max(color, 0.0), 2.0) * 0.4, pow(max(color, 0.0), 3.0) * 0.15, 1.0);
}

void main()
{
    mainImage(fragColor, gl_FragCoord.xy);
}
"""


class MyGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.program = None
        self.time = 0.0
        self.width = 750
        self.height = 750

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.create_shaders()

    def paintGL(self):
        self.time += 0.01  # Обновляем время для эффекта огня
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program)  # Активируем программу шейдеров
        glUniform1f(glGetUniformLocation(self.program, "time"), self.time)  # Устанавливаем uniform переменную
        # Устанавливаем uniform переменную для размера экрана
        glUniform2f(glGetUniformLocation(self.program, "resolution"), self.width, self.height)

        # Рисуем квадрат
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()
        self.update()

    def create_shaders(self):
        vertex_shader = shaders.compileShader(vertex_shader_source, GL_VERTEX_SHADER)
        fragment_shader = shaders.compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
        self.program = shaders.compileProgram(vertex_shader, fragment_shader)

        if not self.program:
            error = glGetProgramInfoLog(self.program)
            print(f"Ошибка при создании программы шейдеров: {error}")
            return