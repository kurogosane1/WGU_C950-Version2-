# # Syed Khurshid, SID:010081191

import datetime
from distance import get_shortest_path, set_values, get_current_distance, get_package_address, get_time_travelled
# from hashingData import HashingData
# from Data_Sorting import DataSort,replace_in_truck


# This is where the package status[s] will be used to find and identify where they stand -> O(N^2)
class Status():
    # Constructor
    def __init__(self):
        pass

    # This converts to time
    # O(1)
    def convert_time(self, input):
        if input != 'EOD':
            (hrs, min, secs) = input.split(":")
            converted_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(secs))
            return converted_time
        else:
            return "EOD"

    # This is to fix the incorrect address mistakes
    # O(1)
    def fix_address(self, myHash, truck1, truck2, truck3, dataTest):
        result = myHash.search("9")
        result[1] = "410 S State St"
        result[2] = "Salt Lake City"
        result[3] = "UT"
        result[4] = "84111"
        myHash.update("9", result)
        if result in truck1:
            print("Found in Truck 1")
        elif result in truck2:
            dataTest.replace_in_truck("9", truck2, result, 2)
            temp2 = set_values(truck2)
            temp2.insert(0, "0")
            T2 = get_shortest_path(temp2)
            self.set_time(T2['path'], truck2, 2, myHash)
        else:
            print("Found in Truck 3")

    # This sets the delivery time of the package into the truck list and array -> O(N^2)
    def set_time(self, shortestPath_truck, truck_list, truck_number, myHash):
        start_time = ""
        # O(1)
        if truck_number == 1:
            start_time = "08:00:00"
        elif truck_number == 2:
            start_time = "09:10:00"
        else:
            start_time = "11:00:00"
        travelled_distance = 0
        # Based on the truck_number we arrange the start time
        # O(N)
        for i in range(0, len(truck_list)):
            truck_list[i][8] = start_time
        tempTime = [start_time]
        # Setting the path
        # O(N)
        for index in range(0, len(shortestPath_truck)):
            try:
                # O(1)
                distance = get_current_distance(
                    int(shortestPath_truck[index]), int(shortestPath_truck[index+1]))
                travelled_distance = distance
                # O(N)
                time_travelled = get_time_travelled(
                    travelled_distance, tempTime)
                if truck_list[index+1] == "0":
                    pass
                # This is to set the path to the truck lists -> O(N)
                address = get_package_address(shortestPath_truck[index])
                if address == "0":
                    pass
                # O(N)
                for i in range(len(truck_list)):
                    if truck_list[i][1] == address:
                        truck_list[i][5] = time_travelled
                        input = [truck_list[i][0], truck_list[i][1], truck_list[i][2], truck_list[i][3], truck_list[i][4], truck_list[i]
                                 [5], truck_list[i][6], truck_list[i][7], truck_list[i][8], truck_list[i][9], truck_list[i][10], str(truck_number), truck_list[i][12]]
                        myHash.update(truck_list[i][0], input)
            except IndexError:
                pass

    # This is to determine the status of the package at a particular time -> O(N^2)
    def get_all_status(self, myHash, truck1, truck2, truck3, dataTest):
        # User input is broken down for the datetime library
        # converting in a date time format
        fix = myHash.search("13")
        fix[11] = 1
        # O(N)
        myHash.update("13", fix)
        fix = myHash.search("9")
        fix[11] = 2
        # O(N)
        myHash.update("9", fix)
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all packages till that time\n and enter as (HH:MM:SS): ')
        if user_time != "Quit" or user_time != "q" or user_time != "exit":
            con_user_time = self.convert_time(user_time)

            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                # Package 9 address needs to be found and update
                self.fix_address(myHash, truck1, truck2, truck3, dataTest)
            # Counting for all the packages
            # O(N^2)
            for count in range(1, 41):
                # O(N)
                package = myHash.search(str(count))
                try:
                    # O(N)
                    starting_time = myHash.search(str(count))[8]
                    # O(N)
                    delivery_time = myHash.search(str(count))[5]
                    conv_starting_time = self.convert_time(starting_time)
                    (h, m, s) = delivery_time.split(':')
                    conv_del_time = datetime.timedelta(
                        hours=int(h), minutes=int(m), seconds=int(s))
                    if conv_starting_time > con_user_time:
                        package[10] = "At Hub"
                        print(
                            f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')

                    elif conv_starting_time < con_user_time:
                        if con_user_time < conv_del_time:
                            package[10] = "In transit"
                            print(
                                f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')

                        else:
                            package[10] = "Delivered"
                            print(
                                f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                except ValueError:
                    pass
                except IndexError:
                    print("Invalid Time Range Provided")
                    exit()
                except TypeError:
                    print("Invalid Time Range Provided")
                    exit()

    # This is to get the individual package status
    # O(N^2)

    def get_ind_package_status(self, myhash, truck1, truck2, truck3, dataTest):
        # User input is broken down for the datetime library
        # converting in a date time format
        fix = myhash.search("13")
        fix[11] = 1
        myhash.update("13", fix)
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all packages till that time\n and enter as (HH:MM:SS): ')
        package_id = input("Enter valid package ID Number ")

        if user_time != "Quit" or user_time != "q" or user_time != "exit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                # Package 9 address needs to be found and update
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            # if packageInfo != None:
            try:
                packageInfo = myhash.search(package_id)
                starting_time = packageInfo[8]
                delivery_time = packageInfo[5]
                conv_starting_time = self.convert_time(starting_time)
                conv_del_time = self.convert_time(delivery_time)
                if conv_starting_time > con_user_time:
                    packageInfo[10] = "At Hub"
                    print(
                        f'Package ID: {packageInfo[0]}, "Address: {packageInfo[1]} City: {packageInfo[2]} State: {packageInfo[3]} ZipCode: {packageInfo[4]}" | Truck {packageInfo[11]} | Departs at {packageInfo[8]}|  Current status {packageInfo[10]} | Deadline expected {packageInfo[12]}')

                elif conv_starting_time < con_user_time:
                    if con_user_time < conv_del_time:
                        packageInfo[10] = "In transit"
                        print(
                            f'Package ID: {packageInfo[0]} | "Delivering at Address: {packageInfo[1]}, {packageInfo[2]} City: {packageInfo[3]} ZipCode {packageInfo[4]}" | Truck {packageInfo[11]} | Departed at {packageInfo[8]}| Weight of the package: {packageInfo[6]} | Current status {packageInfo[10]}| Delivery Deadline: {packageInfo[12]} ')
                    else:
                        packageInfo[10] = "Delivered"
                        print(
                            f'Package ID: {packageInfo[0]}| "Delivered at Address: {packageInfo[1]} City: {packageInfo[2]} State: {packageInfo[3]} ZipCode: {packageInfo[4]}". | Truck {packageInfo[11]} | Departed at {packageInfo[8]}| Weight of the package: {packageInfo[6]}| Current status:  {packageInfo[10]} at {packageInfo[5]}|  Delivery Deadline {packageInfo[12]}')
            except ValueError:
                pass
            except IndexError:
                print("Invalid Package ID")
                exit()
            except TypeError:
                print("Invalid Package ID")
                exit()

    # Get by address
    # O(N^2)
    def get_by_address(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        user_address = input(
            "Please input street address for example '300 Washington st: ")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                # Package 9 address needs to be found and update
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            for count in range(1, 41):
                package = myhash.search(str(count))
                if user_address == package[1]:
                    try:
                        starting_time = myhash.search(str(count))[8]
                        deliver_time = myhash.search(str(count))[5]
                        conv_starting_time = self.convert_time(starting_time)
                        con_del_time = self.convert_time(deliver_time)
                        if conv_starting_time > con_user_time:
                            package[10] = "At Hub"
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                        elif conv_starting_time < con_user_time:
                            if con_user_time < con_del_time:
                                print("Reached here")
                                package[10] = "In transit"
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')
                            else:
                                package[10] = "Delivered"
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')

                    except ValueError:
                        pass
                    except IndexError:
                        print("Invalid address")
                        exit()
                    except TypeError:
                        print("Please enter a valid address")
                        exit()

    # Get by City
    # O(N^2)
    def get_by_city(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        user_address = input(
            "Please input the city of package for example 'Salt Lake City' :")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            for count in range(1, 41):
                package = myhash.search(str(count))
                if user_address == package[2]:
                    try:
                        starting_time = myhash.search(str(count))[8]
                        deliver_time = myhash.search(str(count))[5]
                        conv_starting_time = self.convert_time(starting_time)
                        con_del_time = self.convert_time(deliver_time)
                        if conv_starting_time > con_user_time:
                            package[10] = "At Hub"
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                        elif conv_starting_time < con_user_time:
                            if con_user_time < con_del_time:
                                package[10] = "In transit"
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')
                            else:
                                package[10] = "Delivered"
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                    except ValueError:
                        pass
                    except TypeError:
                        print("Please enter a valid")
                        exit()
                    except IndexError:
                        print("Invalid City")
                        exit()

    # Get by Zipcode
    # Get by City
    # O(N^2)
    def get_by_zipcode(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        user_address = input(
            "Please input the zipcode of the package for example '87788' :")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            # O(N^2)
            for count in range(1, 41):
                # O(N)
                package = myhash.search(str(count))
                if user_address == package[4]:
                    try:
                        starting_time = myhash.search(str(count))[8]
                        deliver_time = myhash.search(str(count))[5]
                        (hr, min, sec) = starting_time.split(":")
                        conv_starting_time = datetime.timedelta(
                            hours=int(hr), minutes=int(min), seconds=int(sec))
                        (hr, min, sec) = deliver_time.split(":")
                        con_del_time = datetime.timedelta(
                            hours=int(hr), minutes=int(min), seconds=int(sec))

                        if conv_starting_time > con_user_time:
                            package[10] = "At Hub"
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                        elif conv_starting_time < con_user_time:
                            if con_user_time < con_del_time:
                                package[10] = "In transit"
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')

                            else:
                                package[10] = "Delivered"
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                    except ValueError:
                        pass
                    except TypeError:
                        print("Please enter a valid zipcode")
                        exit()
                    except IndexError:
                        print("Invalid zipcode")
                        exit()

    # Get by status
    # Get by City
    # O(N^2)
    def get_by_pack_weight(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        user_weight = input(
            "Please input by weight of the package for example '2' :")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            # O(N^2)
            for count in range(1, 41):
                # O(N)
                package = myhash.search(str(count))
                if user_weight == package[6]:
                    try:
                        starting_time = myhash.search(str(count))[8]
                        deliver_time = myhash.search(str(count))[5]
                        conv_starting_time = self.convert_time(
                            starting_time)
                        (h, m, s) = deliver_time.split(':')
                        con_del_time = datetime.timedelta(
                            hours=int(h), minutes=int(m), seconds=int(s))
                        if conv_starting_time > con_user_time:
                            package[10] = "At Hub"
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                        elif conv_starting_time < con_user_time:
                            if con_user_time < con_del_time:
                                package[10] = "In transit"
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')
                            else:
                                package[10] = "Delivered"
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                    except ValueError:
                        pass
                    except IndexError:
                        print("Invalid weight")
                        exit()
                    except TypeError:
                        print("Invalid weight")
                        exit()

    # Get the status of the package by delivery status
    # O(N^2)

    def get_by_delivery_status(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        # This is to get the status of the package
        user_del_status = input(
            "Please input the status of the package by either entering 'at the hub' or 'en-route' or 'delivered' :")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            (hrs, min, sec) = user_time.split(':')
            con_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(min), seconds=int(sec))
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            # O(N^2)
            for count in range(1, 41):
                # O(N)
                package = myhash.search(str(count))
                try:
                    starting_time = myhash.search(str(count))[8]
                    deliver_time = myhash.search(str(count))[5]
                    (hr, min, sec) = starting_time.split(":")
                    conv_starting_time = datetime.timedelta(
                        hours=int(hr), minutes=int(min), seconds=int(sec))
                    (hr, min, sec) = deliver_time.split(":")
                    con_del_time = datetime.timedelta(
                        hours=int(hr), minutes=int(min), seconds=int(sec))
                    if conv_starting_time > con_user_time:
                        package[10] = "At Hub"
                        if user_del_status == "At Hub" or user_del_status == "at the hub":
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                    elif conv_starting_time < con_user_time:
                        if con_user_time < con_del_time:
                            package[10] = "In transit"
                            if user_del_status == "In transit" or user_del_status == "en-route":
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')

                        else:
                            package[10] = "Delivered"
                            if user_del_status == "Delivered" or user_del_status == "delivered":
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                except ValueError:
                    pass
                except IndexError:
                    print("Please enter the provided status options")
                    exit()
                except TypeError:
                    print("Please enter the provided status options")
                    exit()

    # Get the status of the package by delivery deadline
    # O(N^2)
    def get_by_del_deadline(self, myhash, truck1, truck2, truck3, dataTest):
        print(
            "If time is 'PM' then enter in 24 Hour format example 1:12pm would be 13:12:00 ")
        user_time = input(
            'Enter a time to get all package[s] till that time\n and enter as (HH:MM:SS): ')
        user_deadline = input(
            "Please input delivery deadline. Please input either 'EOD', '10:30:00' or '09:00:00 :")
        if user_time != "Quit" or user_time != "q" or user_time != "quit":
            con_user_time = self.convert_time(user_time)
            # Need to check if the package 9 address needs to be updated since the address was wrong
            check_time = "10:20:00"
            con_check_time = self.convert_time(check_time)
            if con_user_time >= con_check_time:
                self.fix_address(myhash, truck1, truck2, truck3, dataTest)
            # O(N^2)
            for count in range(1, 41):
                # O(N)
                package = myhash.search(str(count))
                user_conv = self.convert_time(user_deadline)
                pack_deadline = self.convert_time(package[12])
                if user_conv == pack_deadline:
                    try:
                        starting_time = myhash.search(str(count))[8]
                        deliver_time = myhash.search(str(count))[5]
                        conv_starting_time = self.convert_time(starting_time)
                        (hr, min, sec) = deliver_time.split(":")
                        con_del_time = datetime.timedelta(
                            hours=int(hr), minutes=int(min), seconds=int(sec))
                        if conv_starting_time > con_user_time:
                            package[10] = "At Hub"
                            print(
                                f'Package ID: {package[0]}, "Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}" | Truck {package[11]} | Departs at {package[8]}|  Current status {package[10]} | Deadline expected {package[12]}')
                        elif conv_starting_time < con_user_time:
                            if con_user_time < con_del_time:
                                package[10] = "In transit"
                                print(
                                    f'Package ID: {package[0]} | "Delivering at Address: {package[1]}, {package[2]} City: {package[3]} ZipCode {package[4]}" | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]} | Current status {package[10]}| Delivery Deadline: {package[12]} ')
                            else:
                                package[10] = "Delivered"
                                print(
                                    f'Package ID: {package[0]}| "Delivered at Address: {package[1]} City: {package[2]} State: {package[3]} ZipCode: {package[4]}". | Truck {package[11]} | Departed at {package[8]}| Weight of the package: {package[6]}| Current status:  {package[10]} at {package[5]}|  Delivery Deadline {package[12]}')
                    except ValueError:
                        pass
                    except IndexError:
                        print("Please enter a valid deadline")
                        exit()
                    except TypeError:
                        print("Please enter a valid deadline")
                        exit()
