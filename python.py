userName = input("Your Name:")
print(f"Hello {userName}!")
function
def add_two_values(num1,num2):
    return num1+num2


n1 = int(input("Enter First Number"))
n2 = int(input("The second one"))
sum = add_two_values(n1,n2)

print(f"{n1} + {n2} = {sum}")

Basic maths

num1 = 10
num2 = 5

addition = num1 + num2

subtraction = num1 - num2

multiplication = num1*num2

division = num1/num2

print(f"Addition = {addition}")
print(f"subtraction = {subtraction}")
print(f"Multiplication = {multiplication}")
print(f"Division = {division}")

person_name = "Shaikat"
food = "Chicken-burger"
connected_string = person_name + food
print(connected_string)
value = 9
Shaikat_with_value = person_name + value
print(Shaikat_with_value)

print(f"Length of name: {len(person_name)}")

list

grocery_list = ["rice","potato","tomate"]

print(grocery_list)

grocery_list.append("papaya")

print(grocery_list)

# another way for list

l1 = list((1,"computer",4.5,"hello_world","hi shaikat!"))
print(l1)
l1.append("hello Harm")
print(l1)

print(li[4])
item2_g_list = grocery_list[1]

print(item2_g_list)

name_list = list(("Shaikt","Supta","Harm","Alpha","Grim Reaper"))
# name_list.sort()
print(name_list)
sorted_name = sorted(name_list) #This sorted and sort function are not same
print(sorted_name)
marks = int(input("Your marks:"))

def show_grade(grade):
    print(f"You got {grade}")

if marks >= 80:
    show_grade("A+")
elif marks<80 and marks>=70:
    show_grade("A")
elif marks<70 and marks>=60:
    show_grade("A-")
elif marks<60 and marks>=33:
    show_grade("Passed")
else:
    show_grade("Failed")

inception
if marks>=80 or marks<=10:
    if marks>=80:
        print("you are great")
    else:
        print("You naughty One!")
else:
    print("you are okay!")
number = int(input("Enter number:"))

the_user_is_good = number >=80
print(f"The user is good and it is {the_user_is_good}")




loop in python


def even_odd(number):
    if number%2 == 0:
        return True
    else:
        return False

starting = 0
while(starting<100):
    if even_odd(starting):
        print(f"{starting} is even!")
    else:
        print(f"{starting} is odd!")
    starting = starting + 1


even_numbers_list
even_numbers = []

def check(number):
    if number%2 == 0:
        return True
    else:
        return False
starting = 0
while starting<100:
    if check(starting):
        even_numbers.append(starting)
    starting = starting+1

print(even_numbers)

for loop

limit = int(input("Give the limit:"))

def even(number):
    if number%2==0:
        return True
    else:
        return False

even_numbers = []
for num in range(0,limit):
    if even(num):
        even_numbers.append(num)


print(even_numbers)

grocery_list = ["rice","tomato","papaya","sweets","cucumber"]

for item in grocery_list:
    print(item)

grocery_list1 = ["rice","tomato","papaya","sweets","burger","cucumber"]

for item in grocery_list1:
    if item == "sweets":
        continue
    print(item)

mobiles = ["pixel","motorola","samsung","nokia","i-Phone","oppo","vivo","oneplus"]


for mobile in mobiles:
    if mobile == 'oppo':
        break
    print(mobile)

for i in range(0,10):
    print(i)

for i in range(0,12,2):
    print (i)

for i in range(0,13,3):
    print (i)


grocery = ["tomato","onion","rice","potato","banana"]

for item in range(0,len(grocery)):
    print(grocery[item])
