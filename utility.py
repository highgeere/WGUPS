# Manually sorted truck manifests
# Replace with package sorting algorithm before production
# sorting rules:
def sort_packages():
    truck1 = [13, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4, 26, 34]
    truck2 = [3, 18, 36, 38, 6, 25, 28, 31, 30, 29, 32, 2]
    truck3 = [5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 29, 33, 35, 39]
    return truck1, truck2, truck3


def time_convert(mins):
    hour = "{:02d}".format(int(mins / 60))
    minute = "{:02d}".format(mins % 60)
    time_string = hour + ':' + minute
    return time_string
