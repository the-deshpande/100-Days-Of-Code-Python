def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def calculate(**kwargs):
    for key, items in kwargs.items():
        print(key, items)


print(add(1, 2))
print(calculate(a=10, b=12, c=8))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


car = Car(make=10)
print(car.make, car.model)
