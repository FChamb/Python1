import math
import itertools

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
Helper function for get_power_combinations.
Takes a list of sublists and multiplies every
element, adding results to a set which eventually 
contains the span of the original generators.
combs - the list of sublists of combinations
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
"""
def multiply_sublists(combs, n, alpha):
    print("Running multiply_sublists")
    span_list = []
    for sublist in combs:
        if len(sublist) == 1:
            ele = IntricateInteger(sublist[0], n, alpha)
            span_list.append(ele.object)
            span_list.append((ele*ele).object)
        else:
            product = IntricateInteger(0, n, alpha)
            for i in sublist:
                ele = IntricateInteger(i, n, alpha)
                product = product*ele
            print("Product: ", product.object)
            span_list.append(product.object)
    return set(span_list)


"""
Method to return a nicer looking version of a set of
IntricateIntegers, showing only their object values.
set1 - the set of IntricateIntegers to be manipulated
"""
def get_set_vals(set1):
    list1 = list(set1)
    if isinstance(list1[0], int):
        return set1
    set1_vals = {i.object for i in set1}
    return set(set1_vals) #iterate through all and if not int, get .object
    

"""
Helper method for get_power_combinations,
returns true if two sets of IntricateIntegers are
equal by comparing the object attributes of each
element.
set1, set2 - the sets to be compared
"""
def are_sets_equal(set1, set2):
    print("Running are sets equal")
    set1_vals = {i for i in get_set_vals(set1)}
    set2_vals = {i for i in get_set_vals(set2)}
    print(set1_vals == set2_vals)
    return set1_vals == set2_vals


"""
Returns the span of a given set of IntricateIntegers,
for a given (n, alpha) by recursively finding all 
combinations of set elements and their products.
Stops when no new products have been found in
a pass.
n - the modules of the IntricateInteger
alpha - the multiplier of the IntricateInteger
int_set - the set of generators (and eventually products)
to be combined
"""
def get_power_combinations(int_set, n, alpha):
    val_set = get_set_vals(int_set)
    print("running!")
    combs = [] #list of possible product 'factors'
    print(len(int_set), "\n")
    for i in range (1, len(val_set) + 1):
        print("In loop")
        #get all combinations of a certain length
        combs.extend(itertools.combinations(val_set, i))
        print(len(combs))
    print("Escaped the loop")
    neat_set = multiply_sublists(combs, n, alpha)
    print("Int set: ", get_set_vals(int_set))
    print("Neat set: ", get_set_vals(neat_set))
    if are_sets_equal(val_set, neat_set):
        #no new products added, return set
        return neat_set
    else:
        return get_power_combinations(neat_set, n, alpha)

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
        self.memo = {} #implementing memoisation for efficiency purposes

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
            if (self.object, other.object) in self.memo: #check if result is memoized
                return self.memo[(self.object, other.object)]
    
            result = IntricateInteger((self.object 
                                        + other.object
                                        + self.alpha * math.lcm(self.object, other.object))
                                        % self.n, self.n, self.alpha) #calculate intricate multiplication
            self.memo[(self.object, other.object)] = result #memoize result
            return result 
        else:
            raise Exception("Incompatible intricate integers!")

    def mul2(self, other): #compare timing improvement with memoisation
        if self.n == other.n and self.alpha == other.alpha:
            result = IntricateInteger((self.object
                                        + other.object
                                        + self.alpha * math.lcm(self.object, other.object))
                                        % self.n, self.n, self.alpha) #calculate intricate multiplication
            return result 
        else:
            raise Exception("Incompatible intricate integers!")

#test stuff to be removed!!!
x = IntricateInteger(1, 20, 5)
y = IntricateInteger(2, 20, 5)
z = IntricateInteger(3, 20, 5)
test_set = {x, y, z}
print(get_power_combinations(test_set, 20, 5))
