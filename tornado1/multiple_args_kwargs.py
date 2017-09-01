def foo(*args):
    print type(args)


def foo2(**kwargs):
    print type(kwargs)


foo()
foo2()
