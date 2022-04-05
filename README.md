# Movie Theater Seating Challenge - 2020

Language used: Python

# Assumptions:

1. The program should tell if the seats are insufficient for the upcomibg order -> don't order any seats and let the customer decide if they still want to watch the movie with fewer customers.
2. The reservation numbers are in sequential order i.e. R001, R002, R003,...
3. There will never be a group that’s too large to fit within a single row
4. R = Number of rows, C = Number of columns  

Customer Safety - Must be enforced:
1. A buffer of three seats and/or one row is required.

Customer Satisfaction:
1. Customer groups will be more satisfied if they sit next to each other
2. Customers who order tickets first should be given a better viewing experience by assigning them to the best seats. Hence, customers who order first will take the best rows, until they're filled up. Assume the best seats are from row R/2 to R/2+3. 

Maximum Theater Utilization:
1. Once row R/2 to R/2+3 are filled up, the rest of seats will be filled from back to front (i.e. row R to 1), and from column 0-C in each row. 
2. Each row is filled from left to right (i.e. from column 1-C).

# Algorithm
Always keep track of the number of available seats and the row/col of the next seat location.
Fill the best rows first.
Fill the rest of rows from row R to 1.
For each order request: 
1. check if there's no sufficient seat -> return an empty list of assigned seats
2. assign the next connected seats to customer. If there's not enough seats in the same row, go to the next row
3. calculate the next available seat position, num of seatsLeft for the next order based on the seatBuffer.
4. -> return list of assigned seats, seatsLeft, nextAvailRow, nextAvailCol

# Steps for running
1. Download repository
2. Navigate to the downloaded repository
3. Run “python3 seat_assigner_main.py input.txt” in terminal

# Testing
1. Min requirement - unit testing and regression testing.

# Design Principles
1. Open/Closed
2. 

# This version
1. For the sake of time, the current version will only fill seats from row R to 1, and from column 1 to C in each row.

# Optimization in the future
1. use satisfaction points of each seat to optimize the seat assignments
2. skip single available seat when a group comes
