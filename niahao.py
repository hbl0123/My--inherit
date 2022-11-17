#利用海龟画图先引入"函数turtle"
#再利用里面的函数"write""color""forward""goto"...
'''
import turtle
turtle.showturtle()
turtle.write("你好")
turtle.forward(300)
turtle.color("yellow")
turtle.left(90)
turtle.forward(300)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,300)
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,50)
turtle.goto(50,50)
turtle.circle(100)
turtle.circle(500)
'''
#利用海龟画图画出奥运五环
'''
import turtle

turtle.width(10)#改变宽度的函数


turtle.color("blue")
turtle.circle(50)

turtle.penup()

turtle.goto(120,0)

turtle.pendown()

turtle.color("black")

turtle.circle(50)

turtle.penup()

turtle.goto(240,0)

turtle.pendown()

turtle.color("red")

turtle.circle(50)

turtle.penup()

turtle.goto(50,-50)

turtle.pendown()

turtle.color("yellow")

turtle.circle(50)

turtle.penup()

turtle.goto(200,-50)

turtle.pendown()

turtle.color("green")

turtle.circle(50)
'''
#利用海龟画图来计算两点之间的距离
'''
import turtle
import math
x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

turtle.penup()

turtle.goto(x1,y1)

turtle.pendown()

turtle.goto(x2,y2)

turtle.goto(x3,y3)

turtle.goto(x4,y4)

distance = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)

turtle.write(distance)
'''
#不换行打印，可以通过参数"end"="任意字符串"
'''
print("aa",end = "##")
print("bb",end = "\t")

print("cc")
print("nihao",end =  "你好")

print("哈哈")
'''
#温故知新，比较字符"+"和函数"join()"之间的差距
#比较结果：字符"+"在进行大量运算时"时间效率"，"空间效率"比较低
#原因：字符"+"在进行运算的时候会生成新的的变量，而函数"join()"不会
#运用的函数"time"是以"unix时间点"为标准，即"1970年1月1日00：00：00"
'''
import time
time01 = time.time()    #开始时间
a =''
for i in range(1000000):
    a +='sxt'

time02 = time.time()    #终止时间

print('运算时间'+str(time02-time01))

time03 = time.time()    #开始时间
li =[]
for i in range(1000000):
    li.append("sxt")


a = ''.join(li)
time04 = time.time()    #终止时间
print("运算时间"+str(time04-time03))
'''

