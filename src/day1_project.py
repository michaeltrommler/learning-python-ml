# speed analyzer function with random inputs

import random
speeds = [random.randint(20,120) for _ in range(50)] # generate random list with 50 elements, integers between 20 and 120

def analyze_speeds(speed_list):
    return {"Minimum": min(speed_list),
            "Maximum": max(speed_list),
            "Average": sum(speed_list) / len(speed_list)
    } # return dictionary with respective values

print(speeds)

result = analyze_speeds(speeds)

if result["Average"] > 72:
    print("average too high, risk detected!")
else:
    print("average acceptable")

print(result)