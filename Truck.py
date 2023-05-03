# Syed Khurshid, SID:010081191

# Truck class where the locations are added to the Truck list for
# them to travel to and get there respective location
class Truck():
    def __init__(self):
        # This is where the package addresses are added
        self.truck_list = []
        pass

    # This is to get all the Truck List
    def get_truck_list(self):
        return self.truck_list

    # This is to get the status of the Truck List Packages
    def get_truck_list_status():
        pass

    # This is to add the object to the Truck list
    def add_to_Truck(self, address):
        if address is not None:
            self.truck_list.append(address)
            return True
        else:
            return False

    # This to remove the truck object from the truck list
    def remove_from_Truck(self, key):
       # Searching by the index and then removing from Truck List
       for index, key in enumerate(self.truck_list):
           if self.truck_list[index][0] == key:
               self.truck_list.pop(index)
               return True
           else:
               return False

    # Calculate the time to reach at its destination
    def get_time_to_reach(distance):
        # Getting the time to travel to the destination point
        # Since speed is distance upon time, time travelled is distance upon speed since truck speed is 18 miles per hour
        travelTime = distance / 18
        # Convert to minutes in layout
        distanceMin = '{0:02.0f}:{1:02.0f}'.format(*divmod(travelTime * 60, 60))
        # Now we have to enter the time into the truck List

    
    
