import csv
from hashtable import HashTable
from package import Package

# This module loads the data from CSVs into the desired data structure

# Specify data file paths and initialize empty hash table object
package_list = "data/packages.csv"
package_table = HashTable()
distances = "data/distances.csv"
addresses = "data/addresses.csv"


# Parse package list, create a package object for each, and store in the hash table
# O(n)
def read_packages():
    with open(package_list, 'r', encoding="utf-8-sig") as infile:
        csvreader = csv.reader(infile)
        for row in csvreader:
            p = Package(row)
            package_table.insert(p.package_id, p)
        return package_table


# Parse distance table into 2d matrix - O(n)
def read_distances():
    with open(distances, 'r', encoding="utf-8-sig") as infile:
        distance_matrix = []
        csvreader = csv.reader(infile)
        for row in csvreader:
            distance_matrix.append(row)
        return distance_matrix


# Parse address data into dictionary - O(n)
# Key = the address
# Value = [address_id, address name]
def read_addresses():
    with open(addresses, 'r', encoding="utf-8-sig") as infile:
        address_map = {}
        csvreader = csv.reader(infile)
        for row in csvreader:
            address_map[row[0]] = [int(row[1]), row[2]]
        return address_map

