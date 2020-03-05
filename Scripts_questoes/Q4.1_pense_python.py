import turtle
import math

def main():
    bob = turtle.Turtle()
    print(bob)
    arc(bob,120,180)

'''
def square(t,lenght):
    t.fd(lenght)
    t.lt(90)
    t.fd(lenght)
    t.lt(90)
    t.fd(lenght)
    t.lt(90)
    t.fd(lenght)
'''


def polygon(t,lenght,n):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)

'''
def circle(t,r):        
        c = ((2 * math.pi) * r) / 360
        polygon(t,c,100)
'''

def arc(t,r,angle):        
        c = ((2 * math.pi) * r) / 360
        polygon(t,c,100)
        360 - angle


main()

turtle.mainloop()