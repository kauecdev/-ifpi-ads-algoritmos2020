''' 3.2.1

def do_twice(f,s):
    f(s)
    f(s)

def print_cicero():
    print('cicero')

''' 
''' 3.2.2

def do_twice(f,s):
    f(s)
    f(s)

def print_cicero(dado):
    print(dado)

do_twice(print_cicero, 'kaue')

'''
''' 3.2.5

def do_twice(f,s):
    f(s)
    f(s)

def print_cicero(dado):
    print(dado)

def do_four(r,s):
    do_twice(r,s)
    do_twice(r,s)

do_four(print_cicero, 'kaue')