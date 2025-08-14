# For Else

connection_status = False
for i in range(3):
    print("Checking....")
    if connection_status:
        print("Connected")
        break
else:
    print("No Internet")

# Nested Loop

for i in range(5):
    for j in range(5):
        print(i*j)

# Iterables

language_name = "Python"
for i in language_name:
    print(i)

shopping_items = [
    ["Large Bread , Rs: 130"],
    ["2L Coke , Rs: 250"],
    ["Small Butter , 150"]
]
for i in shopping_items:
    print(i)

# while loop

bomb = ""
while bomb.lower() != "difuse":
    print("Warning !!! Bomb Expload in few second")
    bomb = input("Enter Pass : ")
    print(f"Bomb : {bomb}")
