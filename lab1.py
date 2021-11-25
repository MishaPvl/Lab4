from random import *
from math import ceil, sqrt


def modpow(base: int, exponent: int, mod: int):
    base %= mod
    if exponent == 0:
        pw = 1
    elif exponent % 2 == 0:
        pw = modpow(base * base, exponent // 2, mod) % mod
    else:
        pw = (base * modpow(base, exponent - 1, mod)) % mod
    return pw

def gcd(a, b):
    # if a < b:
    #     a, b = b, a
    U = [a, 1, 0]
    V = [b, 0, 1]
    while V[0] != 0:
        q = U[0] // V[0]
        T = [U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
        U = V
        V = T
    # print(f'x = {U[1]}, y = {U[2]}, gcd = {U[0]}, a = {a}, b = {b}')
    # print('a*x+b*y =', a * U[1] + b * U[2])
    return U


def dh_system(xa, xb, p, g):
    q = (p - 1)//2
    print(f'q = {q}')
    Xa, Xb = xa, xb
    if not(1 < g < p-1):
        p,g = g,p
    if modpow(g, q, p) != 1:
        Ya = modpow(g, Xa, p)
        Yb = modpow(g, Xb, p)
        Zab = modpow(Yb, Xa, p)
        Zba = modpow(Ya, Xb, p)
        return Ya, Yb, Zab, Zba
    else:
        print('Сгенерируйте новое число')

def shanks(y, a, p):
    if y >= p:
        y, p = p, y
    print(f'(y = {y}, a = {a}, mod = {p}')
    m = k = ceil(sqrt(p))    
    first_table = {(modpow(a, i, p)*y)%p: i for i in range(m+1)}
#   print(hashtable.keys())
#   print(hashtable.values())
    for j in range(1, k+1):
        k = modpow(a, j*m, p)
        if k in first_table:
            print(j*m-first_table[k])
            r = (j*m-first_table[k])
            print('Проверка через функцию modpow: ', modpow(a, r, p))
            return r
        
def get_coprime(num: int) -> int:
    res = rand_prime(1, 10**4)
    while gcd(num, res) != 1:
        res = rand_prime(1, 10**4)
    return res

def IsPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def rand_prime(a, b):
    p = randint(a, b)
    if IsPrime(p):
        return p
    else:
        return rand_prime(a, b)


def rand_int(x, y):
    p = randint(x, y)
    return p

def mutually_prime(a):
    while True:
        b = rand_int(2, a)
        if gcd(a, b)[0] == 1:
            return b
def gen_c_d(p):
    c = mutually_prime(p)
    gd = gcd(c, p)[0]
    d = gcd(c, p)[1]
    assert gd == 1
    while d < 0:
        d += p
    return c, d
def gen_g(mod: int) -> int:
    while True:
        g = rand_int(2, mod)
        if pow(g, (mod - 1) // 2, mod) != 1:
            return g
a = rand_int(0, 10**5)
b = rand_int(0, 10**5)
c = rand_int(0, 10**9)
xa = rand_prime(1, 10**9)
xb = rand_prime(1, 10**9)
p = rand_prime(1, 10**6)
g = rand_prime(1, 10**9)

# print('Быстрое возведение в степень по модулю')
# print(f'Первое число = {a}, Второе число = {b}, Третье число = {c}')
# print(modpow(a, b, c))
# print('*'*50)
# print('Обобщенный алгоритм Евклида')
# print(gcd(a, b))
# print('*'*50)
# print('Д-Х')
# print(f'Xa = {xa}, Xb = {xb}, p = {p}, g = {g}')
# print(dh_system(xa, xb, p, g))
# print('*'*50)
# print('Шаг младенца, шаг великана')
# print(shanks(a, b, p))
#print(shanks(84083, 95896, 582067))
#print(bsgs(5, 2, 23))
#print(extgcd(15, 4))
#print(gcd(15, 4))
#print(modpow(5, 5, 23))
#print(modpow(9, 21, 69))