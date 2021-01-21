# Manually sorted truck manifests - O(1)
# Replace with package sorting algorithm before production
# sorting rules:
# Truck 1 - earliest deadlines, co-delivery requirements, ZIP proximity
# Truck 2 - packages delayed until 9:05 with deadline by 10:30, some that
# must be on truck 2, a couple more for ZIP proximity
# truck 3 - Remaining packages
def sort_packages():
    truck1 = [13, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4, 26, 34, 29, 30]
    truck2 = [3, 18, 36, 38, 6, 25, 28, 31, 32, 2]
    truck3 = [5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39]
    return truck1, truck2, truck3


# Name coule be misleading. Function does not interact with datetime objects
# Just formats a provided number of minutes into a familiar time string - hh:mm
# O(n)
def time_convert(mins):
    hour = "{:02d}".format(int(mins / 60))
    minute = "{:02d}".format(mins % 60)
    time_string = hour + ':' + minute
    return time_string
