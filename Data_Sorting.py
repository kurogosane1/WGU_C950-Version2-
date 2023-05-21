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
    # O(N)
    def sort_to_trucks(self):
        with open('./data/package.csv') as locationCSV:
            locCSV = csv.reader(locationCSV, delimiter=',')
            # O(N)
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
                truck_number = ''
                delivery_time = row[5]
                Package = Packages(id, address, city, state, zip, delivery,
                                   size, notes, starting_time, delivery_address, status, truck_number, delivery_time)
                # value = [id, address, city, state, zip, delivery,
                #          size, notes, starting_time, delivery_address, status, truck_number, delivery_time]
                value = [Package.id, Package.address, Package.city, Package.state, Package.zip, Package.delivery,
                         Package.weight, Package.note, Package.starting_time, Package.delivery_address, Package.status, Package.truck_number, Package.delivery_time]
                # Conditional statements to determine which truck a package should be located and put these packages into a nested list for quick loaded
                # Correct incorrect package details
                if '84104' in value[4] and '10:30' not in value[5]:
                    self.Truck_3.add_to_Truck(value)
                    # self.test3.append(value)

                # To filter out EOD to truck delivery
                if value[5] != 'EOD':
                    if 'Must' in value[7] or 'None' in value[7]:
                        # if len(self.Truck_1.get_truck_list(value)) < 17:
                        self.Truck_1.add_to_Truck(value)
                        # self.test1.append(value)

                # Second truck delivery
                if 'Can only be' in value[7] or 'Delayed' in value[7]:
                    self.Truck_2.add_to_Truck(value)
                    # self.test2.append(value)

                # Putting whatever is not remaining in in first truck and second truck, then placing them in  third truck
                if value not in self.Truck_1.get_truck_list() and value not in self.Truck_2.get_truck_list() and value not in self.Truck_3.get_truck_list():
                    if len(self.Truck_2.get_truck_list()) < len(self.Truck_3.get_truck_list()):
                        self.Truck_2.add_to_Truck(value)
                    else:
                        self.Truck_3.add_to_Truck(value)

                # Inserting trucks to the main list as well
                self.my_Hash.insert(id, value)
    
     # Now being able to deliver trucks list
     # O(1)
    def get_first_truck(self):
        return self.Truck_1.get_truck_list()

    # Getting Truck 2
    # O(1)
    def get_second_truck(self):
        return self.Truck_2.get_truck_list()
        # return self.test2

    # Getting Truck 3
    # O(1)
    def get_third_truck(self):
        return self.Truck_3.get_truck_list()
    # Getting all the Hash Table
    # O(1)

    def get_All_Pacakges(self):
        return self.my_Hash

    # Searching a key value and replacing value in truck
    # O(N)
    def replace_in_truck(self, key, truckList, new_value, truck_number):
        for i in range(0, len(truckList)):
            if truckList[i][0] == key:
                truckList[i] = new_value
                truckList[i][11] = truck_number
