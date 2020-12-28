# Beginner - Functions with Outputs

# Functions with Outputs
'''
def my_function():
    return 3 * 2
    
output = my_function()
'''

# https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
# https://docs.python.org/3/library/stdtypes.html#str.title
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

print("================================================================")

# Example - Days in Month
'''
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.: 28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
'''

def is_leap(year):
    '''
    判斷輸入年是否為閏年
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """
    輸入年及輸入月當月的天數
    """
    if month > 12 or month < 1:
        return "Invalid month!"
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
    if is_leap(year) and month == 2:
        return 29
    
    return month_days[month - 1]
  
  
# 🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print("================================================================")

# Docstrings
# 函式內的第一列可放供外界使用時顯示的註釋
def docstrings():
    '''
    這裡放置此函式的說明文字
    '''
    return True

docstrings()

print("================================================================")

# Calculator

from day010_art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()

