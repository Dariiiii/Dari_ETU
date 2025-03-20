import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

astronomical_unit = 149597870700  # астрономическая единица
step = 200  # шаг - 200 секунд
nt = 4500  # количество шагов
# наблюдения начались 21 января 2023 года 8 ч 13 мин 54 с
# закончились 31 января 2023 17 ч 39 мин 24 с
GM_SUN = 132712440043.85333e9
coordinates_SUN = np.loadtxt('Sun.txt', dtype='float')

GM_EARTH = 398600.43552e9
coordinates_EARTH = np.loadtxt('Earth.txt', dtype='float')

GM_JUPITER = 126712764.13345e9
coordinates_JUPITER = np.loadtxt('Jupiter.txt', dtype='float')

GM_MARS = 42828.37521e9
coordinates_MARS = np.loadtxt('Mars.txt', dtype='float')

GM_SATURN = 37940585.20000e9
coordinates_SATURN = np.loadtxt('Saturn.txt', dtype='float')

GM_2023BU = 0
x_2023BU = -137749744808.6816 + coordinates_SUN[0, 0]
y_2023BU = 59076551415.83601 + coordinates_SUN[0, 1]
z_2023BU = 5102548312.272886 + coordinates_SUN[0, 2]
vx_2023BU = -13851.933889925379
vy_2023BU = -27809.521725242163
vz_2023BU = 1796.8628003746991

comet_info = np.array([x_2023BU, y_2023BU, z_2023BU, vx_2023BU, vy_2023BU, vz_2023BU])


def model(previous_data_index, comet_info):
    x, y, z, vx, vy, vz = comet_info
    r_Sun = np.sqrt(
        (x - coordinates_SUN[previous_data_index, 0]) ** 2 + (y - coordinates_SUN[previous_data_index, 1]) ** 2 + (
                    z - coordinates_SUN[previous_data_index, 2]) ** 2)
    r_Saturn = np.sqrt((x - coordinates_SATURN[previous_data_index, 0]) ** 2 + (
                y - coordinates_SATURN[previous_data_index, 1]) ** 2 + (
                                   z - coordinates_SATURN[previous_data_index, 2]) ** 2)
    r_Mars = np.sqrt(
        (x - coordinates_MARS[previous_data_index, 0]) ** 2 + (y - coordinates_MARS[previous_data_index, 1]) ** 2 + (
                    z - coordinates_MARS[previous_data_index, 2]) ** 2)
    r_Earth = np.sqrt(
        (x - coordinates_EARTH[previous_data_index, 0]) ** 2 + (y - coordinates_EARTH[previous_data_index, 1]) ** 2 + (
                    z - coordinates_EARTH[previous_data_index, 2]) ** 2)
    r_Jupiter = np.sqrt((x - coordinates_JUPITER[previous_data_index, 0]) ** 2 + (
                y - coordinates_JUPITER[previous_data_index, 1]) ** 2 + (
                                    z - coordinates_JUPITER[previous_data_index, 2]) ** 2)
    drx_dt = vx
    dry_dt = vy
    drz_dt = vz
    dvx_dt = GM_SUN * (coordinates_SUN[previous_data_index, 0] - x) / (r_Sun ** 3) + GM_MARS * (
                coordinates_MARS[previous_data_index, 0] - x) / (r_Mars ** 3) + GM_SATURN * (
                         coordinates_SATURN[previous_data_index, 0] - x) / (r_Saturn ** 3) + GM_EARTH * (
                         coordinates_EARTH[previous_data_index, 0] - x) / (r_Earth ** 3) + GM_JUPITER * (
                         coordinates_JUPITER[previous_data_index, 0] - x) / (r_Jupiter ** 3)
    dvy_dt = GM_SUN * (coordinates_SUN[previous_data_index, 1] - y) / (r_Sun ** 3) + GM_MARS * (
                coordinates_MARS[previous_data_index, 1] - y) / (r_Mars ** 3) + GM_SATURN * (
                         coordinates_SATURN[previous_data_index, 1] - y) / (r_Saturn ** 3) + GM_EARTH * (
                         coordinates_EARTH[previous_data_index, 1] - y) / (r_Earth ** 3) + GM_JUPITER * (
                         coordinates_JUPITER[previous_data_index, 1] - y) / (r_Jupiter ** 3)
    dvz_dt = GM_SUN * (coordinates_SUN[previous_data_index, 2] - z) / (r_Sun ** 3) + GM_MARS * (
                coordinates_MARS[previous_data_index, 2] - z) / (r_Mars ** 3) + GM_SATURN * (
                         coordinates_SATURN[previous_data_index, 2] - z) / (r_Saturn ** 3) + GM_EARTH * (
                         coordinates_EARTH[previous_data_index, 2] - z) / (r_Earth ** 3) + GM_JUPITER * (
                         coordinates_JUPITER[previous_data_index, 2] - z) / (r_Jupiter ** 3)
    coefficients = np.array([drx_dt, dry_dt, drz_dt, dvx_dt, dvy_dt, dvz_dt])
    return coefficients


def RungeKutta4(t_last, h, data0):
    comet = np.zeros((t_last, data0.size))
    comet[0, :] = data0
    for i in range(t_last - 1):
        k1 = h * model(i, comet[i,:])
        k2 = h * model(i,comet[i,:] + k1/2)
        k3 = h * model(i,comet[i,:] + k2/2)
        k4 = h * model(i,comet[i,:] + k3)
        delta =(k1 + 2*k2 + 2*k3 + k4)/6
        comet[i+1,:] = comet[i,:] + delta
    return comet

def plot(array):
    figure = plt.figure()
    _3D = figure.add_subplot(projection='3d')
    _3D.plot(array[:,0], array[:,1], array[:,2], label='Comet 2023BU')
    _3D.plot(coordinates_SUN[:,0], coordinates_SUN[:,1], coordinates_SUN[:,2], label='SUN', marker='.', markersize=30)
    _3D.plot(coordinates_EARTH[:,0],coordinates_EARTH[:,1], coordinates_EARTH[:,2], label='Earth', marker='.', markersize=15)
    _3D.plot(coordinates_JUPITER[:,0],coordinates_JUPITER[:,1], coordinates_JUPITER[:,2], label='Jupiter', marker='.', markersize=20)
    _3D.plot(coordinates_MARS[:,0],coordinates_MARS[:,1], coordinates_MARS[:,2], label='Mars', marker='.', markersize=15)
    _3D.plot(coordinates_SATURN[:,0],coordinates_SATURN[:,1], coordinates_SATURN[:,2], label='Saturn', marker='.', markersize=20)
    _3D.legend()
    plt.show()

result = RungeKutta4(nt,step,comet_info)

plot(result)