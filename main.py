# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import get_shortest_path, set_values
from Data_Sorting import DataSort
from status import Status

# The class in initialized -> O(N)
dataTest = DataSort()
# The trucks are sorted with the packages -> O(N)
dataTest.sort_to_trucks()
# Status class is initialized -> O(N)
status = Status()
# Truck 1, 2, and 3 was then called and saved here -> O(N)
truck1 = dataTest.get_first_truck()
truck2 = dataTest.get_second_truck()
truck3 = dataTest.get_third_truck()
print(f'This is truck 2 {truck2}')
# Temp 1,2 and 3 are the Index for each package index is identified and saved temporaily -> O(N)
temp1 = set_values(truck1)
temp2 = set_values(truck2)
temp3 = set_values(truck3)
# A starting point of 0 is inserted into the list
temp1.insert(0, "0")
temp2.insert(0, "0")
temp3.insert(0, "0")
# Getting the all the package list with the hash function -> O(1)
myHash = dataTest.get_All_Pacakges()
# Determining the shortest path in temporily in T1, T2, T3 -> O(N^4)
T1 = get_shortest_path(temp1)
T2 = get_shortest_path(temp2)
T3 = get_shortest_path(temp3)

# The delivery time is then calculated and then saved into truck and hash list -> (O^2)
status.set_time(T1['path'], truck1, 1, myHash)
status.set_time(T2['path'], truck2, 2, myHash)
status.set_time(T3['path'], truck3, 3, myHash)


# The user menue with options is run and represented here O(N^2)
userMenu(status, myHash, truck1, truck2, truck3, dataTest, T1,T2,T3)
