# parameters
# *args
# default parameters
# **kwargs


def fun(name, *args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


fun('ajay', 1, 2, 3, a=1, b=2)
