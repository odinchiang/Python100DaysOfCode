def add(*args):
    print(type(args))  # Tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 2, 5, 65))


def calculate(n, **kwargs):
    print(type(kwargs))  # dict
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]  # 若無此 key 值會報錯
        # self.model = kw["model"]
        self.make = kw.get("make")  # 若無此 key 值則回傳 None
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
