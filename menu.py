# Syed Khurshid, SID:010081191

# User menu is what is seen when the user runs the system -> O(N^2)
def userMenu(status, myHash, truck1, truck2, truck3, dataTest, T1, T2, T3):
    # This is run when the display message is seen in the terminal
    # The interface is accessible via terminal
    miles = T1['distance'] + T2['distance'] + T3['distance']
    print('Western Governors Universtiy Parcel Services Planning Tool')
    print('================================================================')
    print('Efficient route and delivery distribution software \n')

    # The distances are determined and then printed out to the user
    print('Total distance truck 1 travelled is ' +
          str(T1['distance']) + " miles")
    print('Total distance truck 2 travelled is ' +
          str(T2['distance']) + " miles")
    print('Total distance truck 3 travelled is ' +
          str(T3['distance']) + " miles")
    print('Total distance travelled is ' +
          str(T1['distance'] + T2['distance'] + T3['distance']) + " miles \n")

    print("Please select the following options by selecting either 1-8")
    print("Anytime you'd like to exit or quit, please type in either 'q' or 'quit' or 'exit'")
    print(
        "1 - Get the status of all package[s] within a designated time range")
    print("2 - Get a single package information at a specified time range")
    print(
        "3 - Get all the package[s] by address within a specified time range")
    print("4 - Get all the package[s] by city within a specified time range")
    print(
        "5 - Get all the package[s] by Zipcode within a specified time range")
    print("6 - Get all the package[s] by weight within a specified time range")
    print(
        "7 - Get all the package[s] by delivery status within a specified time range")
    print("8 - Get all the package[s] by delivery deadline")

    # User selects the options from the list of above options
    selection = input(
        " Please select the options above by entering a number from 1-8: \n")
    # O(N^2)
    match selection:
        case "1":
            # O(N^2)
            status.get_all_status(myHash, truck1, truck2, truck3, dataTest)
        case "2":
            # O(N^2)
            status.get_ind_package_status(
                myHash, truck1, truck2, truck3, dataTest)
        case "3":
            status.get_by_address(myHash, truck1, truck2, truck3, dataTest)
        case "4":
            status.get_by_city(myHash, truck1, truck2, truck3, dataTest)
        case "5":
            status.get_by_zipcode(myHash, truck1, truck2, truck3, dataTest)
        case "6":
            status.get_by_pack_weight(myHash, truck1, truck2, truck3, dataTest)
        case "7":
            status.get_by_delivery_status(
                myHash, truck1, truck2, truck3, dataTest)
        case "8":
            status.get_by_del_deadline(
                myHash, truck1, truck2, truck3, dataTest)
        case "Quit":
            # O(1)
            exit()
        case "q":
            # O(1)
            exit()
        case "quit":
            # O(1)
            exit()
