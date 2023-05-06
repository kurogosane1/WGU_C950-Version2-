# # Syed Khurshid, SID:010081191

from menu import userMenu
from distance import get_shortest_path, set_values, get_time_travelled, get_current_distance, get_package_address,get_time_travelled2
from Data_Sorting import DataSort
import datetime


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
# print(T['distance'], T['path'])
# T1 = get_shortest_path(temp1)
for i in range(0, len(truck1)):
    truck1[i][8] = "09:00:00"
travel = 0
tempTime = ["09:00:00"]
for index in range(0, len(T['path'])):
    try:
        distance = get_current_distance(int(T['path'][index]), int(T['path'][index+1]))
        travel = distance

        print(T['path'][index])
        print(f'when index is {index} and travelled {travel}')
        time_travelled = get_time_travelled2(travel,tempTime)
        print(time_travelled)
        print(tempTime)
        # time_travelled2 = get_time_travelled2(travel, tempTime)
        print(f'when index is time travelled is {time_travelled}')
        

    except IndexError:
        pass
    
# for index in range(0, len(T['path'])):
#     try:
#         distance = get_current_distance(
#             int(T['path'][index]), int(T['path'][index+1]))
#         # print(get_time_travelled(distance, int(T['path'][index])))
#         truck_time = get_time_travelled(travel+distance),
#         # print(f'This is truck_time {truck_time}')
#         getaddress = get_package_address(T['path'][index+1]),
#         # print(f'The index is {getaddress[0]}')
#         for i in range(0, len(truck1)):
#             if truck1[i][1] == getaddress[0]:
#                 print('It reached here')
#                 start_min = truck1[i][8]
#                 (hrs, min, secs) = start_min.split(":")
#                 convertStart = datetime.timedelta(
#                     hours=int(hrs), minutes=int(min), seconds=int(secs))
#                 # (hrs, min, secs) = truck_time.split(":")
#                 # convertTime = datetime.timedelta(
#                 #     hours=int(hrs), minutes=int(min), seconds=int(secs))

#                 total = convertStart + truck_time[0]
#                 # print(f'this is the {total}')
#                 truck1[i][5] = str(total)

#         # (hrs,mins,secs) = time_min.split(':')
#         # convertedTime = datetime.timedelta(hours=int(hrs),minutes=int(mins),secs=int(secs))
#         ################################
#         # This is to check if the time is added or not

#         (f'distance is found to be {distance} for {index} in truck1_short_path')
#     except IndexError:
#         pass
# print(truck1)
# for i in range(0, len(truck1)):
#             print(distance)
# truck1[i][8]="09:00:00"
# time_min = get_time_travelled(distance, int(T['path'][i]))
# start_min = truck1[i][8]
# (hrs,mins,secs) = start_min.split(':')
# convertStart = datetime.timedelta(hours=int(hrs),minutes=int(mins),seconds=int(secs))
# total  = convertStart+ time_min
# print(total)

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
