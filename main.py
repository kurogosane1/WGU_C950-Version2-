# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import get_shortest_path, set_values
from Data_Sorting import DataSort
from status import Status


dataTest = DataSort()
dataTest.sort_to_trucks()
status = Status()
# test1()
truck1 = dataTest.get_first_truck()
truck2 = dataTest.get_second_truck()
truck3 = dataTest.get_third_truck()
temp1 = set_values(truck1)
temp2 = set_values(truck2)
temp3 = set_values(truck3)
temp1.insert(0, "0")
temp2.insert(0, "0")
temp3.insert(0, "0")

myHash = dataTest.get_All_Pacakges()

T1 = get_shortest_path(temp1)
T2 = get_shortest_path(temp2)
T3 = get_shortest_path(temp3)

print('Total distance truck 1 travelled is ' + str(T1['distance']) + " miles")
print('Total distance truck 2 travelled is ' + str(T2['distance']) + " miles")
print('Total distance truck 3 travelled is ' + str(T3['distance']) + " miles")
print('Total distance travelled is ' + str(T1['distance'] + T2['distance'] + T3['distance']) + " miles")
status.set_time(T1['path'], truck1,1,myHash)
status.set_time(T2['path'], truck2,2,myHash)
status.set_time(T3['path'], truck3,3,myHash)


userMenu(status, myHash,truck1, truck2, truck3, dataTest)

