def HotelCost(days):
    return 140 * days

def PlaneCost(city):
    if city == 'Charlotte':
        return 190
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 150
    elif city == 'Los Angeles':
        return 470

def car_rental_cost(days):
    return 40 * days - (50 if days >= 7 else 20 if days >= 3 else 0)
    
input_city = input("Enter your destination city (Charlotte, Tampa, Pittsburgh, Los Angeles): ")
input_days = int(input("Enter number of days for the trip: "))

total_cost = HotelCost(input_days) + PlaneCost(input_city)
print(f"The total cost for your trip to {input_city} for {input_days} days is: ${total_cost}")