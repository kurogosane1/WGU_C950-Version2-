# # Syed Khurshid, SID:010081191

import datetime
from distance import get_shortest_path, set_values, get_current_distance, get_package_address, get_time_travelled
from hashingData import HashingData
# from Data_Sorting import DataSort,replace_in_truck


# This is where the package status[s] will be used to find and identify where they stand
class Status():
    def __init__(self):
        pass

    def set_time(self, shortestPath_truck, truck_list, truck_number, myHash):
        start_time = ""
        if truck_number == 1:
            start_time = "08:00:00"
        elif truck_number == 2:
            start_time = "09:10:00"
        else:
            start_time = "11:00:00"
        travelled_distance = 0
        # Based on the truck_number we arrange the start time
        for i in range(0, len(truck_list)):
            truck_list[i][8] = start_time
        tempTime = [start_time]
        # Setting the path
        for index in range(0, len(shortestPath_truck)):
            try:
                distance = get_current_distance(
                    int(shortestPath_truck[index]), int(shortestPath_truck[index+1]))
                travelled_distance = distance
                time_travelled = get_time_travelled(
                    travelled_distance, tempTime)
                if truck_list[index+1] == "0":
                    pass
                # This is to set the path to the truck lists
                address = get_package_address(shortestPath_truck[index])
                if address == "0":
                    pass
                for i in range(len(truck_list)):
                    if truck_list[i][1] == address:
                        truck_list[i][5] = time_travelled
                        input = [truck_list[i][0], truck_list[i][1], truck_list[i][2], truck_list[i][3], truck_list[i][4], truck_list[i]
                                 [5], truck_list[i][6], truck_list[i][7], truck_list[i][8], truck_list[i][9], truck_list[i][10], str(truck_number)]
                        myHash.update(truck_list[i][0], input)
            except IndexError:
                pass

    # This is to determine the status of the package at a particular time
    def get_all_status(self, myHash, truck1, truck2, truck3, dataTest):
        # User input is broken down for the datetime library
        # converting in a date time format
        fix = myHash.search("13")
        fix[11]=1
        myHash.update("13",fix)
        fix = myHash.search("9")
        fix[11]=2
        myHash.update("9",fix)
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all packages till that time\n and enter as (HH:MM:SS): ')

        if user_time != "Quit" or user_time != "q" or user_time != "exit":
            (hrs, min, sec) = user_time.split(':')
            con_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(sec))

            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            (hrs, min, sec) = check_time.split(":")
            con_check_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(sec))
            # print(f'this is truck truck 2 before update {truck2}')
            if con_user_time >= con_check_time:
                # Package 9 address needs to be found and update
                result = myHash.search("9")
                result[1] = "410 S State St"
                result[2] = "Salt Lake City"
                result[3] = "UT"
                result[4] = "84111"
                # result[11] = "2"
                myHash.update("9", result)
                if result in truck1:
                    print("Found in Truck 1")
                elif result in truck2:
                    dataTest.replace_in_truck("9", truck2, result, 2)
                    # print(f'This is after truck 2 is updated {truck2}')
                    temp2 = set_values(truck2)
                    temp2.insert(0, "0")
                    T2 = get_shortest_path(temp2)
                    self.set_time(T2['path'], truck2, 2, myHash)
                else:
                    print("Found in Truck 3")
            # Counting for all the packages
            for count in range(1, 41):
                package = myHash.search(str(count))
                # print(myHash.search(str(13)))

                try:
                    starting_time = myHash.search(str(count))[8]
                    delivery_time = myHash.search(str(count))[5]
                    (h, m, s) = starting_time.split(':')
                    conv_starting_time = datetime.timedelta(
                        hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = delivery_time.split(':')
                    conv_del_time = datetime.timedelta(
                        hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass

                if conv_starting_time > con_user_time:
                    package[10] = "At Hub"
                    print(
                        f'Package ID: {package[0]}, "Delivering at {package[1]}, {package[2]}, {package[3]}, {package[4]}". Departs on Truck {package[11]} at {package[8]}, Current status {package[10]}')

                elif conv_starting_time < con_user_time:
                    if con_user_time < conv_del_time:
                        # package = myHash.search(str(count))
                        package[10] = "In transit"
                        print(
                            f'Package ID: {package[0]}, "Delivering at {package[1]}, {package[2]}, {package[3]}, {package[4]}". Departed on Truck {package[11]} at {package[8]}, weight of the package is {package[6]}, Current status {package[10]} ')

                    else:
                        # package = myHash.search(str(count))
                        package[10] = "Delivered"
                        print(
                            f'Package ID: {package[0]}, "Delivered at {package[1]}, {package[2]}, {package[3]}, {package[4]}". Departed on Truck {package[11]} at {package[8]}, weight of the package is {package[6]}. Current status {package[10]} at {package[5]}')

    # This is to get the individual package status

    def get_ind_package_status(self, myhash, truck1, truck2, truck3, dataTest):
        #User input is broken down for the datetime library
        #converting in a date time format
        fix = myhash.search("13")
        fix[11]=1
        myhash.update("13",fix)
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all packages till that time\n and enter as (HH:MM:SS): ')
        package_id = input("Enter valid package ID Number ")

        if user_time != "Quit" or user_time != "q" or user_time != "exit":
            (hrs, min, sec) = user_time.split(':')
            con_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(sec))
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            (hrs, min, sec) = check_time.split(":")
            con_check_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(sec))
            if con_user_time >= con_check_time:
                # Package 9 address needs to be found and update
                result = myhash.search("9")
                # print(f"This is the search result {result}")
                result[1] = "410 S State St"
                result[2] = "Salt Lake City"
                result[3] = "UT"
                result[4] = "84111"
                # result[11] = "2"
                myhash.update("9", result)
                if result in truck1:
                    print("Found in Truck 1")
                elif result in truck2:
                    dataTest.replace_in_truck("9", truck2, result, 2)
                    # print(truck2)
                    temp2 = set_values(truck2)
                    temp2.insert(0, "0")
                    T2 = get_shortest_path(temp2)
                    self.set_time(T2['path'], truck2, 2, myhash)
                else:
                    print("Found in Truck 3")
            packageInfo = myhash.search(package_id)
            if packageInfo != None:
                try:
                    starting_time = packageInfo[8]
                    delivery_time = packageInfo[5]
                    (h, m, s) = starting_time.split(':')
                    conv_starting_time = datetime.timedelta(
                        hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = delivery_time.split(':')
                    conv_del_time = datetime.timedelta(
                        hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass
                if conv_starting_time > con_user_time:

                    packageInfo[10] = "At Hub"
                    print(
                        f'Package ID: {packageInfo[0]}, "Delivering at {packageInfo[1]}, {packageInfo[2]}, {packageInfo[3]}, {packageInfo[4]}". Departs on Truck {packageInfo[11]} at {packageInfo[8]}. Current Status is {packageInfo[10]}')

                elif conv_starting_time < con_user_time:
                    if con_user_time < conv_del_time:

                        packageInfo[10] = "In transit"
                        print(
                            f'Package ID: {packageInfo[0]}, "Delivering at {packageInfo[1]}, {packageInfo[2]}, {packageInfo[3]}, {packageInfo[4]}". Departed on Truck {packageInfo[11]} at {packageInfo[8]}, weight of the package is {packageInfo[6]}. Current Status is {packageInfo[10]} ')

                    else:

                        packageInfo[10] = "Delivered"
                        print(
                            f'Package ID: {packageInfo[0]}, "Delivered at {packageInfo[1]}, {packageInfo[2]}, {packageInfo[3]}, {packageInfo[4]}". Departed on Truck {packageInfo[11]} at {packageInfo[8]}, weight of the package is {packageInfo[6]}. Current Status is {packageInfo[10]} ')
            else:
                print("Invalid Package ID entered")
                exit()
  