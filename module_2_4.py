numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
numbers.remove(1)
length = (len(numbers))
for i in range(length):
    for j in range(length):
        num = (numbers[i] / numbers[j])
        if num == 2 or num == 3 or num == 5:
            not_primes.append(numbers[i])
            break
        elif num == is_prime:
            primes.append(numbers[i])
            break
print('Точные: ', primes)
print('Не точные: ', not_primes)






