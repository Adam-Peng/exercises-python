# Dhananjay has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values and character he has developed a special word and named it Dhananjay's Magical word.
#
# A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is Dhananjay's Magical alphabet if its ASCII value is prime.
#
# Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives few string to his friends and ask them to convert it to Dhananjay's Magical word. None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.
#
# Rules for converting:
#
# 1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
#
# 2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.
#
# Input format:
#
# First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.
#
# Output Format:
#
# For each test case, print Dhananjay's Magical Word in a new line.
#
# Constraints:
#
# 1 <= T <= 100
#
# 1 <= |S| <= 500

#  a - z => 65 - 90 , A - Z => 97 - 122

T = int(input())
cases = []
for i in range(T):
    N = input()
    S = input()
    cases.append(S)


def list_primes(start, end):
    '''
    Return a list of primes in a range
    :param start: int
    :param end: int
    :return: list
    '''
    prime_list = []
    for i in range(start, end + 1):
        is_prime = True
        for j in range(1, i + 1):
            if i % j == 0 and i != j and j != 1:
                is_prime = False
        if is_prime:
            prime_list.append(i)
    return prime_list


def list_alphabet_primes():
    '''
    Return all magical alphabets in a list
    :return:
    '''
    primes = []
    ranges = [(65, 90), (97, 122)]
    for i in ranges:
        start, end = i
        primes += list_primes(start, end)
    return primes

target_primes = list_alphabet_primes()

def get_magical_alphabet(letter):
    '''
    Return the magical alphabet given a letter
    :param letter: target
    :return: the magical alphabet
    '''
    primes = target_primes[:]
    position = ord(letter)
    if position in primes:
        return chr(position)
    else:
        primes.append(position)
    new_array = sorted(primes)

    index = new_array.index(position)
    if index == 0:
        return chr(new_array[1])
    elif index == len(new_array) - 1:
        return chr(new_array[len(new_array) - 2])
    else:
        average = (new_array[index - 1] + new_array[index + 1]) / 2
    magical_letter_position = new_array[index - 1] if average >= position else new_array[index + 1]
    return chr(magical_letter_position)

for case in cases:
    p = ''.join([get_magical_alphabet(i) for i in case])
    print(p)
