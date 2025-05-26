import numpy as np

# 📌 ОДНОМЕРНЫЙ МАССИВ
one_d_array = np.array([1, 2, 3])
print("Одномерный массив:", one_d_array)

# 📌 ДВУМЕРНЫЙ МАССИВ
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Двумерный массив:\n", two_d_array)

# Альтернативный способ создания
list_2d = [[1, 2], [3, 4]]
two_d_array = np.array(list_2d)
print("Двумерный массив из list_2d:\n", two_d_array)

# 📌 ВЕКТОР-СТОЛБЕЦ
col = np.array([[10], [20]])
print("Вектор-столбец:\n", col)

# 📌 ФУНКЦИИ СОЗДАНИЯ МАССИВОВ

# Базовый массив для *_like функций
base_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\nБазовый массив:\n", base_array)

# empty_like — пустой массив с той же формой (значения случайные)
empty_arr = np.empty_like(base_array)
print("\nempty_like:\n", empty_arr)

# ones_like — массив из 1 с той же формой
ones_arr = np.ones_like(base_array)
print("\nones_like:\n", ones_arr)

# zeros_like — массив из 0 с той же формой
zeros_arr = np.zeros_like(base_array)
print("\nzeros_like:\n", zeros_arr)

# full_like — массив, заполненный значением
full_arr = np.full_like(base_array, 99)
print("\nfull_like (значение 99):\n", full_arr)

# empty — пустой массив заданной формы
empty_direct = np.empty((2, 3))
print("\nempty (2x3):\n", empty_direct)

# ones — массив из 1 заданной формы
ones_direct = np.ones((2, 3))
print("\nones (2x3):\n", ones_direct)

# zeros — массив из 0 заданной формы
zeros_direct = np.zeros((2, 3))
print("\nzeros (2x3):\n", zeros_direct)

# full — массив из одного значения заданной формы
full_direct = np.full((2, 3), 7)
print("\nfull (2x3, значение 7):\n", full_direct)

# 📌 arange — массив с шагом
a = np.arange(0, 9, 2)
print("\narange от 0 до 9 с шагом 2:", a)

b = np.arange(0., 8, 2)
print("arange с float:", b)

# 📌 linspace — равномерная последовательность
lin = np.linspace(10, 20, 21)
print("\nlinspace от 10 до 20 (21 число):\n", lin)

# 📌 ТРЕХМЕРНЫЙ МАССИВ
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D массив:\n", three_d_array)
print("Размерность:", three_d_array.ndim)
print("Форма:", three_d_array.shape)
print("Длина (len):", len(three_d_array))
print("Всего элементов:", three_d_array.size)

# 📌 ЗАДАНИЕ: Сколько строк и столбцов?
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])
print("\nМатрица:\n", array)
print("Форма:", array.shape)  # (4, 3)
print("len(array):", len(array))  # 4 строки

# 📌 Типизация в NumPy
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\nint массив:\n", two_d_array)

two_d_array = np.array([[1, 2, 3.0], [4, 5, 6]])
print("float массив:\n", two_d_array)

two_d_array = np.array([[1, 2, 3], ["A", "B", "C"]])
print("строки и числа → строки:\n", two_d_array)

two_d_array = np.array([[1, 2, 3], ["A", "B", "C"*28]])
print("длинная строка влияет на dtype:\n", two_d_array)

# 📌 Размер элемента в байтах
print("\nitemsize int:", np.array([1, 2, 3]).itemsize)
print("itemsize str:", np.array([[1, 2, 3], ["A", "B", "C"]]).itemsize)

# Пример обрезки строки при недостаточном dtype
a = np.array([[1, 2, 3], ["A", "B", "C"]])
a[0][0] = "a"*10+"b"*10
print("обрезанная строка в массиве:", a)

# 📌 Преобразование между списками и массивами
list_int_str = [[1, 2, 3], ["A", "B", "C"]]
print("\nСписок int/str:", list_int_str)

list_int_float = [[1, 2, 3.0], [4, 5, 6]]
print("Список int/float:", list_int_float)

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("to list:", two_d_array.tolist())

# 📌 Задание: массив с типом float64
float_array = np.array([1, 2, 3], dtype=np.float64)
print("\nfloat64 массив:", float_array)
print("Тип данных:", float_array.dtype)

# 📌 astype — смена типа данных
int_array = np.array([1, 2, 3], dtype=np.int8)
print("astype → float:", int_array.astype(np.float32))

# 📌 Примеры операций
arr = np.array([1, 2, 3, 4, 5])
print("\narr[1] + arr[3] = ", arr[1] + arr[3])  # 6

arr = np.array([1.0, 2, 3])
print("Тип данных при смешивании float и int:", arr.dtype)

arr = np.arange(5, 15, 2)
print("arange(5, 15, 2):", arr)

# 📌 ЗАДАНИЕ: случайный одномерный массив
rand_arr = np.random.randint(0, 100, size=5)
print("\nСлучайный массив:", rand_arr)
print("Тип:", type(rand_arr))
print("Размер:", rand_arr.shape)

# 📌 ЗАДАНИЕ: массив 3x4 из 1
ones_3x4 = np.ones((3, 4))
print("Массив 3x4 из 1:", ones_3x4)

# 📌 ЗАДАНИЕ: arange и linspace
ar = np.arange(0, 11, 2)
ls = np.linspace(0, 10, 6)
print("arange:", ar)
print("linspace:", ls)
print("Совпадают ли значения?", np.allclose(ar, ls))

np.array([1, 2, 3])            # 1D массив
np.array([[1, 2], [3, 4]])     # 2D массив
np.zeros((2, 3))               # массив из 0
np.ones((3, 1))                # массив из 1
np.full((2, 2), 7)             # массив из 7
np.eye(3)                      # единичная матрица
np.arange(0, 10, 2)            # [0 2 4 6 8]
np.linspace(0, 1, 5)           # равномерно от 0 до 1
np.random.rand(2, 2)           # случайные числа
np.empty((2, 2))               # пустой (мусор)

a.shape          # форма массива
a.ndim           # количество измерений
a.dtype          # тип данных
a.size           # общее количество элементов
a.itemsize       # размер одного элемента (в байтах)
a.nbytes         # общий размер массива (в байтах)

a[0]             # элемент
a[1:3]           # срез
a[:, 0]          # первый столбец
a[1, 2]          # строка 2, столбец 3
a[-1]            # последний элемент

a.reshape((2, 3))     # новая форма
a.ravel()             # в 1D
a.T                   # транспонирование
a.flatten()           # копия в 1D

a + b                 # поэлементное сложение
a - b                 # вычитание
a * b                 # умножение
a / b                 # деление
a ** 2                # возведение в степень
np.add(a, b)          # то же самое
np.dot(a, b)          # скалярное или матричное произведение
np.exp(a)             # экспонента
np.sqrt(a)            # корень
np.log(a)             # логарифм
