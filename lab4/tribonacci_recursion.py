def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return (n - 3) + (n - 2) + (n - 1)


print(tribonacci(35))
