# You have been given an array A of size N consisting of positive integers.
# You need to find and print the product of all the number in this array 10^9 + 7
n = int(input(""))
value = 1
list1 = list(map(int,input().split()))
for i in range(n):
    value = (value * list1[i]) % (1000000007)

print(value)
