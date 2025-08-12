import gc


a = 1
b = 2
c = 3

data_list = list()
data_dict = dict()
data_tuple = tuple()


class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

MyClass(value='in memory')


def add(x, y):
    print(locals())
    return x + y

gc.enable()  # Enable garbage collection

#print(gc.get_objects())
#print(gc.get_stats())


while True:
    try:
        suplier = input("Simple REPL: ")
        print(eval(suplier, globals(), locals()))
    except:
        print("An error occurred. Please try again.")

#print(eval("a + b + c + d", {"f": 5}, {"a": 2, "b": 4, "c": 6, "d": 2}))  # Should print 57
#expr, globals, locals = "a + b + c + d", {"d": 45}, {"a": 2, "b": 4, "c": 6}