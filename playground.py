import time
import math
import random

arr = [
    233453534653464564, 65646565656565, 656565654654654,
    64564565464565463454, 645645645654656, 45645645645645645645,
    6456456456456456565, 645645645654654645645, 6546546456456,
    45645654645645, 645645656, 45645, 654645654645645
]

# Random constant to simulate variation
big_const = 324324235432643546897234968734

# START TIMER
timeFrame1 = time.perf_counter()

results = []

for i in range(500_000):
    for j in arr:
        # Multiply and simulate complex math
        net = (j * big_const) + (j // 9999991) - (j % 23423)

        # Add conditional branch
        if net % 2 == 0:
            net = net ^ 0b1010101010101010  # bitwise XOR
        else:
            net = net | 0b1100110011001100  # bitwise OR

        # Use math operations
        log_val = math.log(j % 100000 + 1)  # avoid log(0)
        net += int(log_val * 1e6)

        # Random noise
        net += random.randint(1, 100)

        # Save (not print)
        results.append(net)

# END TIMER
timeFrame2 = time.perf_counter()

print(f"Time Taken: {timeFrame2 - timeFrame1:.2f} seconds")
