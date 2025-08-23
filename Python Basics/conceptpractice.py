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