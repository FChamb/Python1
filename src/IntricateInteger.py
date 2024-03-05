import math

"""
Returns a boolean indicating whether (x * x) = x
for a given (n, alpha). If so the Intricate Peculiar
Property holds true for all x in Zn.
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
"""
def has_intricate_peculiar_property(n, alpha):
    for x in range(0, n):
        a = IntricateInteger(x, n, alpha)
        if (a * a).object != a.object:
            return False
    return True


"""
Returns a boolean indicating whether (x * y) = (y * x)
for a given (n, alpha). If so the Commutative Intricate
Multiplication holds true for all x in Zn.
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
"""
def has_commutative_intricate_multiplication(n, alpha):
    found = {}
    for x in range(0, n):
        for y in range(0, n):
            x = 0
            y = 0
            a = IntricateInteger(x, n, alpha)
            b = IntricateInteger(y, n, alpha)
            key = (a.object, b.object)
            key2 = (b.object, a.object)
            if key in found:
                x = found.get(key)
            if key2 in found:
                y = found.get(key2)
            if x == 0 or y == 0:
                x = (a * b).object
                y = (b * a).object
                found[key] = x
                found[key2] = y
            if x != y:
                return False
    return True


"""
Returns a list of all x in Zn for which (x * y) * z = x * (y * z)
for a given (n, alpha).
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
"""
def has_associative_intricate_multiplication(n, alpha):
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                a = IntricateInteger(x, n, alpha)
                b = IntricateInteger(y, n, alpha)
                c = IntricateInteger(z, n, alpha)
                if ((a * b) * c).object != (a * (b * c)).object:
                    return False
    return True


"""
Returns a list of all x in Zn for which (x * x) = 1
for a given (n, alpha).
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
"""
def intricate_roots_of_one(n, alpha):
    valid = []
    for x in range(0, n):
        a = IntricateInteger(x, n, alpha)
        if (a * a).object == 1:
            valid.append(x)
    return valid


class IntricateInteger:
    """
    Constructor method for a new IntricateInteger object.
    Uses conditional statements to assure that the provided
    values are valid with the specification given
    constraints.
    obj - the object or value of the IntricateInteger
    n - the modulus of the IntricateInteger
    alpha - the multiplier of the IntricateInteger
    """
    def __init__(self, obj, n, alpha):
        if obj < 0:
            raise Exception("Value must be positive!")
        if n < 0:
            raise Exception("Invalid value for: n. Must be positive!")
        allowed = [i for i in range(n)]
        if alpha not in allowed:
            raise Exception("Invalid value for: alpha!")
        if obj not in allowed:
            self.object = obj % n
        else:
            self.object = obj
        self.n = n
        self.alpha = alpha

    """
    Returns a string value of the IntricateInteger object.
    """
    def __str__(self):
        return "<" + str(self.object) + " mod " + str(self.n) + " | " + str(self.alpha) + " >"

    """
    Multiplication method for the IntricateInteger object.
    Only returns a value if the n and alpha values of the
    two provided IntricateInteger objects are equal.
    other - the other IntricateInteger object to be multiplied
    """
    def __mul__(self, other):
        if self.n == other.n and self.alpha == other.alpha:
            return IntricateInteger((self.object
                                     + other.object
                                     + self.alpha * math.lcm(self.object, other.object))
                                    % self.n, self.n, self.alpha)
        else:
            raise Exception("Incompatible intricate integers!")
