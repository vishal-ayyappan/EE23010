import numpy as np

# Define the probability mass function
def pmf(x, k):
    if x in [1, 2, 3, 4]:
        return k * (x + 1)
    elif x in [5, 6, 7]:
        return 2 * k * x
    else:
        return 0

# Define the range of possible values for X
x_values = np.arange(1, 8)

# Define the equations for E(X) and Var(X)
def expected_value(k):
    return sum(x * pmf(x, k) for x in x_values)

def variance(k):
    return sum((x - expected_value(k))**2 * pmf(x, k) for x in x_values)

# (i) Solve for k
def calculate_k():
    for k_candidate in np.linspace(0.001, 10, 10000):  # Try different values of k
        eq = sum(pmf(x, k_candidate) for x in x_values) - 1
        if abs(eq) < 0.0001:  # Check if the equation is close to zero
            return k_candidate

# Perform 10,000 simulations
num_simulations = 10000
results = []

for _ in range(num_simulations):
    k = calculate_k()
    expected_x = expected_value(k)
    std_dev_x = np.sqrt(variance(k))
    results.append((k, expected_x, std_dev_x))

# Calculate averages
avg_k = np.mean([result[0] for result in results])
avg_expected_x = np.mean([result[1] for result in results])
avg_std_dev_x = np.mean([result[2] for result in results])

# Print the results
print(f"Avg. Value of k: {avg_k}")
print(f"Avg. E(X): {avg_expected_x}")
print(f"Avg. Standard Deviation of X: {avg_std_dev_x}")

