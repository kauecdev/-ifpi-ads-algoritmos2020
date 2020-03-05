import turtle

def main():
    bob = turtle.Turtle()
    print(bob)
    circle(bob,2)

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


def circle(t,r):
    polygon(t,10,100)
    
main()

turtle.mainloop()