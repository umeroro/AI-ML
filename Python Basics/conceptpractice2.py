# Factorial of a Number

number = int(input("Enter Number : "))
factorial = 1
for num in range(1,number+1):
    factorial = factorial * num
print(f"Factorial of {number} : {factorial}")

# Check Prime Number

number = int(input("Enter Number : "))
for num in range(2,number-1):
    if number % num == 0:
        print("Number is not Prime")
        break
    else: 
        print("Number is Prime")
        break
    
# Reverse a String

word = [input("Enter : ")]
for str in word:
    print(str[-1::-1])

