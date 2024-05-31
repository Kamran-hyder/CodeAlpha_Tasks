def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

# Example usage:
n_terms = 10
print(f"Fibonacci series with {n_terms} elements:", fibonacci(n_terms))
