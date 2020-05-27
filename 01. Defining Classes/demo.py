x = 5

def f():
    x = 6
    def f1():
        nonlocal x
        x = 7
    print(x)
    f1()
    print(x)


f()

