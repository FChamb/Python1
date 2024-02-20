from IntricateInteger import IntricateInteger


class IntricateIntegers:
    """
    Constructor method for a new IntricateIntegers object.
    n - the modulus of the IntricateIntegers
    alpha - the multiplier of the IntricateIntegers
    """
    def __init__(self, n, alpha):
        self.n = n
        self.alpha = alpha

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


class IntricateIntegersIterator:
    """
    Constructor method for an Iterator IntricateIntegers object.
    intricate_integer - the type of IntricateIntegers object to iterate
    """
    def __init__(self, intricate_integer):
        self.intricate_integer = intricate_integer
        self.start = 0

    """
    Returns the Iterator object.
    """
    def __iter__(self):
        return self

    """
    Advances the Iterator to the next element in the list
    """
    def __next__(self):
        if self.start < self.intricate_integer.size():
            self.start += 1
            return IntricateInteger(self.start - 1, self.intricate_integer.n, self.intricate_integer.alpha)
        else:
            raise StopIteration
