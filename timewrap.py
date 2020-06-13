import time


def call_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('此程序运行了%s' % (stop_time - start_time))
        return res

    return inner


@call_time
def func():
    time.sleep(2)


if __name__ == '__main__':
    func()
