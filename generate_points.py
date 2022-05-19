import random
import math

def generate_points(n):
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        
        if math.sqrt(x**2 + y**2) <= 1:
            count += 1
    return 4 * count / n

print(generate_points(1000000))