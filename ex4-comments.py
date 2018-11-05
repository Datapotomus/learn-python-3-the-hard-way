#This is the amount of cars there are as a variable.
cars = 100
#This is how many seats a car has.
space_in_a_car = 4.0
#These are how many drivers are on the road. Drivers is assigned a 30.
drivers = 30
#How many passengers all the cars can have.
passengers = 90
#This will take the amount of cars and subtract it from the amount of drivers. Since there are more
# cars and less drivers, because you can only have a not driven if it doesn't have a driver. 
cars_not_driven = cars - drivers
# This variable can equal the other, because to drive a car you have to have a driver.
cars_driven = drivers
# This is the amount of space in the car (4 seats), multiplied by the amount of cars their are.
carpool_capacity = cars_driven * space_in_a_car
# This will tell you how many cars on average have passengers. If you change the passenger number or
# or cars driven it will change the value of this variable.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")