import math #importing math module
#using ceil and floor functiom of math module
print('The Floor and Ceiling value of 34.567 are: ' + str(math.ceil(34.567)) + ', ' + str(math.floor(34.567)))

x = 2849
y = -3456
#using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

#using fabs and gcd function
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-345)) + ', ' + str(math.fabs(4534)))

print('The GCD of 8 and 88 : ' + str(math.gcd(8, 88)))
