from IntricateInteger import *
from IntricateIntegers import *
import unittest
from timeit import default_timer as timer


"""
Returns a boolean indicating whether has_intricate_peculiar_property
holds for all values of 1 <= n <= 50 and 0 <= a < n in a = n -1.
"""
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


"""
Returns a boolean indicating whether has_intricate_peculiar_property
holds for all values of 1 <= n <= 50 and 0 <= a < n in a = n -1. This
is for iterative.
"""
def peculiar_iterative_test():
    valid = []
    for n in range(1, 51):
        for a in range(0, n):
            if has_intricate_peculiar_property_iterative(n, a):
                sublist = [n, a]
                valid.append(sublist)
    for sublist in valid:
        if sublist[1] != (sublist[0] - 1):
            return False
    return True


"""
Returns a boolean indicating whether has_commutative_intricate_multiplication
holds for all values of 1 <= n <= 50 and 0 <= a < n. Prints any values where
the commutative intricate multiplication does not hold.
"""
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


"""
Returns a boolean indicating whether has_commutative_intricate_multiplication
holds for all values of 1 <= n <= 50 and 0 <= a < n. Prints any values where
the commutative intricate multiplication does not hold. This is for iterative.
"""
def commutative_iterative_test():
    nonvalid = []
    result = True
    for n in range(1, 51):
        for a in range(0, n):
            if not has_commutative_intricate_multiplication_iterative(n, a):
                result = False
                sublist = [n, a]
                nonvalid.append(sublist)
    for sublist in nonvalid:
        print(sublist[0], sublist[1])
    return result


"""
Returns a boolean indicating whether has_associative_intricate_multiplication
holds for all values of 1 <= n <= 20 and 0 <= a < n. Prints any values where
the associative intricate multiplication does hold.
"""
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


"""
Returns a boolean indicating whether has_associative_intricate_multiplication
holds for all values of 1 <= n <= 20 and 0 <= a < n. Prints any values where
the associative intricate multiplication does hold. This is for iterative
"""
def associative_iterative_test():
    valid = []
    result = True
    for n in range(1, 21):
        for a in range(0, n):
            if has_associative_intricate_multiplication_iterative(n, a):
                sublist = [n, a]
                valid.append(sublist)
            else:
                result = False
    for sublist in valid:
        print(sublist[0], sublist[1])
    return result


"""
Returns a list indicating which values of intricate_roots_of_one
return different values for n and alpha in 1 <= n <= 25 and 
0 <= a < n.
"""
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


"""
Returns a list indicating the minimum values of n and alpha
as a counter example for the conjecture { a is odd, gcd(n,a) != 1
of 1 <= n <= 25 and 0 <= a < n.
"""
def minimum_roots_test():
    for n in range(1, 26):
        for a in range(1, n, 2):
            if math.gcd(n, a) != 1 and intricate_roots_of_one(n, a) != 1:
                items = [n, a]
                return items


