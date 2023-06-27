# factoriel de 3
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1
# 2! = 2 * 1
# 4! = 4 * 3!
# 3! = 3 * 2!
# conclusion : n! = n * (n-1)!

# factoriel (4) = 4 * factoriel (3)
#               = 4 * 3 * factoriel (2)
#               = 4 * 3 * 2 * factoriel (1)
#               = 4 * 3 * 2 * 1


def factoriel(n):
    if n >= 1:
        return n * factoriel(n-1)
    elif n == 0:
        return 1

print(factoriel(4))
