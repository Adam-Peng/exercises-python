# You have been given 3 integers - l, r and k.
# Find how many numbers between l and r (both inclusive) are divisible by k.
# You do not need to print these numbers, you just have to find their count.
# Constrainst:
# 1 <= l <= r <= 1000
# 1 <= k <= 1000
l, r, k = [int(i) for i in input().split(' ')]

print(len([x for x in range(l, r+1) if x % k == 0]))