class Testing(unittest.TestCase):
    """
    Intricate Integer Creation
    """
    # Testing Intricate Integer Non-null
    def test_NonNullIntricateInteger(self):
        print("\033[1mTesting Intricate Integer Creation: \033[0m")
        x = IntricateInteger(1, 2, 1)
        self.assertIsInstance(x, IntricateInteger)

    # Testing Intricate Integer Contains Values
    def test_CorrectValueStored(self):
        print("\033[1mTesting Intricate Integer Values: \033[0m")
        x = IntricateInteger(1, 2, 1)
        self.assertTrue(x.object == 1 and x.n == 2 and x.alpha == 1)

    # Testing Edge Case: n = 1, alpha = 0
    def test_ValidAlpha(self):
        print("\033[1mTesting Edge Case of Valid Alpha: \033[0m")
        x = IntricateInteger(0, 1, 0)
        self.assertIsInstance(x, IntricateInteger)

    # Testing Edge Case: n = 1, alpha = 1
    def test_InvalidAlpha(self):
        print("\033[1mTesting Edge Case of Invalid Alpha: \033[0m")
        self.assertRaises(Exception, IntricateInteger, 0, 1, 1)

    # Testing With Negative Numbers
    def test_NegativeNums(self):
        print("\033[1mTesting Creating Intricate Integer with Negative Numbers: \033[0m")
        self.assertRaises(Exception, IntricateInteger, -1, -2, -1)

    # Testing With String Values
    def test_StringValues(self):
        print("\033[1mTesting Creating Intricate Integer with String Values: \033[0m")
        self.assertRaises(Exception, IntricateInteger, '0', 'Test', '0')

    """
    Intricate Integer Multiplication
    """
    # Testing Multiplication Using Specification Example
    def test_MultiplicationExample(self):
        print("\033[1mTesting Multiplication Example from Specification: \033[0m")
        x = IntricateInteger(3, 7, 2)
        y = IntricateInteger(5, 7, 2)
        z = (x * y)
        self.assertTrue(z.object == 3 and z.n == 7 and z.alpha == 2)

    # Testing Multiplication Using Other Values
    def test_MultiplicationExample2(self):
        print("\033[1mTesting Multiplication Using Other Values: \033[0m")
        x = IntricateInteger(5, 10, 6)
        y = IntricateInteger(2, 10, 6)
        z = (x * y)
        self.assertTrue(z.object == 7 and z.n == 10 and z.alpha == 6)

    # Testing Multiplication Using Different N and Alpha
    def test_MultiplicationError(self):
        print("\033[1mTesting Multiplication Using Different Values of N and Alpha: \033[0m")
        x = IntricateInteger(3, 7, 2)
        y = IntricateInteger(5, 8, 3)
        # self.assertRaises(Exception, IntricateInteger, x, y)
        with self.assertRaises(Exception) as context:
            x * y
            self.assertTrue("Incompatible intricate integers!" in context.exception)

    """
    Easy Additional Requirements
    """
    # Testing Peculiar Property for Specification Values
    def test_hasIntricatePeculiarProperty(self):
        print("\033[1mTesting Peculiar Property: \033[0m")
        self.assertTrue(peculiar_test())

    # Testing Commutative Property for Specification Values
    def test_hasCommutativeIntricateMultiplication(self):
        print("\033[1mTesting Commutative Multiplication: \033[0m")
        self.assertTrue(commutative_test())

    """
    Medium Additional Requirements
    """
    # Testing Associative Property for Specification Values
    def test_hasAssociativeIntricateMultiplication(self):
        print("\033[1mTesting Associative Multiplication: \033[0m")
        self.assertFalse(associative_test())

    # Testing IntricateIntegersIterator
    def test_IntricateIntegers(self):
        print("\033[1mTesting Intricate Integers Iterator: \033[0m")
        out = []
        for x in IntricateIntegersIterator(IntricateIntegers(3, 2)):
            out.append(str(x))
        print(str(out))
        valid = ["<0 mod 3 | 2 >", "<1 mod 3 | 2 >", "<2 mod 3 | 2 >"]
        self.assertTrue(out, valid)

    # Testing Peculiar Property for IntricateIntegersIterator
    def test_IntricateIntegersIteratorPeculiar(self):
        print("\033[1mTesting Peculiar Iterator: \033[0m")
        self.assertTrue(peculiar_iterative_test())

    # Testing Difference in time Between Peculiar Regular and Iterative
    def test_differencePeculiar(self):
        print("\033[1mTesting Peculiar Regular vs Iterative: \033[0m")
        start = timer()
        peculiar_test()
        end = timer()
        print("Regular Tests Completed in", end - start)
        start1 = timer()
        peculiar_iterative_test()
        end1 = timer()
        print("Iterative Tests Completed in", end1 - start1)
        print("Difference in tests", (end1 - start1) - (end - start))

    # Testing Commutative Property for IntricateIntegersIterator
    def test_IntricateIntegersIteratorCommutative(self):
        print("\033[1mTesting Commutative Iterator: \033[0m")
        self.assertTrue(commutative_iterative_test())

    # Testing Difference in time Between Commutative Regular and Iterative
    def test_differenceCommutative(self):
        print("\033[1mTesting Commutative Regular vs Iterative: \033[0m")
        start = timer()
        commutative_test()
        end = timer()
        print("Regular Tests Completed in", end - start)
        start1 = timer()
        commutative_iterative_test()
        end1 = timer()
        print("Iterative Tests Completed in", end1 - start1)
        print("Difference in tests", (end - start) - (end1 - start1))

    # Testing Difference in time Between Associative Regular and Iterative
    def test_differenceAssociative(self):
        print("\033[1mTesting Associative Regular vs Iterative: \033[0m")
        start = timer()
        associative_test()
        end = timer()
        print("Regular Tests Completed in", end - start)
        start1 = timer()
        associative_iterative_test()
        end1 = timer()
        print("Iterative Tests Completed in", end1 - start1)
        print("Difference in tests", (end - start) - (end1 - start1))

    # Testing Associative Property for IntricateIntegersIterator
    def test_IntricateIntegersIteratorAssociative(self):
        print("\033[1mTesting Associative Iterator: \033[0m")
        self.assertFalse(associative_iterative_test())

    """
    Hard Additional Requirements
    """
    # Testing Intricate Roots
    def test_intricateRoots(self):
        print("\033[1mTesting Intricate Roots: \033[0m")
        output = roots_test()
        print(output)
        self.assertTrue(output)

    # Testing Counter Example for gcd of roots
    def test_intricateRootsMinimum(self):
        print("\033[1mTesting Intricate Roots Minimum Value: \033[0m")
        output = minimum_roots_test()
        print(output)
        self.assertEqual(output, [6, 3])

    """
    Very Hard Additional Requirements
    """
    def test_generatorSpanAlgorithm(self):
            print("\033[1mTesting Generator Span Algorithm: \033[0m")
            x = IntricateInteger(1, 6, 5)
            y = IntricateInteger(2, 6, 5)
            z = IntricateInteger(3, 6, 5)
            test_set = {x, y, z}
            output = get_power_combinations(test_set, 6, 5)
            print(output)
            self.assertEqual(output, {1, 2, 3, 5})


"""
Enables UnitTesting to run when file is called.
"""
if __name__ == '__main__':
    unittest.main()
