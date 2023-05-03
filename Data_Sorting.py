# # Syed Khurshid, SID:010081191
import csv
from Truck import Truck
from hashingData import HashingData
from Package import Packages
# This is where the list of packages is then sorted to seperate truck objects for delivery


class DataSort():
    def __init__(self):
        pass

    # Creating the truck list
    # Truck Number 1
    Truck_1 = Truck()
    # Truck Number 2
    Truck_2 = Truck()
    # Truck Number 3
    Truck_3 = Truck()
    # Creating the Hashing Data
    my_Hash = HashingData()

    # Data is sorted from the package list and assigned to the truck lists
    # Conditionally certain criteria are identified and assigned to each truck object and converted to a list
    def sort_to_trucks(self):
        with open('./data/package.csv') as locationCSV:
            locCSV = csv.reader(locationCSV, delimiter=',')

            for row in locCSV:
                id = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                delivery = row[5]
                size = row[6]
                notes = row[7]
                starting_time = ''
                delivery_address = ''
                status = "At Hub"

                value = [id, address, city, state, zip, delivery,
                         size, notes, starting_time, delivery_address, status]

                # Conditional statements to determine which truck a package should be located and put these packages into a nested list for quick loaded
                # Correct incorrect package details
                if '10:30' != value[5] and '84104' != value[4]:
                    self.Truck_3.add_to_Truck(value)

                # To filter out EOD to truck delivery
                if value[5] != 'EOD':
                    if 'Must be' in value[7] or 'None' in value[8]:
                        self.Truck_1.add_to_Truck(value)

                # Second truck delivery
                if 'Can only be' in value[7] or 'Delayed' in value[7]:
                    self.Truck_2.add_to_Truck(value)

                # Putting whatever is not remaining in in first truck and second truck, then placing them in  third truck
                if value not in self.Truck_1.get_truck_list() and value not in self.Truck_2.get_truck_list() and value not in self.Truck_3.get_truck_list():
                    if len(self.Truck_2.get_truck_list()) < len(self.Truck_3.get_truck_list()):
                        self.Truck_2.add_to_Truck(value)
                    else:
                        self.Truck_3.add_to_Truck(value)

            # Inserting trucks to the main list as well
            self.my_Hash.insert(id, value)

     # Now being able to deliver trucks list

    def get_first_truck(self):
        return self.Truck_1.get_truck_list()

    # Getting Truck 2
    def get_second_truck(self):
        return self.Truck_2.get_truck_list()

    # Getting Truck 3
    def get_third_truck(self):
        return self.Truck_3.get_truck_list()
