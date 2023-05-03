# # Syed Khurshid, SID:010081191

# This is where the distance is then calculated and the trucks and package status is found

import csv
from Data_Sorting import DataSort

# First we need to place the Trucks travelling
datasort = DataSort()
# We get the trucks that were sorted out and used here
truck1 = datasort.get_first_truck()
truck2 = datasort.get_second_truck()
truck3 = datasort.get_third_truck()

# Function to find the distance for each point
# def test1():
#     with open('./data/addressData.csv') as addCSV:
#             addressCSV = csv.reader(addCSV, delimiter=',')
#             for data in addressCSV:
#                 print(data)

# This is to get the address location of the points
with open('./data/addressData.csv') as addCSV:
    address_CSV = csv.reader(addCSV, delimiter=',')

    # Starting truck index of address
    first_truck = []
    second_truck = []
    third_truck = []
    first_truck_index = []
    second_truck_index = []
    third_truck_index = []

    # All trucks start from from the Hub which has an index of 0
    first_truck_index.append("0"),
    second_truck_index.append("0")
    third_truck_index.append("0")

    def get_address():
        return address_CSV

    def set_values(arrayList):
        # Temporary Array List
        tempArrayList = []
        # We get the index of where we are going first
        for data in arrayList:
            # starting point of all trucks is at the Hub
            index = get_index(data[1])
            if index != None:
                tempArrayList.append(index)
        return tempArrayList

    def get_index(address):
        with open('./data/addressData.csv') as addCSV:
            address_CSV = csv.reader(addCSV, delimiter=',')
            for add in address_CSV:
                if add[2] == address:
                    return add[0]

    def get_distance(row, col):
        # getting the distance from the column and row from the distance data
        # This is to get the distance point
        with open('./data/distance.csv') as distCSV:
            distance_CSV = list(csv.reader(distCSV, delimiter=','))
            # print(distance_CSV[row][col])
            distance = distance_CSV[row][col]
            if distance == '':
                distance = distance_CSV[col][row]
        return float(distance)

    def printing_distance(arrayList):
        total = 0
        for i in range(0, len(arrayList)):
            if i+1 < len(arrayList):
                distance = get_distance(int(arrayList[i]), int(arrayList[i+1]))
                # print(
                #     f'distance total is now at {total} and distance is {distance} when from {arrayList[i]} to {arrayList[i+1]}')
                total += distance
            else:
                distance = get_distance(int(arrayList[i]), int(arrayList[0]))
                total += distance

        print('Final total is total is {:.2f}'.format(total))
        return total

    def get_distance2(row, arrayList):
        temp = 0.0
        shortest_distance = 0.0
        index = 0

        # print(f'This is to get the row {arrayList[row]} and row is {row}' )
        for i in range(0, len(arrayList)):
            distance = get_distance(row, int(arrayList[i]))
            if temp == 0.0 :
                temp = distance
            else:
                if distance < temp:
                    temp = distance
                    index = i

            shortest_distance = temp
        print(f'shortest distance is {shortest_distance} from {row} to point {index}')
        return index

# Steps to get the nearest neighbor right
# First we need to start to check if the distance to any of the items in the list are closer from the starting point
# We do that by placing the starting point in a seperate list
# if the distance is closer for the line items in the list, then we place that point into the starting point list
    def get_starting_point(arrayList):
        startingPoint = ['0']
        starting_distance = 50.0
        total = 0.0
        lowest_point = ''
        currentPoint = '0'
        placesNotVisited = sorted(arrayList)
        print(f'This is the array list {arrayList} and this is the sorted arrayList {placesNotVisited}')
        # arrayList.remove('0')
        while len(arrayList) > 0:
            for i in range(0, len(arrayList)):
                # we first get the shortest distance from the first point
                print(i)
                check_value = get_distance2(int(currentPoint), arrayList)
                # After we identify the shortest distance from the first point, we append it to the starting Point Array
                startingPoint.append(arrayList[check_value])
                # We remove the visited location from the array list and declare it as the Current Point
                currentPoint = arrayList[check_value]
                arrayList.pop(check_value)
        # startingPoint.append('0')
        print(startingPoint)
        num = printing_distance(startingPoint)
        # print(len(startingPoint))
        #  print(len(arrayList))
        return round(num,2)
