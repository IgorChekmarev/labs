from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
#https://pyprog.pro/mpl/mpl_main_components.html

# P = 0.099 * N - 7.24 [мм рт.ст]
def Pressure(N):
    P = 0.099 * N - 7.24
    return P

with open("Kostya.txt", "r") as file:
    array_rest_pressure = [Pressure(int(i)) for i in file.read().split("\n")]

array_time = []
for i in range(0, len(array_rest_pressure)):
    array_time.append(i * (60 / len(array_rest_pressure)))

step = 1040
step_pulse = array_rest_pressure[::step]
time_pulse = array_time[::step]
pulse = [step_pulse[i] - step_pulse[i - 1] for i in range(1, len(step_pulse))]

array_delta_pressure = []
# #Функция определения координат минимумов пульсов
# cords = []
# k = 0
# t = 120
# for i in range(121, len(array_rest_pressure) - 121):
#     if t <= len(array_rest_pressure) - 121:
#         t = t + 1
#         if k == 240:
#             t = t + 120
#             if t > 0:
#                 cords.append(t - 121)
#                 print(array_time[t])
#         k = 0
#         if array_rest_pressure[t-120] > array_rest_pressure[t] and array_rest_pressure[t] < array_rest_pressure[t+120]:
#             for j in range(t-120, t+120):
#                 if array_rest_pressure[t] <= array_rest_pressure[j]:
#                     k = k + 1

# #Определение кол-ва ударов в минуту по минимумам пульсов на графике:
# D = str(int(round(((len(cords) - 2) / (array_time[cords[len(cords) - 1]] - array_time[cords[2]])) * 60, 2)))
#
# #Формирование амплитудного графика давлений
# for i in range(cords[0], len(array_rest_pressure)):
#     for j in range(0, len(cords) - 1):
#         if i == cords[j]:
#             m = (cords[j] + cords[j+1]) // 2 + 60
#             for index in range (cords[j], cords[j + 1]):
#                 array_delta_pressure.append((array_rest_pressure[index] - array_rest_pressure[m])/2.3)

# #Формирование массива времени для этого графика
# array_time_delta = []
# for i in range(0, len(array_delta_pressure)):
#     array_time_delta.append(i * (60 / len(array_rest_pressure)))

#Чёрная линия
massive = []
for l in range(0, len(pulse)):
    massive.append(0)

#считываем показания
data = numpy.array(pulse)
data_0 = numpy.array(massive)
#считываем показания
data_time = numpy.array(time_pulse)
#параметры фигуры
fig, ax = pyplot.subplots(figsize=(16, 9), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([9.4, 30 + 0, -2, 2])

#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2.5))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Пульс в спокойном состоянии (Костя)', 40)), fontsize = 30, pad = 20, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')


#подпись осей
ax.set_ylabel("Изменение давления в артерии [мм рт.ст.]", fontsize = 16)
ax.set_xlabel("Время [с]", fontsize = 16)

#Добавление самого графика и (в конце присваивает наличие леге label =...)
ax.plot(data_time[:-1], data, c='orange', linewidth=1, label ='Пульс - 91 [уд/мин]')
ax.plot(data_time[:-1], data_0, c='k', linewidth=1)

#маркеры
# ----
#Добавил маркеры в легенду с надписью измерения

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper right', fontsize = 17)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html
ax.text(70, 605, '', rotation = 0, fontsize = 24)

#сохранение
fig.savefig('rest-pulse.png')