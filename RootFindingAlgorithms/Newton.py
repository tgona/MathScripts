def newton_method(func, func_derivative, initial_guess, tolerance=1e-6, max_iterations=100):
    #default iterations is 100, with tolerance of 0.000001
    x = initial_guess
    iteration = 0

    while abs(func(x)) > tolerance and iteration < max_iterations:
        x = x - func(x) / func_derivative(x)
        iteration += 1

    if iteration == max_iterations:
        print("Newton-Raphson method did not converge within the maximum number of iterations.")
    else:
        print(f"Root found at x = {x} after {iteration} iterations.")
    
    return x

# Example usage:
if __name__ == "__main__":
    # Define the function and its derivative.
    def f(x):
        return x**3 - 2*x**2 + 4
    # Input derivative of f(x), import necessary libraries for expression
    def f_derivative(x):
        return 3*x**2 - 4*x
    initial_guess = 2.0
    root = newton_method(f, f_derivative, initial_guess)
