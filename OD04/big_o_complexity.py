import matplotlib.pyplot as plt
import numpy as np

# Размеры входных данных
n = np.linspace(1, 100, 100)

# Временные сложности
O_1 = np.ones_like(n)
O_log_n = np.log(n)
O_n = n
O_n_log_n = n * np.log(n)
O_n2 = n**2
O_2n = 2**n

# Создание графиков
plt.figure(figsize=(12, 8))

plt.plot(n, O_1, label="O(1)", color="blue")
plt.plot(n, O_log_n, label="O(log n)", color="orange")
plt.plot(n, O_n, label="O(n)", color="green")
plt.plot(n, O_n_log_n, label="O(n log n)", color="red")
plt.plot(n, O_n2, label="O(n^2)", color="purple")
plt.plot(n, O_2n, label="O(2^n)", color="brown")

# Настройка графиков
plt.yscale("log")
plt.xlabel("Размер входных данных (n)")
plt.ylabel("Операции")
plt.title("Сравнение временных сложностей алгоритмов")
plt.legend()
plt.grid(True)
plt.show()
