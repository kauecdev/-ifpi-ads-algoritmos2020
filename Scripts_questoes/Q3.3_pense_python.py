def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def first_line():
    print('+ - - - -', end=' ')

def second_line():
    print('|        ', end=' ')

def print_first_line():
    do_twice(first_line)
    print('+')

def print_second_line():
    do_twice(second_line)
    print('|')

def print_1():
    print_first_line()
    do_four(print_second_line)

def print_2():
    do_twice(print_1)
    print_first_line()

print_2()

