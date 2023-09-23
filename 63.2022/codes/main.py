import numpy as np

def p_Y_given_XA(y):
    # Replace with the actual probability density function p(Y|X_A)
    # For example, if it's a Gaussian distribution with mean mu and std sigma:
    mu = 2
    sigma = 1
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((y - mu) / sigma)**2)

def p_Y_given_XB(y):
    # Replace with the actual probability density function p(Y|X_B)
    # For example, if it's a Gaussian distribution with mean mu and std sigma:
    mu = 5
    sigma = 1
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((y - mu) / sigma)**2)

def conditional_probability(Y, X):
    if X == 'A':
        p_Y_given_X = p_Y_given_XA
    elif X == 'B':
        p_Y_given_X = p_Y_given_XB
    else:
        raise ValueError("X must be 'A' or 'B'")
    
    return p_Y_given_X(Y)

# Example usage:
Y_value = 3  # Replace with the actual value of Y
X_value = 'A'  # Replace with the actual value of X (either 'A' or 'B')

result = conditional_probability(Y_value, X_value)
print(result)

