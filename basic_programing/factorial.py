# You have been given a positive integer N.
# You need to find and print the Factorial of this number.
# The Factorial of a positive integer N refers to the product of all number in the range from 1 to N.

def factorial(N):
    if N == 1:
        return 1
    return N * factorial(N - 1)

print(factorial(int(input())))
