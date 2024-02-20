import math


def has_intricate_peculiar_property(n, alpha):
    for x in range(0, n):
        a = IntricateInteger(x, n, alpha)
        if (a * a).object != a.object:
            return False
    return True


def peculiar_test():
    valid = []
    for n in range(1, 51):
        for a in range(0, n):
            if has_intricate_peculiar_property(n, a):
                sublist = [n, a]
                valid.append(sublist)
    for sublist in valid:
        if sublist[1] != (sublist[0] - 1):
            return False
    return True


def has_commutative_intricate_multiplication(n, alpha):
    for x in range(0, n):
        for y in range(0, n):
            a = IntricateInteger(x, n, alpha)
            b = IntricateInteger(y, n, alpha)
            if (a * b).object != (b * a).object:
                return False
    return True


def commutative_test():
    nonvalid = []
    result = True
    for n in range(1, 51):
        for a in range(0, n):
            if not has_commutative_intricate_multiplication(n, a):
                result = False
                sublist = [n, a]
                nonvalid.append(sublist)
    for sublist in nonvalid:
        print(sublist[0], sublist[1])
    return result


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


def associative_test():
    valid = []
    result = True
    for n in range(1, 21):
        for a in range(0, n):
            if has_associative_intricate_multiplication(n, a):
                sublist = [n, a]
                valid.append(sublist)
            else:
                result = False
    for sublist in valid:
        print(sublist[0], sublist[1])
    return result


def intricate_roots_of_one(n, alpha):
    valid = []
    for x in range(0, n):
        a = IntricateInteger(x, n, alpha)
        if (a * a).object == 1:
            valid.append(x)
    return valid


def roots_test():
    valid = []
    for n in range(1, 26):
        for a in range(0, n):
            valid.append(len(intricate_roots_of_one(n, a)))
    maximum = max(valid)
    finallist = []
    for i in range(maximum + 1):
        sublist = [i, valid.count(i)]
        finallist.append(sublist)
    return finallist


class IntricateInteger:

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
print("Has peculiar 1: ", has_intricate_peculiar_property(10, 3))
print("Has peculiar all: ", peculiar_test())
print("Has commutative 1: ", has_commutative_intricate_multiplication(20, 10))
print("Has commutative all: ", commutative_test())
print("Has associative 1: ", has_intricate_peculiar_property(10, 3))
print("Has associative all: ", associative_test())
print("Has roots 1: ")
print(roots_test())
