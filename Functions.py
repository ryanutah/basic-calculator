#Function to perform addition of two numbers
def add(number1, number2): 
    return (number1 + number2) 
  
#Function to perform subtraction of two numbers
def subtract(number1, number2): 
    return (number1 - number2)
  
#Function to perform multiplication of two numbers 
def multiply(number1, number2): 
    return (number1 * number2) 
  
#Function to perform division of two numbers 
def divide(number1, number2): 
    return (number1 / number2)

#Function to perform modulus remainder
def mod(number1, number2):
    return (number1 % number2)

#Function too perform x to the y power
def exponent(number1, number2):
    ans = 1
    for _ in range(0,number2):
        ans *= number1
    return ans