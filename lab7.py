import time
import numpy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# task №1
def comparison():
    array_One = [random.randint(0, 1000000) for i in range(1000000)]
    array_Two = [random.randint(0, 1000000) for i in range(1000000)]
    time_One = time.perf_counter()

    for i in range(1000000):
        prod = array_One[i] * array_Two[i]

    time_Two = time.perf_counter()
    delta_One = time_Two - time_One

    arrOne = np.array(array_One)
    arrTwo = np.array(array_Two)
    time_One = time.perf_counter()
    numpy.multiply(arrOne, arrTwo)
    time_Two = time.perf_counter()
    delta_Two = time_Two - time_One
    print('время без использования нампи и мультиплу: ', delta_One)
    print('время и использованием нампи и мультиплу: ', delta_Two)



# task №2
def hist():
    arr = np.genfromtxt('data1.csv', delimiter=';')
    arr = arr[1:]               # убираем названия колонок
    
    time = arr[:, 0]            # считываем 1 столбец - время
    place = arr[:, 3]           # считываем 4 столбец - данные о положении заслонки
    turnovers = arr [:, 4]      # считываем 5 столбец - количество оборотов двигателя
  
    plt.plot(time, place)       # зависимость положения заслонки от времени
    plt.plot(time, turnovers)   # зависимость оборотов двигателя от времени
    plt.xlabel('время')
    plt.legend(['зависимость положения заслонки от времени', 'зависимость оборотов двигателя от времени'])
    plt.show()
   
    # график корелляции
    plt.plot(place, turnovers, 'ro')  
    plt.title('график корелляции')
    plt.xlabel('положение заслонки')
    plt.ylabel('обороты двигателя')

    plt.show()



#  task 3
def plot3d():
    x_coord = np.linspace(-np.pi, np.pi, 70)      # заданный диапазон
    y_coord = x_coord                                   # функции
    z_coord = np.tan(x_coord)                           

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_coord, y_coord, z_coord, label='parametric curve')
    plt.title('y=x;   z=tg(x)')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()



if __name__ == '__main__':
    comparison()
    hist()
    plot3d()



