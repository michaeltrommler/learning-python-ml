# excercises - 10 tasks 
#
# task 1 - temperature warning, if temperature > 90 "overheat" else "ok"
# task 2 - classify speed < 30 "slow" 30-70 "normal" > 70 "too fast"
# task 3 - filter list, given list 10,22,35,5,60,75, only print values > 30
# task 4 - sum of speeds, from previous list, provide a sum of all speeds, use a for-loop
# task 5 - function max value, define funtion to find max value in list
# task 6 - take car dictionary from basics, add new key-value pair odometer 15000
# task 7 - while-loop, countdown from 10 to 0 incl.
# task 8 - list comprehension, create a new speed list with each value doubled
# task 9 - create a get_average function
# task 10 - speed analysis, create funtion analyze_speed(list) that prints min, max and avg

# task 1 - redundant code usage is intentional for practice purposes
temperature = 65
if temperature > 90:
    print("overheat")
else:
    print("ok")
temperature = 99
if temperature > 90:
    print("overheat")
else:
    print("ok")

# task 2- redundant code usage is intentional for practice purposes
speed = 103
if speed > 70:
    print("too fast")
elif speed >= 30:
    print("normal")
else:
    print("slow")
speed = 12
if speed > 70:
    print("too fast")
elif speed >= 30:
    print("normal")
else:
    print("slow")
speed = 53
if speed > 70:
    print("too fast")
elif speed >= 30:
    print("normal")
else:
    print("slow")

# task 3
speeds = [10,22,35,5,60,75]
for s in speeds:
    if s > 30:
        print(s)

# task 4 using for-loop
speedsum = 0
for s in speeds:
    speedsum += s
print(speedsum)

# task 5 currently no error handling or negative, empty imputs
def max_value(speed_list):
    curmax = 0
    for s in speed_list:
        if s > curmax:
            curmax = s
    return curmax

print(max_value(speeds))

# task 6
car = {"model": "ID.3", "battery": 77, "status": "active"} # dictionary from basics
car["odometer"] = 15000
print(car)

# task 7
count = 10
while count >= 0:
    print(count)
    count -= 1

# task 8
doublespeeds = [x*2 for x in speeds]
print(doublespeeds)

# task 9
def get_average(speed_list):
    return sum(speed_list) / len(speed_list)
print(get_average(speeds))

# task 10
def min_value(speed_list):
    curmin = speed_list[0]
    for s in speed_list:
        if s < curmin:
            curmin = s
    return curmin

def analyze_speed(speed_list):
    print("Minimum:", min_value(speed_list))
    print("Maximum:", max_value(speed_list))
    print("Average:", get_average(speed_list))

analyze_speed(speeds)
