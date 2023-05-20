# Syed Khurshid, SID:010081191

# This is where the hashing table class is used to generate for the address of packages
# Data is read from the package file with package information
import csv
from hashingData import HashingData


class Packages():
    # Converting data to match the numbers
    hasher = HashingData()
    # Constructor

    def __init__(self, id, address, city, state, zip, delivery, weight, note, starting_time, delivery_address, status, truck_number, delivery_time):
        self
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery = delivery
        self.weight = weight
        self.note = note
        self.starting_time = starting_time
        self.delivery_address = ''
        self.status = 'at Hub'
        self.truck_number = truck_number
        self.delivery_time = delivery_time

    # Package information is generated from this

    def get_single_package(self, key):
        # Getting the individual package from the hash table
        package = self.hasher.search(str(key))
        if package is not None:
            return package
        else:
            return None

    # Getting all the packages at that is not requested
    def get_all_packages(self):
        # Getting all the pacakges from the Hash Table
        packages = self.hasher.get_hash_Table()
        if packages is not None:
            return packages
        return None
