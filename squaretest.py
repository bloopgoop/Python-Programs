n = 31
is_prime =  True
m = 2

while is_prime and n > m:
    if n % m == 0:
        is_prime = False
        print(n, m)
    m += 1

print(is_prime)
