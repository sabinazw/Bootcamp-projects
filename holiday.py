def pattern_decorate(text):
    print("="*70)
    print(f"\t\t\t{text}")
    print("="*70)

def check_if_digit(value)-> int:
    """
    Check if the value is a digit
    :param value: number of hotel nights or car rental days
    :type value: Any
    :return: number of hotel nights or car rental days
    :rtype: int
    """    
    while not value.isdigit():
            print("Enter numbers only!")
            value = input("Enter number of days/nights: ")
    return int(value)

def hotel_cost(num_nights:int, price_per_night = 100)->int:
    """
    Calculate the hotel cost
    :param num_nights: number of hotel nights
    :type num_nights: int
    :return: cost of the hotel stay
    :rtype: int
    """ 
    return num_nights * price_per_night

def plane_cost(city_flight:str)->int:
    """
    Calculate the plane cost
    :param city_flight: name of the city you are flying to
    :type city_flight: str
    :return: cost of flight
    :rtype: int
    """ 
    while city_flight not in flights.keys():
        print("Choose from Berlin, Rome or Paris")
        city_flight = input("Where are you flying to: Berlin, Rome or Paris ?: ")
    flight_price = flights[city_flight]
    return flight_price

def car_rental(rental_days:int, daily_rental_cost = 50)->int:
    """
    Calculate the car rental cost
    :param rental_days: number of days
    :type rental_days: int
    :return: cost of car rental
    :rtype: int
    """
    return rental_days * daily_rental_cost

pattern_decorate("SUMMER HOLIDAY COST")

# Calculate the flight cost
flights = {"Berlin":250, "Rome":300, "Paris":350}
city_flight = input("Where are you flying to: Berlin, Rome or Paris ?: ")
total_plane_cost = plane_cost(city_flight)

# Calculate the hotel cost for whole stay
nights = input("Number of nights you will be staying at the hotel: ")
num_nights = check_if_digit(nights)
total_hotel_cost = hotel_cost(num_nights)

# Calculate the car rental cost for whole stay
rental = input("Number of days you will be hiring a car: ")
rental_days = check_if_digit(rental)
total_car_rental = car_rental(rental_days)

print()
print(f"Plane cost: £{total_plane_cost}")
print(f"Hotel cost: £{total_hotel_cost}")
print(f"Car rental cost: £{total_car_rental}\n")

# Calculate total cost of holidays
def holiday_cost(hotel_cost = total_hotel_cost, 
                 plane_cost = total_plane_cost, car_rental = total_car_rental):
    return hotel_cost + plane_cost + car_rental


# The `if __name__ == "__main__":` block is used to check if the current script
# is being run directly or if it is being imported as a module.
if __name__ == "__main__":
    total_holiday_cost = holiday_cost()
    print(f"Your total holiday cost is £{total_holiday_cost}\n")
    print("="*70)


