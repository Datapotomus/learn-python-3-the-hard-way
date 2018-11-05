name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 70 # inches
weight = 200 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = 2.54 * height
weight_in_kg = round(0.453592 * weight, 2)


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_in_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
total_metric = round(age + height_in_cm + weight_in_kg, 2)
print(f"In Metric if I add {age}, {height_in_cm}, and {weight_in_kg} I get {total_metric}.")

