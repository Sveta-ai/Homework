number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

for el in number:
    # print(el)
    is_prostoe = True
    for i in range(2, el):
        if el % i == 0:
            is_prostoe = False
            break
    if is_prostoe:
        primes.append(el)
        # print('Простое')
    else:
        # print('Нет')
        not_primes.append(el)
print(primes)
print(not_primes)
