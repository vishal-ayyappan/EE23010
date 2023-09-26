import numpy as np

def generate_Y(num_samples):
    u = np.random.rand(num_samples)  # Generate random samples from U(0, 1)

    # Generate Y for xA
    y_xA = -1 - np.log(1 - u)

    # Generate Y for xB
    y_xB = 1 + np.log(u)

    # Choose between y_xA and y_xB based on the transmitted symbol
    transmitted_symbols = np.random.choice([-1, 1], size=num_samples, p=[0.5, 0.5])
    y = np.where(transmitted_symbols == -1, y_xA, y_xB)

    return y

# Example: Generate 10 samples of Y
num_samples = 1
Y_samples = generate_Y(num_samples)
print(Y_samples)

