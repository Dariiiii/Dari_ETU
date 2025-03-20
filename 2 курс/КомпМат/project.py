import numpy as np
import random
import matplotlib.pyplot as plt

# Параметры генератора: фаза, частота, амплитуда, шум и количество измерений в секунду
phase = 0  # np.pi / 4
freq = 35
measurements_per_sec = 100
amplitude = 5
noise = 0.1

# равномерная временная сетка
endtime = 2
uniform_time = np.linspace(0, endtime, endtime * measurements_per_sec)

# неравномерная временная сетка
uneven_time = []
for i in range(endtime):
    for j in range(measurements_per_sec):
        uneven_time.append(random.random() + i)
uneven_time = np.sort(np.array(uneven_time))

# y(t) = A * sin(ω*t + φ) + ε
# сигнал для равномерной временной сетки
first_signal = amplitude * np.sin(2 * np.pi * freq * uniform_time + phase) + noise * np.random.randn(len(uniform_time))

# сигнал для неравномерной временной сетки
second_signal = amplitude * np.sin(2 * np.pi * freq * uneven_time + phase) + noise * np.random.randn(len(uneven_time))


# неравномерное преобразование Фурье
def nufft(signal, time):
    N = len(time)
    f = [0] * N
    p = time / time[-1]
    for k in range(N):
        for n in range(N):
            f[k] += signal[n] * np.exp(-2j * np.pi * p[n] * k)
    return f


# поиск массива частот для заданной размерности
def fftfreq(n, m):
    k = np.arange(0, n)
    f = k / n
    f[k > n // 2] = (k[k > n // 2] - n) / n
    return f * m


# поиск частосты
def frequency_search(freqs, fft_signal):
    restore_frequency = -1
    max_signal = fft_signal[0]
    for ind, frequency in enumerate(np.abs(freqs)):
        if fft_signal[ind] > max_signal:
            restore_frequency = frequency
            max_signal = fft_signal[ind]
    return restore_frequency


# для равномерной временной сетки
plt.plot(uniform_time, first_signal, label='Signal for a uniform time grid')
plt.legend()
plt.show()

first_freqs = fftfreq(len(first_signal), measurements_per_sec)
first_fft_signal = nufft(first_signal, uniform_time)
first_fft_signal = np.abs(first_fft_signal)
plt.scatter(first_freqs, first_fft_signal, s=2, label='Signal spectrum')
plt.legend()
plt.show()
print(f"Restored Frequency: {frequency_search(first_freqs, first_fft_signal)}")

# для неравномерной временной сетки
plt.plot(uneven_time, second_signal, label='Signal for a uneven time grid')
plt.legend()
plt.show()

second_freqs = fftfreq(len(second_signal), measurements_per_sec)
second_fft_signal = nufft(second_signal, uneven_time)
second_fft_signal = np.abs(second_fft_signal)
plt.scatter(second_freqs, second_fft_signal, s=2, label='Signal spectrum')
plt.legend()
plt.show()
print(f"Restored Frequency: {frequency_search(second_freqs, second_fft_signal)}")

