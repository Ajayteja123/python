**kwargs(keyword argurments)


def fun(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


d = {'name': 'ajay', 'last_name': 'teja'}
fun(**d)
