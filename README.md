# Movie Theater Seating Challenge - 2020

Language used: Python

# Assumptions:

1. The program should tell if the number of seats left is insufficient for the upcoming group number
2. The reservation numbers are in sequential order i.e. R001, R002, R003,...
3. There will never be a group that’s too large to fit within a single row
4. R = Number of rows, C = Number of columns  

Customer Safety - Must be enforced:
1. A buffer of three seats and/or one row is required.

Customer Satisfaction:
1. Customer groups will be more satisfied if they sit next to each other
2. Customers who order tickets first should be given a better viewing experience. The middle-row and middle-column seats give the best viewing experience, therefore customers who sit there will have the highest satisfaction. Hence, customers who orders first will take the best rows from middle to edge, until row R/2 to R/2+3 are filled up.

Maximum Theater Utilization:
1. Once row R/2 to R/2+3 are filled up, the rest of seats will be filled from row R to 0, and from column 0-C in each row. 


# This version
1. For the sake of time, the current version will only fill seats from row R to 0, and from column 0-C in each row.

# Steps for running
1. Download repository
2. Navigate to the downloaded repository
3. Run “python3 seat_assigner_main.py input.txt” in terminal
