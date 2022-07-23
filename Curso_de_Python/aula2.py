# print('824', '176', '070', sep='.', end='-')
# print(18)
#
# for x in range(0,101,2):
#     print(x)

from turtle import *
speed(10)
color("green")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b*3)
    b = b - 1
