class IntricateInteger:

    def __init__(self, obj):
        self.object = obj

    def __init__(self, obj, z, a):
        self.object = obj
        self.zrange = z
        self.alpha = a

    # overwrite "print"
    def __str__(self):
        return "<" + str(self.object) + ">"

    # define "*"
    def __mul__(self, other):
        return IntricateInteger(self.object
                                + other.object
                                + self.object * other.object)




a = IntricateInteger(3)
print(a)
b = IntricateInteger(5)
print(b)
print(a*b)