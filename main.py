from importdata import *
from utility import sort_packages, time_convert

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

package_table = read_packages()
distance_matrix = read_distances()
addresses = read_addresses()

travel = []

def choose_next(current_location_num, truckload):
    short_route = 20.0
    next_package = None
    next_addr_num = None
    for package_num in truckload:
        try:
            package = package_table.lookup(package_num)
            package_addr_num = addresses[package.address][0]
            if package_addr_num > current_location_num:
                dist = float(distance_matrix[package_addr_num][current_location_num])
            else:
                dist = float(distance_matrix[current_location_num][package_addr_num])
            if dist < short_route:
                short_route = dist
                next_package = package
                next_addr_num = package_addr_num
        except TypeError:
            pass
    truckload.remove(next_package.package_id)
    return next_package, next_addr_num, short_route


def run_route(truck, start):
    for p_id in truck:
        package = package_table.lookup(p_id)
        package.status = "En route"
    num = 0
    drive_time = start
    total_dist = 0
    for i in range(len(truck)):
        p, num, dist = choose_next(num, truck)
        drive_time += int((dist / 18) * 60)
        p.delivery_time = time_convert(drive_time)
        p.delivery_status = "Delivered at " + p.delivery_time
        total_dist += dist
    # return to the hub
    hub_dist = float(distance_matrix[num][0])
    total_dist += hub_dist
    drive_time += int((hub_dist / 18) * 60)
    return total_dist


def run_sim():
    t1, t2, t3 = sort_packages()
    t1_start_mins = 480
    t2_start_mins = 546
    t3_start_mins = 620

    t1_distance = run_route(t1, t1_start_mins)
    travel.append(t1_distance)
    t2_distance = run_route(t2, t2_start_mins)
    travel.append(t2_distance)
    package_table.lookup(9).notes = "Address corrected at 10:20AM"
    t3_distance = run_route(t3, t3_start_mins)
    travel.append(t3_distance)
    all_distance = t1_distance + t2_distance + t3_distance
    travel.append(all_distance)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_sim()
    user_input = ''
    while user_input != 'quit':
        user_input = input(prompt_text)
        if user_input == 'route':
            print("Truck 1 distance traveled: %.2f miles" % travel[0])
            print("Truck 2 distance traveled: %.2f miles" % travel[1])
            print("Truck 2 distance traveled: %.2f miles" % travel[2])
            print("Total distance traveled: %.2f miles" % travel[3])
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
