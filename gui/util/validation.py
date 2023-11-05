import sys
#from lib.models.user_input import UserInput
from lib.enums.keys import CharacterInput
#from gui.components import keyboard

# error_list = []
# user_input_list = '.'


# def isValid(user_input : UserInput, error_list):
#     # run every check function to make sure the calculator doesn't break
        
#     # run check_parenthesis
#     check_parenthesis(error_list)
    
    
#     # run check_operator
#     #check_operator(user_input_string, error_list)
    

#     # return list of strings that holds error messages
#     # if no messages in error_list user_input_string is valid
#     return len(error_list) == 0

# def check_parenthesis(user_input : UserInput, list):
#     # check if there is a mismatch of parenthesis
#     left_paren = user_input_list.count('(')
#     right_paren = user_input_list.count(')')
#     difference = left_paren - right_paren
    
#     if difference > 0:    
#         list.append(f"Missing {abs(difference)} right parentheses.")
#     elif difference < 0:
#         list.append(f"Missing {abs(difference)} left parentheses.")
        
#     # keep track of the previous index
#     counter = -1
#     prev_index = ''
#     # check inside the parentheses
#     for index in user_input_list:
#         if counter >= 0:
#             prev_index = user_input_list[counter]
        
#         if index == ')' and not (ord(prev_index) >= 48 and ord(prev_index) <= 57):
#             print(f"No operand after operator: {prev_index}{index}")
#             break
#         elif prev_index == '(' and index == '-' or index == '+' or index == '*' or index =='/':
#             print(f"No operand before operator: {prev_index}{index}")
        
#         counter += 1
    

# def check_operator(user_input_list, error_list):
#     # check if there is an operator in between operands
#     before_operator = ''
#     operator = ''
#     after_operator = ''
#     for index in user_input_list:
#         if index == '-' or index == '+' or index == '*' or index == '/':
#             operator = index
#         elif ord(index) >= 48 and ord(index) <= 57 and operator == '':
#             before_operator += index
#         elif ord(index) >= 48 and ord(index) <= 57 and operator != '':
#             after_operator += index
            
#         if index == ')':
#             print(before_operator,operator,after_operator)
#             before_operator = ''
#             operator = ''
#             after_operator = ''

def validate(user_input_list) -> bool:
    return check_decimal_points(user_input_list)
    
    

def check_decimal_points(user_input_list) -> bool:
    
    temp_list = [x for x in user_input_list if x == CharacterInput.DECIMAL_POINT]
    
    return len(temp_list) <= 1

# #check_parenthesis(user_input_string, error_list)

# #check_operator(user_input_string, error_list)

#print(validate([CharacterInput.DECIMAL_POINT]))
