n = int(input("n: "))
for i in range(n):
    spaces = abs(n//2 - i)
    stars = n - 2*spaces
    print(" " * spaces + "*" * stars)
