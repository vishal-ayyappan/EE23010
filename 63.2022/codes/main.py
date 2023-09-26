import scipy.integrate as spi
import numpy as np

# Define the conditional probability density functions
def fY_given_xA(y):
    return np.exp(-(y+1))

def fY_given_xB(y):
    return np.exp(y-1) * (1 - (y < -1))

# Define the intervals for integration
interval_xA = (0, 1)
interval_xB = (-1, 0)

# Integrate the conditional probability density functions
PexA, _ = spi.quad(fY_given_xA, *interval_xA)
PexB, _ = spi.quad(fY_given_xB, *interval_xB)

# Calculate the total probability of error
Pe = PexA*0.5 + PexB*0.5

print(f"The probability of error (Pe) is: {Pe}")

