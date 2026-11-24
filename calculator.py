import math
# SIMPLE CALCULATOR
# ENTER ONLY TWO NUMBERS
a = str(input("Enter the first number:  "))
Num_1 = int(a)

b = str(input("Enter the second number:  "))
Num_2 = int(b)

print("\n .....CALCULATOR RESULTS.....")

# ADDITION
print("ADDITION: ", Num_1 + Num_2)

# MULTIPLICATION
print("MULTIPLICATION: ", Num_1 * Num_2)

# SUBTRACTION
print("SUBTRACTION (first - second): ", Num_1 - Num_2)
print("SUBTRACTION (second - first): ", Num_2 - Num_1)

# DIVISION
if Num_2 != 0:
    print("DIVISION (first/second): ", Num_1/Num_2)
else:
    print("DIVISION (first/second):, cannot be divided by zero")
    
if Num_1 != 0:
    print("DIVISION (second/first): ", Num_2/Num_1)
else:
    print("DIVISION (second/first):, cannot be divided by zero")

# EXPONENTIATION
print("EXPONENTIATION (first ** second): ", Num_1 ** Num_2)
print("EXPONENTIATION (second ** first): ", Num_2 ** Num_1)

# MODULUS
if Num_2 != 0:
    print("MODULUS (first % second): ", Num_1 % Num_2)
else:
    print("DIVIS (first % second):, cannot be divided by zero")
    
if Num_1 != 0:
    print("MODULUS (second % first): ", Num_2 % Num_1)
else:
    print("MODULUS (second % first):, cannot be divided by zero")