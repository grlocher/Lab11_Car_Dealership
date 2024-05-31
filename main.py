from classes import Vehicle, Truck, Motorcycle

# Lists for the vehicles
trucks = [
    Truck('Pickup', 20000, 3599.99),
    Truck('Cybertruck', 2500, 100000),
    Truck('Toyota', 0, 15000)
]

motorcycles = [
    Motorcycle('Harley', 3000, 2500.50, 120),
    Motorcycle('Moped', 100, 1999.99, 65),
    Motorcycle('Dirt Bike', 290, 3000, 90)
]

# Empty list to be filled with user selections
vehicles_to_compare = []

print('Hello')
print('Welcome to GC Bikes & Trucks!')

keep_going = 'y'
while keep_going == 'y':
    view = str(input('Would you like to view bikes or trucks? (b or t) >> ')).lower()
    print()
    if view == 'b':
        number = 1
        for motorcycle in motorcycles:
            print(f'{number}. {motorcycle.get_info()}')
            number += 1
    elif view == 't':
        number = 1
        for truck in trucks:
            print(f'{number}.  {truck.get_info()}')
            number += 1
    else:
        print('Not a valid option, please try again.')

    print()
    compare = str(input('Would you like to add a vehicle to compare? (y/n) >> '))
    if compare == 'y':
        compare_list = int(input('Which vehicle would you like to add? >> '))
        if view == 'b':
            if 1 <= compare_list <= len(motorcycles):
                vehicles_to_compare.append(motorcycles[compare_list - 1])
                print(f"{motorcycles[compare_list - 1].make} added!")
                motorcycles.remove(motorcycles[compare_list - 1])
        if view == 't':
            if 1 <= compare_list <= len(trucks):
                vehicles_to_compare.append(trucks[compare_list - 1])
                print(f"{trucks[compare_list - 1].make} added!")
                trucks.remove(trucks[compare_list - 1])
        keep_going = input('Would you like to look at more vehicles? (y/n) >> ')
    else:
        print('Not a valid option, please try again.')


# Printing the vehicle type and the noise
for vehicle in vehicles_to_compare:
    print()
    print(f'{vehicle.get_info()}')
    vehicle.make_noise()