def prime(num):
    for i in range(1, num+1):
        is_prime = True
        if i == 1:
            continue
        for j in range(2, i+1):
            if i % j == 0 and j != i:
                is_prime = False
                break
        if is_prime:
            print(i, end=' ')

number = int(input('Enter an integer: '))
prime(number)

# Given 100
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
