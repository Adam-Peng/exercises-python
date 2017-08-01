# Akash and Vishal are quite fond of travelling.
# They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment.
# The compartment looked something like
# Window Seat : WS
# Middle Seat : MS
# Aisle Seat : AS
# You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.
# INPUT
# First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.
#
# OUTPUT
# For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.
#

N = int(input())
L = []

for i in range(N):
    L.append(int(input()))

for j in L:
    multiple = int(j / 12)
    remainder = j % 12
    if remainder == 0:
        seat = 12 * (multiple - 1) + (13 - 12)
    else:
        seat = 12 * multiple + (13 - remainder)

    seat_type = ''
    if remainder in [2, 5, 8, 11]:
        seat_type = 'MS'
    elif remainder in [3, 4, 9, 10]:
        seat_type = 'AS'
    else:
        seat_type = 'WS'
    print('{0} {1}'.format(seat, seat_type))
