from numpy import log2
from alg_ShF import encode_ShF_str
from alg_stH import encode_stH_str
from alg_dinH import encode_dinH_str
from time import time_ns as time
import matplotlib.pyplot as plt

string = "☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^ _`abcdefghijklmnopqrstuvwxyz"
length = 500


def measureTime(func, string, codes):
    start = time()
    func(string, codes)
    end = time()
    return (end - start) / (10 ** 9)


if __name__ == "__main__":
    timings = [[], [], []]
    codes = dict()
    for n in range(1, len(string)):
        strToEncode = string[:n] * length
        timings[0].append(measureTime(encode_ShF_str, strToEncode, codes))
        timings[1].append(measureTime(encode_stH_str, strToEncode, codes))
        timings[2].append(measureTime(encode_dinH_str, strToEncode, codes))
    xCoord = range(1, len(string))
    yCoord = timings[0]
    plt.scatter(xCoord, yCoord, color="green")
    a = (yCoord[-1] + yCoord[-2]) / 2 / xCoord[-1] / log2(xCoord[-1])
    yCoord = [a * x * log2(x) for x in xCoord]
    plt.plot(xCoord, yCoord, color="red")
    plt.xlabel("Количество элементов (x500)")
    plt.ylabel("Время")
    plt.legend(["Время работы нашей функции", "a*n*log2n"])
    # plt.show()
    plt.savefig("alg_ShF.png")
    plt.clf()

    yCoord = timings[1]
    plt.scatter(xCoord, yCoord, color="green")
    a = (yCoord[-1] + yCoord[-2]) / 2 / xCoord[-1] / log2(xCoord[-1])
    yCoord = [a * x * log2(x) for x in xCoord]
    plt.plot(xCoord, yCoord, color="red")
    plt.xlabel("Количество элементов (x500)")
    plt.ylabel("Время")
    plt.legend(["Время работы нашей функции", "a*n*log2n"])

    # plt.show()
    plt.savefig("alg_sH.png")
    plt.clf()

    yCoord = timings[2]
    plt.scatter(xCoord, yCoord, color="green")
    # plt.plot(xCoord, yCoord)
    a = yCoord[-1] / xCoord[-1] ** 2
    yCoord = [a * x ** 2 for x in xCoord]
    plt.plot(xCoord, yCoord, color="red")
    plt.xlabel("Количество элементов (x500)")
    plt.ylabel("Время")
    plt.legend(["Время работы нашей функции", "a*n**2 "])
    # plt.show()
    plt.savefig("alg_dinH.png")
    plt.clf()

    print("Finished")
