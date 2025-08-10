# Ternitory operator

age = 10
message = "eligible" if age >= 18 else "Not Eligible"
print(message)

# logical operators
# Short-circuit Evaluation

high_income = True
good_credit = True
student = True
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# Chaining comparsion operators

age = 22

if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")

# loops

for i in range(10):
    print(i)


for i in range(0, 10, 2):
    print(i, i*("."))
