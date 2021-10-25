num1 = 42       #variable declaration
num2 = 2.3      #variable declaration
boolean = True      #boolean
string = 'Hello World'      #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      #dictionary
fruit = ('blueberry', 'strawberry', 'banana')       #tuple
print(type(fruit))      #log - tuple
print(pizza_toppings[1])        #log - 
pizza_toppings.append('Mushrooms')      #list - add value
print(person['name'])       #log - dictionary - access value
person['name'] = 'George'       #list - access value
person['eye_color'] = 'blue'    #list - access value
print(fruit[2])     #log - list - access value - tuple

if num1 > 45:       # conditional
    print("It's greater")       #log
else:       #conditional
    print("It's lower")     #log

if len(string) < 5:     #conditional
    print("It's a short word!")     #log
elif len(string) > 15:      #conditional
    print("It's a long word!")      #log
else:       #conditional
    print("Just right!")        #log

for x in range(5):      #for loop
    print(x)        #log
for x in range(2,5):        #for loop
    print(x)        #log
for x in range(2,10,3):     #for loop
    print(x)        #log
x = 0       #variable declaration
while(x < 5):       #conditional - while
    print(x)        #log
    x += 1      #var declaration

pizza_toppings.pop()        #list - add value
pizza_toppings.pop(1)       #list - delete value

print(person)       #log
person.pop('eye_color')     #dictionary - delete value
print(person)       #log

for topping in pizza_toppings:      #access value in list
    if topping == 'Pepperoni':      #conditional - if
        continue        #for loop - continue
    print('After 1st if statement')     #log
    if topping == 'Olives':     #conditional - if
        break       #for loop - break

def print_hello_ten_times():        #function
    for num in range(10):       #for loop
        print('Hello')      # log

print_hello_ten_times()     #function

def print_hello_x_times(x):     #function definition
    for num in range(x):        #for loop
        print('Hello')      #log

print_hello_x_times(4)      #function parameter

def print_hello_x_or_ten_times(x = 10):     #function definition
    for num in range(x):        #for loop
        print('Hello')      #log

print_hello_x_or_ten_times()        #function
print_hello_x_or_ten_times(4)       #function - parameter


"""
Bonus section
"""

# print(num3)       #print(num2)
# num3 = 72     
# fruit[0] = 'cranberry'        #fruit[0].append('cranberry')
# print(person['favorite_team'])        
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)