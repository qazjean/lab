import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Настройка фигуры и осей
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 2 * np.pi) #до 2пи. по дуге вниз и вверх)
ax.set_ylim(-1.1, 1.1)
ax.grid(alpha=0.8) #прозрачность сетки
ax.set_title("Пошаговая анимация sin(x)", fontsize=14)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("sin(x)", fontsize=12)

# Инициализация графических элементов
line, = ax.plot([], [], 'r-', lw=2, label='sin(x)')
current_point, = ax.plot([], [], 'pink', ms=8) #точка для текущей позиции
#ax.plot() возвращает список объектов (даже если создаётся одна линия). Запятая в конце распаковывает список,
# присваивая переменной line сам объект линии, а не список.
ax.legend(loc='upper right') #Доббавила легенду

# Генерация данных
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)


# Функции анимации
def init():
    line.set_data([], [])
    current_point.set_data([], [])
    return line, current_point,


def animate(frame):
    # Обновляем линию
    line.set_data(x[:frame], y[:frame])

    # Обновляем текущую точку
    if frame > 0:
        # Передаем данные как списки [x], [y]
        current_point.set_data([x[frame - 1]], [y[frame - 1]])
    else: #это начальный кадр
        current_point.set_data([], [])

    # изменение цвета (красиви). frame/100 преобразует номер кадра в значение от 0.0 до 1.0.
    line.set_color(plt.cm.viridis(frame / 100))

    return line, current_point, #запятая в конце превращает возвращаемые значения в кортеж,
    # как требует FuncAnimation.


# Создание анимации
ani = FuncAnimation(
    fig=fig,
    func=animate,
    frames=len(x) + 1,
    init_func=init,
    interval=20, #задержка между кадрами
    blit=True  #перерисовывает только измененные части графика
)

ani.save('sin_animation.gif', writer='pillow', fps=20) #сохранить у меня вышло только в таком формате
