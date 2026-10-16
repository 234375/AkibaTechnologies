destination = input("Enter destination: ")
distance = float(input("Enter distance in kilometer: "))
speed = float(input("Enter average speed in km/h: "))

travel_time = distance / speed
hours = int(travel_time)
minutes= int((travel_time - hours)*60)

print()
print("========================================")
print("           TRAVEL PLANNER        ")
print("========================================")

print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h")
print("----------------------------------------")
print(f"Estimated Travel Time: {travel_time} hours")
print (f"{hours} hours and { minutes} minutes")
print("========================================")