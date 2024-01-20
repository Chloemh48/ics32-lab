# lab1.py
# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python
# Chloe Yuan


def print_message():
     return 'Welcome to ICS 32 PyCalc!'
def get_input():
    
    num1 = int(input('Enter your first operand:'))
    num2 = int(input('Enter your second operand:'))
    operator = input('Enter your desired operator (+, -, or x):')
    return num1, num2, operator  

def calculation(n, m, operator):
    if operator == "+":
        return f'The result of your calculation is:{n + m}'
    elif operator == "-":
        return f'The result of your calculation is:{n - m}'
    elif operator == "*":
        try: 
            return f'The result of your calculation is:{n * m}'
        except ZeroDivisionError:
            return "Cannot divide a number by zero! Try again"
    elif operator == "/":
        return f'The result of your calculation is:{n / m}' 
    else:
        return f'Invalid input! Try again!'   

def main():
    print(print_message())
    num1, num2, operator = get_input()
    print(calculation(num1, num2, operator))
   
main()
    
