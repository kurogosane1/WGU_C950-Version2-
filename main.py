# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import get_shortest_path, set_values, get_time_travelled, get_current_distance
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
temp1.insert(0, "0")
temp2.insert(0, "0")
temp3.insert(0, "0")
# print(f'This is line 23 {temp1}')

# truck1_distance, truck1_short_path = get_shortest_path(temp1)
T = get_shortest_path(temp1)
print(T['distance'], T['path'])
# T1 = get_shortest_path(temp1)
for index in range(0, len(T['path'])):
    try:
        distance = get_current_distance(
            int(T['path'][index]), int(T['path'][index+1]))
        print(get_time_travelled(distance, int(T['path'][index])))
        print(
            f'distance is found to be {distance} for {index} in truck1_short_path')
    except IndexError:
        pass

# distance, path = get_shortest_path(temp2)
# # T2 = get_shortest_path(temp2)
# truck3_distance, truck3_short_path = get_shortest_path(temp3)
# # T3 = get_shortest_path(temp3)
# print(f'Total distance truck1 traveled is {truck1_distance}')
# print(f'Total distance truck2 traveled is {truck2_distance}')
# print(f'Total distance truck3 traveled is {truck3_distance}')
# print(
#     f'Total distance all trucks travelled is {truck1_distance + truck2_distance + truck3_distance}')
userMenu()
