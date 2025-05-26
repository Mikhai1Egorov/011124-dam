# 🔢 Математические операции в NumPy

import numpy as np

two = np.array(["Hello"])

# 📌 Базовые арифметические операции с массивами

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Сложение массива с самим собой:\n", two_d_array + two_d_array)
print("Поэлементное умножение массива на самого себя:\n", two_d_array * two_d_array)
print("Умножение на число:\n", two_d_array * 5)
print("Прибавление числа:\n", two_d_array + 10)

# 📌 Broadcasting (расширение размерностей)
one_d_array = np.array([10, 20, 30])
print("Broadcasting (одномерный массив + двумерный):\n", one_d_array + two_d_array)

col = np.array([[10], [20]])
print("Broadcasting (вектор-столбец + двумерный массив):\n", col + two_d_array)

# 📌 Объединение массивов
col = np.array([1, 2])
row = np.array([3, 4, 5])
print("Объединение массивов:\n", np.concatenate([col, row]))

# 📌 Арифметика, бесконечности и NaN
a = np.array([0, 2, 1])
b = np.array([3, 4, 5])
print("Вычитание:", a - b)
print("Деление:", a / b)
print("Степень:", a ** b)
print("Деление на ноль (возникает inf):", b / a)
print("0.0 / 0.0 -> nan:", np.array([0.0]) / 0.0)
print("inf / inf -> nan:", np.array([np.inf]) / np.inf)

# 📌 Универсальные функции (ufunc), сравнения, логика
print("Синус поэлементно:", np.sin(a))
print("Сравнение (a > b):", a > b)
print("Хотя бы одно True:", np.any(a >= 2))
print("Все элементы True:", np.all(a >= 2))

# 📌 Статистика и агрегаты
d = np.array([1, 5, 6])
print("Сумма:", d.sum(), "Произведение:", d.prod(), "Максимум:", d.max(), "Минимум:", d.min())
print("Среднее:", d.mean(), "Ст. отклонение:", d.std())

# 📌 Полезные математические функции
print("Корень из элементов b:", np.sqrt(b))
print("Экспонента b:", np.exp(b))
print("Логарифм b:", np.log(b))
print("Синус b:", np.sin(b))
print("Константы e и pi:", np.e, np.pi)
print("Кумулятивная сумма b:", b.cumsum())

# ✅ Упражнение: косинусы
x = np.linspace(-2 * np.pi, 2 * np.pi, 20)
print("Квадраты косинусов не превышают 1:", np.all(np.cos(x)**2 <= 1))

import numpy as np
import time

# ✅ Вопрос: Как эффективность хранения данных в NumPy влияет на производительность?
# Ответ: NumPy использует компактное представление (однородный тип, непрерывный блок памяти),
# что позволяет быстрее производить операции (векторизация, SIMD) и экономит память.

a = np.arange(1_000_000)
b = np.arange(1_000_000)

start = time.time()
c = a + b
end = time.time()

print("Сложение NumPy:", end - start, "секунд")  # очень быстро!

# ✅ Вопрос: Что будет при делении массива на массив, содержащий нули?
# Ответ: Будет предупреждение, но не ошибка. Возвращаются значения `inf`, `-inf`, `nan` в зависимости от ситуации.

a = np.array([1, 2, 0, -4])
b = np.array([1, 0, 0, 2])

result = a / b
print("Результат деления:", result)  # [ 1. inf nan -2.]

# Проверка на бесконечность и NaN
print("Является бесконечностью:", np.isinf(result))
print("Является NaN:", np.isnan(result))

# ✅ Вопрос: Что такое np.nan, np.inf и как с ними работать?
# Ответ: `np.nan` — "не число" (например, 0/0). `np.inf` — бесконечность.
# Это float-значения, которые можно проверять через `np.isnan`, `np.isinf`.

arr = np.array([1, np.nan, 3, np.inf, -np.inf])

print("nan:", np.isnan(arr))         # [False  True False False False]
print("inf:", np.isinf(arr))         # [False False False  True  True]
print("finite:", np.isfinite(arr))   # [ True False  True False False]

# ✅ Вопрос: Чем отличаются списки от массивов при арифметике?
# Ответ: Списки не поддерживают поэлементную арифметику: `list * 2` удваивает список,
# а `array * 2` — каждый элемент. Массивы эффективнее и поддерживают операции как в математике.

lst = [1, 2, 3]
print("Список * 2:", lst * 2)  # [1, 2, 3, 1, 2, 3]

arr = np.array([1, 2, 3])
print("Массив * 2:", arr * 2)  # [2 4 6]

# ✅ Вопрос: Что такое broadcasting?
# Ответ: Broadcasting — это автоматическое расширение размерностей массива,
# чтобы можно было выполнять операции над несовпадающими по форме массивами.

a = np.array([1, 2, 3])
b = 10
print("Broadcast scalar:", a + b)  # [11 12 13] — 10 «растягивается» на каждый элемент

m = np.array([[1], [2], [3]])
n = np.array([10, 20, 30])
print("Broadcast row + column:\n", m + n)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]