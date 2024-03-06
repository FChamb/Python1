from IntricateInteger import IntricateInteger
import timeit
import random
import csv

def timer():
    functionName = [IntricateInteger.__mul__, IntricateInteger.mul2] #use method references
    repetitions = 100000 #100,000 repetitions of the code snippet - more accurate average speed
    with open('Performance_Testing/test.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['MultType', 'n', 'alpha', 'TotalTime', 'AvgTime'])
        for i in range(2):
            for j in range(250): #250 different combinations of x, y, n and alpha
                n = random.randint(2, 20)
                n1 = random.randint(1, n-1)
                n2 = random.randint(1, n-1)
                alpha = random.randint(1, n-1)  
                x = IntricateInteger(n1, n, alpha)
                y = IntricateInteger(n2, n, alpha)
                t = timeit.Timer(lambda: functionName[i](x, y))
                result = t.timeit(number=repetitions)
                totalTime = result * 1000000000  #convert seconds to nanoseconds
                avgTime = result * 10000  #convert seconds to nanoseconds
                writer.writerow([i+1, n, alpha, totalTime, avgTime])

timer()
