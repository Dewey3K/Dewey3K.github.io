def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n-1):
        if (n % i) == 0:
            return False
    return True

def primes(n):
    primes_list=[]
    for i in range(2, n):
        if is_prime(i) == True:
            primes_list.append(i)
    return primes_list

def prime_factorization(n):
    prime_factorizations = []
    x = 2
    while x*x <= n:
        while (n % x) == 0:
            prime_factorizations.append(x)
            n //= x
        x += 1
    if n > 1:
        prime_factorizations.append(n)
    return prime_factorizations

def my_sort(list): #insertion sort
    for i in range(1, len(list)):
        x = list[i]
        j = i-1
        while (j >= 0) and (x < list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = x

def unscramble(string):
    dictionary = open('wordlist.txt', 'r')
    lines = dictionary.readlines()
    string_sort = sorted(string)

    wordslist = []
    for line in lines:
        line_sort = sorted(line)
        line_sort.remove('\n')
        if string_sort == line_sort:
            wordslist.append(line.strip())
    return wordslist



primes = primes(10)
print(primes)
factorizations = prime_factorization(120)
print(factorizations)
list = [2,5,8,2,54,6,7,0]
my_sort(list)
print(list)
list2 = unscramble('islent')
print(list2)
