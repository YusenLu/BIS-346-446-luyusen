# Exercise 7.14
import numpy as np

arry1 = np.array([[0, 1], [2, 3]])
arry1

arry2 = np.array([[4, 5], [6, 7]])
arry2

arry3 = np.vstack((arry1, arry2))
arry3

arry4 = np.hstack((arry1, arry2))
arry4 

arry5 = np.vstack((arry4, arry4))
arry5

arry6 = np.hstack((arry3, arry3))
arry6
