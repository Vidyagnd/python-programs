import numpy as np
import time

# Object coordinates (2x2)
object_matrix = np.array([
    [1, 2],
    [3, 4]
])

# Rotation matrix (90° rotation)
rotation = np.array([
    [0, -1],
    [1,  0]
])

# -------- NumPy Version --------
start = time.time()

rotated = object_matrix @ rotation
scaled = rotated * 2   # Scale by factor 2

end = time.time()

print("NumPy Result:")
print(scaled)
print("NumPy Time:", end - start)


# -------- Python Loop Version --------
start = time.time()

rotated_loop = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            rotated_loop[i][j] += object_matrix[i][k] * rotation[k][j]

# Scale
for i in range(2):
    for j in range(2):
        rotated_loop[i][j] *= 2

end = time.time()

print("\nLoop Result:")
print(rotated_loop)
print("Loop Time:", end - start)