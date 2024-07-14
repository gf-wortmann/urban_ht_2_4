# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(the_list)):
    is_prime = True
    for j in range(1, i):
        print('current i= ', i, ' current [i] = ', the_list[i], 'current j= ', j, ' current [j] = ', the_list[j])
        if the_list[i] % the_list[j] == 0:
            not_primes.append(the_list[i])
            is_prime = False
            print('is_prime is: ', is_prime)
            break
    if is_prime:
        primes.append(the_list[i])
        print('is_prime is: ', is_prime)

print('not primes: ', not_primes)
print('primes: ', primes)

