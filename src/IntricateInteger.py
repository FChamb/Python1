import math


class IntricateInteger:

    def __init__(self, obj, n, alpha):
        self.object = obj
        self.n = n
        self.alpha = alpha

    # overwrite "print"
    def __str__(self):
        return "<" + str(self.object) + " mod " + str(self.n) + " | " + str(self.alpha) + " >"

    # define "*"
    def __mul__(self, other):
        return IntricateInteger(self.object
                                + other.object
                                + self.object * other.object)


x = IntricateInteger(3, 7, 2)
print(x)
y = IntricateInteger(5, 7, 2)
print(y)
print(x * x)
print(x * y)
