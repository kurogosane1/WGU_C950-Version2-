# Syed Khurshid, SID:010081191

import datetime

def userMenu():
    # This is run when the display message is seen in the terminal
    # The interface is accessible via terminal 
    miles =''
    print('Western Governors Universtiy Parcel Services Planning Tool')
    print('================================================================')
    print('Efficient route and delivery distribution software')
    print(f'Total distance covered is {miles} miles. \n')

    print("Please select the following options by selecting either 1-5")
    print("Anytime you'd like to exit or quit, please type in either 'q' or 'quit' or 'exit'")
    print("1 - Get the status of all package[s] within a designated time range")
    print("2 - Get a single package information")
    print("3 - Get a package[s] by address")
    print("4 - Get package[s] info by City")
    print("5 - Get package[s] by zipcode")
    print("6 - Get package[s] by package weight")
    print("7 - Get by Deadline")

    # User selects the options from the list of above options
    selection = input(" Plesae select the options above by entering a number from 1-7: ")


    match selection:
        case "1":
            print("Test") 
