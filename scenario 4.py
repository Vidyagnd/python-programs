import numpy as np
import time

# Generate 1,000,000 inputs
inputs = np.arange(1000000)

# Create weights (simulate single neuron)
weights = np.arange(1000000)

# -------- NumPy Version --------
start = time.time()

output = inputs @ weights

end = time.time()

print("NumPy Time:", end - start)


# -------- Python List Version --------
inputs_list = list(range(1000000))
weights_list = list(range(1000000))

start = time.time()

result = 0
for i in range(1000000):
    result += inputs_list[i] * weights_list[i]

end = time.time()

print("Python Loop Time:", end - start)