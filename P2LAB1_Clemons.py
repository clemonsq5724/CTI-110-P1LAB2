"""CTI 110
P2LAB1 -Gas Prices
Clemons
9/7/23

Write a program with car's gas milage (miles/gallon) and the cost of a gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1f:.2f} {your_value2:.2f} {your_value3:.2f}')


"""

#ask for miles per gallon
miles_per_gallon = float(input("What is the car's MPG?"))
#ask for price per gallon of gas
price_per_gallon = float(input("price per gallon?"))

#show the price per mile to drive
#unit we want is $/miles
price_per_mile = price_per_gallon / miles_per_gallon

#print("This vehicle costs $", price_per_mile, "to drive 1 mile.")
# f strings are like this: {variable:.2f} for 2 decimals places
print(f"This vehicle costs ${ price_per_mile:.2f} to drive 1 mile.")

# Last step: Tell the user the cost to drive 20, 75, and 500 miles

print(f"This vehicle costs $ {price_per_mile * 20:.2f} to drive 20 miles.")
print(f"This vehicle costs $ {price_per_mile * 75:.2f} to drive 75 miles.")
print(f"This vehicle costs $ {price_per_mile * 500:.2f} to drive 500 miles.")