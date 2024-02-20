from IntricateInteger import IntricateInteger


class IntricateIntegers:
    """
    Constructor method for a new IntricateIntegers object.
    n - the modulus of the IntricateIntegers
    alpha - the multiplier of the IntricateIntegers
    """
    def __init__(self, n, a):
        self.n = n
        self.a = a

    """
    Returns a string of the value of the IntricateIntegers object.
    """
    def __str__(self):
        return "< n = " + str(self.n) + " | alpha = " + str(self.alpha) + " >"

    """
    Returns the size of the Intricate Integer object.
    """
    def size(self):
        return self.n
