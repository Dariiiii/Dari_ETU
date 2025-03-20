#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

// структура для хранения квадратов
// x и y координаты левого верхнего угла квадрата
// size размер квадрата
struct Square {
    int x;
    int y;
    int size;
} typedef Square;

// функция для поиска наименьших простых делителей числа (от 2 до 5)
int find_coefficient(int N) {
    for (int i = 2; i < 6; i++) {
        if (N % i == 0)
            return i;
    }
    return N;
}

// функция для возвращение исходного размера квадрата
void original_size(std::vector<Square> &squares, int coefficient) {
    for (int i = 0; i < squares.size(); i++) {
        squares[i].x *= coefficient;
        squares[i].y *= coefficient;
        squares[i].size *= coefficient;
    }
}

// функция для проверки находится ли точка внутри квадрата или нет
bool is_inside(std::vector<Square> squares, int x, int y) {
    for (int i = 0; i < squares.size(); i++) {
        if (x >= squares[i].x && x < squares[i].x + squares[i].size && y >= squares[i].y &&
            y < squares[i].y + squares[i].size)
            return true;
    }
    return false;
}

// функция, обеспечивающая корректный вывод
void print(std::vector<Square> record_list) {
    for (int i = 0; i < record_list.size(); i++) {
        std::cout << record_list[i].x + 1 << " " << record_list[i].y + 1 << " " << record_list[i].size << "\n";
    }
}

// фунция для сборки большого квадрата из множества квадратов меньшего размера 
void assembly(std::vector<Square> &squares, int S, int xmin, int ymin, int &k, int &record,
              std::vector<Square> &record_list) {
    for (int x = xmin; x < k; x++) {
        for (int y = ymin; y < k; y++) {
            if (!(is_inside(squares, x, y))) {
                int length = std::min(k - x, k - y);
                for (auto each: squares) {
                    if (each.x + each.size > x && each.y > y) {
                        length = std::min(length, each.y - y);
                    }
                }
                for (int i = length; i > 0; i--) {
                    Square s;
                    s.x = x;
                    s.y = y;
                    s.size = i;
                    std::vector<Square> tmp = {squares.begin(), squares.end()};
                    tmp.push_back(s);
                    if (S + s.size * s.size == k * k) {
                        if (tmp.size() < record) {
                            record = tmp.size();
                            record_list = {tmp.begin(), tmp.end()};
                        }
                    } else {
                        if (tmp.size() < record + 1)
                            assembly(tmp, S + s.size * s.size, x, y + i, k, record, record_list);
                        else {
                            return;
                        }
                    }
                }
                return;
            }
        }
        ymin = int(k / 2);
    }
}

int main() {
    int N;
    std::cin >> N;
    int coefficient = find_coefficient(N);
    int record = 2 * N + 1;
    std::vector<Square> record_list;
    std::vector<Square> squares;
    Square tmp = {0, 0, int((coefficient + 1) / 2)};
    squares.push_back(tmp);
    tmp = {0, int((coefficient + 1) / 2), int(coefficient / 2)};
    squares.push_back(tmp);
    tmp = {int((coefficient + 1) / 2), 0, int(coefficient / 2)};
    squares.push_back(tmp);
    assembly(squares, int((coefficient + 1) / 2) * int((coefficient + 1) / 2) +
                      2 * (int(coefficient / 2) * int(coefficient / 2)), int(coefficient / 2),
             int((coefficient + 1) / 2), coefficient, record, record_list);
    if (coefficient != N)
        original_size(record_list, int(N / coefficient));
    printf("%d\n", record);
    print(record_list);
}