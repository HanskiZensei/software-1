import random


random_points = int(input("Enter how many random points to generate: "))

a_circle = 0
point_count = 0


while point_count < random_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        a_circle += 1

    point_count += 1

pi_approximation = 4 * a_circle / random_points
print(f"Approximation of pi: {pi_approximation}")
