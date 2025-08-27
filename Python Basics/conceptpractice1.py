# program even or odd

number = int(input("Enter Number : "))
if number % 2 == 0 :
    print("Number is Even")
else :
    print("Number is Odd")

# if Positive, Negative, or Zero

number = int(input("Enter Number : "))
if number <= -1:
    print("Number is Negative")
elif number == 0:
    print("Number is Zero")
elif number >= 1:
    print("Number is Positive")

# Sum of Numbers

number = int(input("Enter Number : "))
total = 0
for n in range(1,number+1):
    total = total + n
print(f"Total Sum : {total}")

# multiplication table

number = int(input("Enter Number : "))
for n in range(1,11):
    print(f"{number} * {n} = {number*n}")

# count how many letters

word = input("Enter Word : ")
for w in range (word.__len__()):
    w+=1
print(w)

# List of Number

list = [1,2,3,4,5]
total = 0
print(list[0])
print(list[-1])
for i in list:
    total = total + i
print(total)

# Largest of Two Numbers

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
if a > b:
    print(f"{a} is Larger")
elif a == b:
    print("Both are Equal")
else:
    print(f"{b} is Larger")

# Simple Login System

username = input("Enter username : ")
password = input("Enter Password : ")
if username == "ummorro" and password == "9876":
    print("Login Succesfully")
else:
    print("Wrong Credentital! Try Again")