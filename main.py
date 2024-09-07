def calculate_trip_cost(distance, mileage, fuel_price):
    fuel_consumption = distance / mileage
    trip_cost = fuel_consumption * fuel_price
    return trip_cost

distance = float(input("Enter the distance of the trip in kilometers: "))
print()
mileage = float(input("Enter the mileage of your car(km/l): "))
print()
fuel_price = float(input("Enter the price of fuel per liter: "))
print()
total_cost = calculate_trip_cost(distance, mileage, fuel_price)

print(f"The total cost of the trip will be {total_cost:.2f} rupees")
