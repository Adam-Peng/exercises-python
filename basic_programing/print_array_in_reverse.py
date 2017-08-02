# Given the size and the elements of array A, print all the elements in reverse order.
#
# Input:
# First line of input contains, N - size of the array.
# Following N lines, each contains one integer, i{th} element of the array i.e. A[i].
#
# Output:
# Print all the elements of the array in reverse order, each element in a new line.

N = int(input())

Lst = [int(input()) for i in range(N)]
for i in reversed(range(N)):
    print(Lst[i])

