# Scott Aylward
# ID: 000748921

from importdata import *
from utility import sort_packages, time_convert

# Initialize main data structures and load data from CSVs
# hash_table
package_table = read_packages()
# 2d matrix
distance_matrix = read_distances()
# python dict
addresses = read_addresses()

travel = []


# Identify the next destination based on current location and truck manifest
# Nearest neighbor algorithm uses distance matrix to check addresses of
# remaining packages and find the one closes to the current stop
# O(n)
def choose_next(current_location_num, truckload):
    # Initial short route value should be greater than the largest single value
    # in the distance matrix. Could be automated, but could also be made
    # arbitrarily large to always be valid as a static value, e.g., 10000.00
    short_route = 20.0
    next_package = None
    next_addr_num = None
    # iterate through package IDs still on truck and choose next
    # O(n)
    for package_num in truckload:
        # Get the associated package obj
        package = package_table.lookup(package_num)
        # Use the package address as key for address dict, and get address ID
        package_addr_num = addresses[package.address][0]
        # get the distance between current location and package location
        # Conditional statement is only needed because the distance matrix is
        # one-sided. Consider completing the matrix before or after
        # import to avoid this if/else
        if package_addr_num > current_location_num:
            dist = float(distance_matrix[package_addr_num][current_location_num])
        else:
            dist = float(distance_matrix[current_location_num][package_addr_num])
        # If this route is shorter than others we've checked, use it for now
        if dist < short_route:
            short_route = dist
            next_package = package
            next_addr_num = package_addr_num

    return next_package, next_addr_num, short_route


# 'Deliver' each package from a truck and return to Hub, tracking distance and time
# O(n^2) complexity for run_route, as it calls choose_next within a for loop
def run_route(truck, route_time):
    # Update all package status when the truck leaves the hub
    for p_id in truck:
        package = package_table.lookup(p_id)
        package.status = "En route"
    # Represents the Hub as starting point
    num = 0
    total_dist = 0
    # Run once for each package - O(n)
    for i in range(len(truck)):
        # Package obj, address ID, and next distance returned
        p, num, dist = choose_next(num, truck)
        # Use distance, known truck speed to determine minutes taken for delivery
        route_time += int((dist / 18) * 60)
        # Format time string based on current minutes
        p.delivery_time = time_convert(route_time)
        # Update status
        p.delivery_status = "Delivered at " + p.delivery_time
        total_dist += dist
        # Remove delivered package from the truck manifest
        truck.remove(p.package_id)

    # Record distance/time for return to Hub from last package stop
    hub_dist = float(distance_matrix[num][0])
    total_dist += hub_dist
    route_time += int((hub_dist / 18) * 60)

    return total_dist


# Simulate package delivery. Load packages on trucks and run each
# truck's route at the appropriate start time
# O(n^2) complexity from called run_route() function
def run_sim():
    # Get truck manifests from package sorter
    t1, t2, t3 = sort_packages()
    # This could be an additional return value from the sorter
    # Currently using static start times based on package data
    # Truck 1 leaves at 8AM to deliver the packages with earliest deadline
    t1_start_mins = 480
    # Truck 2 leaves at 9:06AM with packages that arrived late from the depot
    t2_start_mins = 546
    # Truck 3 leaves at 10:20, when the first driver is back with truck 1
    # and we have the corrected address for package 9
    t3_start_mins = 620

    # run each truck route and record the distance traveled
    # Each truck route is O(n^2)
    t1_distance = run_route(t1, t1_start_mins)
    travel.append(t1_distance)
    t2_distance = run_route(t2, t2_start_mins)
    travel.append(t2_distance)
    # It's 10:20, and we have the corrected address for Package ID 9
    package_table.lookup(9).notes = "Address corrected at 10:20AM"
    t3_distance = run_route(t3, t3_start_mins)
    travel.append(t3_distance)
    all_distance = t1_distance + t2_distance + t3_distance
    travel.append(all_distance)


# Main function to kick off the simulation and control the CLI
if __name__ == '__main__':
    # Run the route simulation.
    run_sim()
    # Help text for the CLI
    prompt_text = '''
        Welcome to the WGUPS package tracking system.
        -------
        The following functions are available:
        - Enter 'route' to view delivery route information
        - Enter a time(hh:mm) to retrieve all package status
        information for that time
        - Enter a package ID to view information for that package
        - Enter 'quit' to exit the program

    '''
    user_input = ''
    # Limited 'CLI' for the program
    # Consider replacing with proper CLI via argparse/optparse
    while user_input != 'quit':
        user_input = input(prompt_text)
        # get distance info - O(1)
        if user_input == 'route':
            print("Truck 1 distance traveled: %.2f miles" % travel[0])
            print("Truck 2 distance traveled: %.2f miles" % travel[1])
            print("Truck 2 distance traveled: %.2f miles" % travel[2])
            print("Total distance traveled: %.2f miles" % travel[3])
        # Get all package data - O(n)
        elif ":" in user_input:
            delivered = []
            not_delivered = []
            for i in range(1, package_table.table_size()):
                p = package_table.lookup(i)
                if p.delivery_time <= user_input:
                    delivered.append(p)
                else:
                    not_delivered.append(p)
            print("Packages delivered by %s:" % user_input)
            for p in delivered:
                p.print_inline()
            print("\n")
            print("Packages not delivered by %s:" % user_input)
            for p in not_delivered:
                p.print_inline()
        # Get single package data - O(1)
        elif len(user_input) < 3:
            try:
                package_key = int(user_input)
                if package_key in range(1, package_table.table_size() + 1):
                    package_table.lookup(package_key).print_long()
                else:
                    print("Invalid entry!")
            except Exception:
                print("Invalid entry!")
        else:
            if user_input != 'quit':
                print("Invalid entry!")
