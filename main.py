import sys

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
rows, cols = (10, 20) # sys.argv[3], sys.argv[4]
arr = [[0] * cols] * rows # empty = 0, occupied = 1
seatBuffer = 3

def assignSeats(R: int, C: int, seatBuffer: int, numCustomer: int, seatsLeft: int, nextAvailRow: int, nextAvailCol: int):
    # nextAvailCol = 0 to (C-1), nextAvailRow = 0 to (R-1)
    # return a tuple of -> (list, int, int, int)
    # 1. list of assigned seats (strings)
    # 2. the number of available seats
    # 3. the row/col of the next seat location.

    # check for insufficient seats
    if (seatsLeft < numCustomer):
        return ([], seatsLeft, nextAvailRow, nextAvailCol)

    # start assigning
    result = []
    for i in range(numCustomer):
        result.append((nextAvailRow, nextAvailCol))
        if (nextAvailCol + 1 < C):
            nextAvailCol += 1
        else:
            nextAvailRow += 1
            nextAvailCol = 0

    # add seatBuffer and fine the next avail seat
    if nextAvailCol + seatBuffer < C:
        # after inserting seatBuffer, if the next avail seat is still in the same row
        nextAvailCol += seatBuffer
        seatsLeft -= (numCustomer + seatBuffer)
    else:
        seatsLeft -= (numCustomer + C - nextAvailCol)
        nextAvailRow += 1
        nextAvailCol = 0

    return (result, seatsLeft, nextAvailRow, nextAvailCol) 



