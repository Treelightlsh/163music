def func(n):
    if n == 0:
        print('我的小鲤鱼', end='')
    else:
        print('抱着', end='')
        func(n-1)
        print('的我', end='')


func(5)
