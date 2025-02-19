def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = [0 for _ in range(n)]
    
    for k in range(max_iterations):
        x_new = x.copy()
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        
        x = x_new
    
    raise Exception("Gauss-Seidel method did not converge")

A = [
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3]
]
b = [4, 7, 3]

solution = gauss_seidel(A, b)
print("Solution:", solution)