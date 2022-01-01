
pizza_toppings.pop() # type check, data types, composite, list, delete value
pizza_toppings.pop(1) # type check, data types, composite, list, delete value

print(person) # log statement, variable
person.pop('eye_color') # type check, data types, composite, tuple, delete value
print(person) # log statement, variable

for topping in pizza_toppings: # for loop, start
    if topping == 'Pepperoni': # conditional, if
        continue # for loop, continue
    print('After 1st if statement') # log statement, string
    if topping == 'Olives': # conditional, if
        break # for loop, break

def print_hello_ten_times(): # function, argument
    for num in range(10): # for loop, increment
        print('Hello') # log statement, string, function, return

print_hello_ten_times() # function, parameter

def print_hello_x_times(x): # function, argument
    for num in range(x): # for loop, increment, variable
        print('Hello') # log statement, string, function, return

print_hello_x_times(4) # function, parameter

def print_hello_x_or_ten_times(x = 10): # funciton, argument
    for num in range(x): # for loop, increment, varibale
        print('Hello') # log statement, string, function, return

print_hello_x_or_ten_times() # function, return
print_hello_x_or_ten_times(4) # function, return parameter


""" # comment, multiple
Bonus section
"""

# print(num3)                     # comment, single line
# num3 = 72                       # comment, single line
# fruit[0] = 'cranberry'          # comment, single line
# print(person['favorite_team'])  # comment, single line
# print(pizza_toppings[7])        # comment, single line
#   print(boolean)                # comment, single line
# fruit.append('raspberry')       # comment, single line
# fruit.pop(1)                    # comment, single line