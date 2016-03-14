globals()["z"] = 7  # == 7 = 7



def f(n):
    print(locals())
    if n == 0:
        return 1
    x = n
    t = f(n - 1)
    return x * t


print(f(5))


def f():
    p = 7
    print(p)


def h():
    p = 2

    def f():
        print(p)

    f()


h()


def izmeri(n):
    poskusov = 0

    def indeks(s, x):
        from random import randint
        nonlocal poskusov
        while True:
            poskusov += 1
            i = randint(0, len(s) - 1)
            if s[i] == x:
                return i

    for i in range(100):
        indeks(list(range(n)), 0)
    return poskusov / 100


print(izmeri(500))
