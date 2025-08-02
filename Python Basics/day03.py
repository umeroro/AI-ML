# formatted strings

import math
car_make = '  Nissan r35'
varient = 'gtr r35'
car_details = f"{car_make} {varient}"
print(car_details)

# strings methods

print(car_details.upper())
print(car_details.lower())
print(car_details.strip())
print(car_details.lstrip())
print(car_details.rstrip())
print(car_details.find("S"))
print(car_details.replace("r35", "r34"))
print("Nissan" in car_details)
print("Nissan" not in car_details)

# Math Module

print(math.ceil(1.0))
