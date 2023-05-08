# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import get_shortest_path, set_values
from Data_Sorting import DataSort
import datetime
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
status.set_time(T1['path'], truck1,1,myHash)
status.set_time(T2['path'], truck2,2,myHash)
status.set_time(T3['path'], truck3,3,myHash)


userMenu(status, myHash)

