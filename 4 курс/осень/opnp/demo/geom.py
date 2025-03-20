import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Папка с изображениями
image_folder = 'C:/Users/79064/Desktop/etu/4/opnp/test img/'

def detect_shapes(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices = len(approx)

        if vertices == 3:
            shape_name = "Triangle"
        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
        elif vertices == 5:
            shape_name = "Pentagon"
        else:
            shape_name = "Circle"

        # Рисуем контур и название формы на изображении
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            # Цвет текста - красный
            cv2.putText(image, shape_name, (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Обрабатываем изображения с именами от "1.png" до "10.png"
for i in range(1, 11):
    image_path = os.path.join(image_folder, f'{i}.png')
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        continue
    
    detect_shapes(img)

    # Отображаем результат с помощью Matplotlib
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f"Detected Shapes in Image {i}")
    plt.axis('off')
    plt.show()