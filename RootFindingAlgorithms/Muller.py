def muller_method(func, x0, x1, x2, tolerance=1e-6, max_iterations=100):
    iteration = 0
    while iteration < max_iterations:
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (func(x1) - func(x0)) / h1
        delta2 = (func(x2) - func(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        b = delta2 + h2 * d
        D = (b**2 - 4 * func(x2) * d)**0.5
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2 * func(x2) / E
        p = x2 + h
        if abs(h) < tolerance:
            return p
        x0, x1, x2 = x1, x2, p
        iteration += 1
    return None
