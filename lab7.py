import time

import numpy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

import tkinter as tk 
from tkinter import ttk
import pygame


# def tableLoad():
#     arr = np.genfromtxt('voltage.csv', delimiter=',')
#     time = arr[:100,0]
#     time = time[:,np.newaxis]
#     curr = arr[:100,1]
#     curr = curr[:,np.newaxis]
#     volt = arr[:100,2]
#     volt = volt[:,np.newaxis]

#     plt.plot(time, curr * 50, 'b', time, volt, 'r')
#     plt.show()




# def plot3d():
#     np.random.seed(40)
#     xs = np.linspace(0, 10, 20)
#     ys = xs
#     zs = np.sin(xs)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot(xs, ys, zs, marker='x', c='red')
#     plt.show()
    


# task №1
def comparison():
    arrayOne = [random.randint(0, 1000000) for i in range(1000000)]
    arrayTwo = [random.randint(0, 1000000) for i in range(1000000)]
    timeOne = time.perf_counter()

    for i in range(1000000):
        x = arrayOne[i] * arrayTwo[i]

    timeTwo = time.perf_counter()
    deltaOne = timeTwo - timeOne

    arrOne = np.array(arrayOne)
    arrTwo = np.array(arrayTwo)
    tOne = time.perf_counter()
    numpy.multiply(arrOne, arrTwo)
    tTwo = time.perf_counter()
    deltaTwo = tTwo - tOne
    print('время без использования нампи и мультиплу: ', deltaOne)
    print('время и использованием нампи и мультиплу: ', deltaTwo)

    # a = [deltaOne, deltaTwo]
    # return a


    
# #  в консоли ничего не видно, решила сделать окошечко
# window = tk.Tk()
# window.geometry('550x400')
# window.title('РАЗНИЦА МЕЖДУ "С НАМПИ И МУЛЬТИПЛУ" И БЕЗ')
# bg_img = tk.PhotoImage(file='may.png')
# lbl = tk.Label( command=comparison, font=('Garamond', 15))
# window.mainloop()




# task №2
def hist():
    arr = np.genfromtxt('data1.csv', delimiter=';')
    arr = arr[1:]               # убираем названия колонок
    # print(arr)
    time = arr[:, 0]            # считываем 1 столбец - время
    place = arr[:, 3]           # считываем 4 столбец - данные о положении заслонки
    turnovers = arr [:, 4]      # считываем 5 столбец - количество оборотов двигателя
  
 
    plt.plot(time, place)       # зависимость положения заслонки от времени
    plt.plot(time, turnovers)   # зависимость оборотов двигателя от времени
    plt.xlabel('время')
    plt.show()
   
    # график корелляции
    plt.plot(place, turnovers, 'ro')  
    plt.title('график корелляции')
    plt.xlabel('положение заслонки')
    plt.ylabel('обороты двигателя')

    plt.show()



#  task 3
def Plot():
    x = np.linspace(-np.pi, np.pi, 70)      # заданный диапазон
    y = x                                   # функции
    z = np.tan(x)                           

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    plt.title('y=x;   z=tg(x)')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()



if __name__ == '__main__':
    #start()
    #tableLoad()
    comparison()
    # hist()
    # Plot()
    # plot3d()

