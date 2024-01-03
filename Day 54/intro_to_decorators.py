import time


def decorator_func(func):
    def wrapper_func():
        time.sleep(2)
        func()

    return wrapper_func


@decorator_func
def say_hello():
    print("Hello")


def say_hi():
    print("Hi")


def say_hola():
    print("Hola")


say_hello()
