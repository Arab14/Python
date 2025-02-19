def gcd(a, m):
    if a == 0:
        return m, 0, 1
    ans, x1, y1 = gcd(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return ans, x, y

def congruence(a, b, m):
    ans, x, _ = gcd(a, m)
    if b % ans != 0:
        print("No solution")
        return None
    a, b, m = a // ans, b // ans, m // ans
    x = (x * b) % m
    return x

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the constant b: "))
m = int(input("Enter the modulo m: "))
sol = congruence(a, b, m)
if sol is not None:
    print(f"The solution to {a}x ≡ {b} (mod {m}) is: {sol}")