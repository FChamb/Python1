import math


class IntricateInteger:

    def __init__(self, obj, n, alpha):
        if obj < 0:
            raise Exception("Value must be positive!")
        if n < 0:
            raise Exception("Invalid value for: n. Must be positive!")
        allowed = [i for i in range(n - 1)]
        if alpha not in allowed:
            raise Exception("Invalid value for: alpha!")
        if obj not in allowed:
            self.object = obj % n
        else:
            self.object = obj
        self.n = n
        self.alpha = alpha

    # overwrite "print"
    def __str__(self):
        return "<" + str(self.object) + " mod " + str(self.n) + " | " + str(self.alpha) + " >"

    # define "*"
    def __mul__(self, other):
        if self.n == other.n and self.alpha == other.alpha:
            return IntricateInteger((self.object
                                     + other.object
                                     + self.alpha * math.lcm(self.object, other.object))
                                    % self.n, self.n, self.alpha)
        else:
            raise Exception("Incompatible intricate integers!")


x = IntricateInteger(3, 7, 2)
print(x)
y = IntricateInteger(5, 7, 2)
print(y)
print(x * x)
print(x * y)
