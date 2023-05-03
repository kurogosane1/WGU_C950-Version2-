# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import set_values, printing_distance,get_starting_point
from Data_Sorting import DataSort


dataTest = DataSort()
dataTest.sort_to_trucks()
# test1()
truck1 = dataTest.get_first_truck()
truck2 = dataTest.get_second_truck()
truck3 = dataTest.get_third_truck()
temp1 = set_values(truck1)
temp2 = set_values(truck2)
temp3 = set_values(truck3)
temp1.insert(0,"0")
temp2.insert(0,"0")
temp3.insert(0,"0")
truck1_distance = get_starting_point(temp1)
truck2_distance = get_starting_point(temp2)
truck3_distance = get_starting_point(temp3)
print(f'Total distance truck1 traveled is {truck1_distance}')
print(f'Total distance truck2 traveled is {truck2_distance}')
print(f'Total distance truck3 traveled is {truck3_distance}')
print(f'Total distance all trucks travelled is {truck1_distance + truck2_distance + truck3_distance}')
userMenu()
