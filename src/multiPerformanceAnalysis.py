from IntricateInteger import IntricateInteger
import timeit
import random

def timer():
    functionName = [IntricateInteger.__mul__, IntricateInteger.mul2] #use method references
    repetitions = 100000 #100,000 repetitions of the code snippet - more accurate average speed
    for i in range(2):
        for j in range(100): #100 different combinations of x, y, n and alpha
            n = random.randint(2, 20)
            n1 = random.randint(1, n-1)
            n2 = random.randint(1, n-1)
            alpha = random.randint(1, n-1)  
            x = IntricateInteger(n1, n, alpha)
            y = IntricateInteger(n2, n, alpha)
            t = timeit.Timer(lambda: functionName[i](x, y))
            result = t.timeit(number=repetitions)
            print(f"{functionName[i].__name__} ({n}, {n1}, {n2}, {alpha}): {result}")

timer()
