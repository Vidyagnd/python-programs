import numpy as np

# Original traffic matrix
T = np.array([[100, 40],
              [60, 80]])

# Signal optimization matrix
S = np.array([[0.9, 0.1],
              [0.2, 0.8]])

# Compute S squared (apply transformation twice)
S2 = np.linalg.matrix_power(S, 2)

# Final traffic after two optimizations
T_final = S2 @ T

print("Original Traffic Matrix:\n", T)
print("\nTransformation Matrix Squared (S^2):\n", S2)
print("\nTraffic After Two Optimizations:\n", T_final)