import sys

SEAT_BUFFER = 3
R, C = (10, 20)  # R = numRows = sys.argv[3], C = numCols = sys.argv[4]
ARR = [[0] * C] * R  # empty = 0, occupied = 1


def parseInput(filename: str) -> list:
    orders = []  # list of tuples (orders)
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            line = line.split()
            oneOrder = (line[0], int(line[1]))  # i.e. ("R001", 2)
            orders.append(oneOrder)
    return orders


def writeIntoOutputFile(filename: str, output: list):
    # @param output: list of str
    with open(filename, 'w') as file:
        for line in output:
            file.write("%s\n" % line)


def boundryCheck(nextAvailRow, nextAvailCol):
    if nextAvailRow >= R or nextAvailCol >= C:
        return False


def findNextAvailSeat(seatsLeft, nextAvailRow, nextAvailCol, numSeatRequested, forCustomerOrBuffer: bool):
    # 1. calc 1 nextAvailSeat
    if nextAvailCol + numSeatRequested < C:
        # after inserting the customer/buffer, if the next avail seat is still in the same row
        nextAvailCol += numSeatRequested
        seatsLeft -= numSeatRequested
    else:
        if (forCustomerOrBuffer == False):
            seatsLeft -= (C - nextAvailCol)
        else:
            seatsLeft -= numSeatRequested
        nextAvailRow += 1
        nextAvailCol = 0

    # 2. if the next avail seat should not be used due to customer safety
    print("nextAvailRow, nextAvailCol:\t", nextAvailRow, nextAvailCol)
    if boundryCheck(nextAvailRow, nextAvailCol) == True:
        if ARR[nextAvailRow - 1][nextAvailCol] == 1:
            seatsLeft, nextAvailRow, nextAvailCol = findNextAvailSeat(
                seatsLeft, nextAvailRow, nextAvailCol, 1, True)

    # 3. push seat to the next one if
    return seatsLeft, nextAvailRow, nextAvailCol


def assignSeats(numCustomer: int, seatsLeft: int, nextAvailRow: int, nextAvailCol: int):
    # nextAvailCol = 0 to (C-1), nextAvailRow = 0 to (R-1)
    # return a tuple of -> (list, int, int, int)
    # 1. list of assigned seats (strings)
    # 2. the number of available seats
    # 3. the row/col of the next seat location.

    # check for insufficient seats
    if (seatsLeft < numCustomer):
        return ([], seatsLeft, nextAvailRow, nextAvailCol)

    # start assigning
    assignment = []
    for i in range(numCustomer):
        # 1. assign 1 customer a seat, assuming the given nextAvailSeat is usable
        ARR[nextAvailRow][nextAvailCol] = 1  # occupied now
        assignment.append((nextAvailRow, nextAvailCol))

        # 2. find the 1 nextAvailSeat that is SAFE for customer
        seatsLeft, nextAvailRow, nextAvailCol = findNextAvailSeat(
            seatsLeft, nextAvailRow, nextAvailCol, 1, True)

    seatsLeft, nextAvailRow, nextAvailCol = findNextAvailSeat(
        seatsLeft, nextAvailRow, nextAvailCol, SEAT_BUFFER, False)
    return (seatsLeft, nextAvailRow, nextAvailCol, assignment)


def generateOutputLines(results: list) -> list:
    # results = list of tuples: (seatsLeft, nextAvailRow, nextAvailCol, Order#, assignmentResult)
    resultInLines = []
    for oneResult in (results):
        line = oneResult[3] + " "  # add "R001 "
        for i in oneResult[4]:  # add "I1,I2"
            # line += "\t" + str(i) + "="
            line += (chr(ord('J') - i[0]) + str(i[1] + 1) + ",")

        resultInLines.append(line)
        print(line)
    return resultInLines  # list of str (lines)


if __name__ == '__main__':
    # 1. check command line input
    if len(sys.argv) != 2:
        print("Invalid command line -- python3 main.py /path/to/inputfile")
        sys.exit()
    INPUT_FILE = sys.argv[1]
    OUTPUT_FILE = INPUT_FILE.split(".")[0] + "_out.txt"

    # 2. parse inputfile
    orders = parseInput(INPUT_FILE)  # list of tuples

    # 3. calcuate seats assignment
    results = []
    seatsLeft = R * C
    nextAvailRow, nextAvailCol = 0, 0
    for oneOrder in orders:  # each tuple
        seatsLeft, nextAvailRow, nextAvailCol, oneResult = assignSeats(
            oneOrder[1], seatsLeft, nextAvailRow, nextAvailCol)
        results.append((seatsLeft, nextAvailRow,
                        nextAvailCol, oneOrder[0], oneResult))

    print("(seatsLeft, nextAvailRow, nextAvailCol, Order#, assignmentResult)")
    for i in results:
        print(i)
    print("\n")

    # 4. generate results from the calculated seats assignment
    resultInLines = generateOutputLines(results)
    writeIntoOutputFile(OUTPUT_FILE, resultInLines)  # sys.argv[2]
    # return /path/to/outputfile
    print("The relative path to outputfile:\t./" + OUTPUT_FILE)
