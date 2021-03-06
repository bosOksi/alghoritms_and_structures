# alghoritms_and_structures
Solving problems for algorithms and data structures

**Task 1. Fibonacci**
Числа Фибоначи
F1 = F2 = 1, Fn = Fn-1 + Fn-2, при n > 2
Входные данные
В единственной строке входных данных записано натуральное число n (1≤n≤45).
Выходные данные
Вывести одно число Fn

Примеры
входные данные
2
выходные данные
1
входные данные
5
выходные данные
5

**Task 2. Stairs**
Мячик на лесенке
На вершине лесенки, содержащей N ступенек, находится мячик, который начинает прыгать по ним вниз, к основанию. Мячик может прыгнуть на следующую ступеньку, на ступеньку через одну или через 2. (То есть, если мячик лежит на 8-ой ступеньке, то он может переместиться на 5-ую, 6-ую или 7-ую.) Определить число всевозможных "маршрутов" мячика с вершины на землю.

Входные данные
Вводится одно число 0 < N < 31.
Выходные данные
Выведите одно число — количество маршрутов.

Примеры
входные данные
4
выходные данные
7

**Task 3. One and Null**
Последовательность из 0 и 1
Требуется подсчитать количество последовательностей длины N, состоящих из 0 и 1, в которых никакие две единицы не стоят рядом.

Входные данные
На вход программы поступает целое число N (1≤N≤100).

Выходные данные
Выведите количество искомых последовательностей.

Примеры
входные данные
1
выходные данные
2

**Task 4. Calc**
Калькулятор
Имеется калькулятор, который выполняет три операции:

Прибавить к числу X единицу.
 Умножить число X на 2.
Умножить число X на 3.
Определите, какое наименьшее число операций необходимо для того, чтобы получить из числа 1 заданное число N.

Входные данные
Программа получает на вход одно число, не превосходящее 106.

Выходные данные
Требуется вывести одно число: наименьшее количество искомых операций.

Примеры
входные данные
1
выходные данные
0
входные данные
5
выходные данные
3
входные данные
32718
выходные данные
17

**Task 5. Calc with answer**
Калькулятор с восстановлением ответа
Имеется калькулятор, который выполняет три операции:

Прибавить к числу X единицу.
Умножить число X на 2.
Умножить число X на 3.
Определите кратчайшую последовательность операций, необходимую для получения из числа 1 заданное число N.

Входные данные
Программа получает на вход одно число N, не превосходящее 106.

Выходные данные
Выведите строку, состоящую из цифр "1", "2" или "3", обозначающих одну из трех указанных операций, которая получает из числа 1 число N за минимальное число операций. Если возможных минимальных решений несколько, выведите любое из них. 😁

Пример

Ввод	Вывод
1 - |

5 
121 |
562340 
3333312222122213312

**Task 6. Сheapest way**
Cамый дешевый путь
В каждой клетке прямоугольной таблицы N×M записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).

Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

Входные данные
Вводятся два числа N и M — размеры таблицы (1≤N≤20, 1≤M≤20). Затем идет N строк по M чисел в каждой — размеры штрафов в килограммах за прохождение через соответствующие клетки (числа от 0 до 100).

Выходные данные
Выведите минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол.

Примеры
входные данные
5 5| 1 1 1 1 1 |
3 100 100 100 100 |
1 1 1 1 1 |
2 2 2 2 1 |
1 1 1 1 1 |
выходные данные
11

**Task 6. Chess**
Ход конем
Дана прямоугольная доска N × M (N строк и M столбцов). В левом верхнем углу находится шахматный конь, которого необходимо переместить в правый нижний угол доски. При этом конь может ходить ТОЛЬКО на две клетки вниз и на одну клетку вправо, либо на две клетки вправо и на одну клетку вниз.
Необходимо определить, сколько существует различных маршрутов, ведущих из левого верхнего в правый нижний угол.
 

Входные данные
В первой строке входного файла находятся два натуральных числа N и M (1 <= N, M <= 50).  

Выходные данные
В выходной файл выведите единственное число количество способов добраться конём до правого нижнего угла доски.

Примеры
входные данные
4 4
выходные данные
2

**Task 7. Longest common subsequence**
Наибольшая общая подпоследовательность
Даны две последовательности, требуется найти длину их наибольшей общей подпоследовательности.

Входные данные
В первой строке входных данных содержится число N – длина первой последовательности (1 ≤ N ≤ 1000). Во второй строке заданы члены первой последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

В третьей строке записано число M – длина второй последовательности (1 ≤ M ≤ 1000). В четвертой строке задаются члены второй последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

Выходные данные
Требуется вывести одно число – длину  наибольшей общей подпоследовательности двух данных последовательностей или 0, если такой подпоследовательности нет.

Примеры
входные данные
3
1 2 3
3 
2 3 1
выходные данные
2
