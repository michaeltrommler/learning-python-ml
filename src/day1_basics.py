# a simple basic python script to cover the most basic principles and building blocks

# variables
speed = 50
temperature = 23.5
status = "ok"

print(speed, temperature, status) # print values of variables
print(type(speed), type(temperature), type(status)) # print types of variables

# lists and dictionaries

speeds = [40, 42 ,44, 41, 39] # list
car = {"model": "ID.3", "battery": 77, "status": "active"} # dictionary

print(speeds[0], speeds[-1]) # print first and last element
print(car["model"]) # print value for key model
print(car["status"]) # print value for key status

# control structures

speed = 72
if speed > 70:
    print("Warning: speed limit exceeded!")
else:
    print("Everything is fine")

# loops

# for-loop
for s in speeds:
    print("Speed:",s)

# while-loop
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1

# functions
def average_speed(speed_list):
    return sum(speed_list) / len(speed_list)

print ("Average:", average_speed(speeds))