def myfnc( a, *args):
    print(a)
    print(type(args))

    for a in args:
        print(a)

def greet(number, **kwargs):
    print(type(kwargs))
    print(number)


myfnc('Hello')
greet(name='sparsh', 4)