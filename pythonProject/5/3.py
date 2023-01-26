def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Syötä kokonaisluku: "))
if is_prime(num):
    print(num, "on alkuluku.")
else:
    print(num, "ei ole alkuluku.")