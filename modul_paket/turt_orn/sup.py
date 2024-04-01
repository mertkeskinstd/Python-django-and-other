from turtle import *
import colorsys

bgcolor("black")

speed(0)
bgcolor("black")
h=0
for i in range(16):
    for j in range(18):
        c=colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.05
        rt(90)
        circle(150-j *6,90)
        lt(90)
        circle(150-i *6,90)
        rt(160)
        circle(150-j *6,90)
        lt(160)
        circle(150-i *6,90)
        rt(270)
        circle(150-j *6,90)
        lt(270)
        