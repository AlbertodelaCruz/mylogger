from mylogger import mylogger


class Arithmetics():
    def __init__(self):
        pass

    @mylogger
    def sum(self, x, y):
        result = x+y.sum
        print("This is a sum function: {}".format(result))
        return result

class MyObject():
    def __init__(self, var1, var2):
        self._var1 = var1
        self._var2 = var2

    @property
    def sum(self):
        return self._var1+self._var2


if __name__ == '__main__':
    arithmetics = Arithmetics()
    my_object = MyObject(1, 2)
    arithmetics.sum(1, my_object)
