# # Syed Khurshid, SID:010081191

# This is where the distance is then calculated and the trucks and package status is found

import csv
import datetime
from Data_Sorting import DataSort

# First we need to place the Trucks travelling
datasort = DataSort()
# We get the trucks that were sorted out and used here
truck1 = datasort.get_first_truck()
truck2 = datasort.get_second_truck()
truck3 = datasort.get_third_truck()

# This is to get the address location of the points
# Starting truck index of address
first_truck_index = []
second_truck_index = []
third_truck_index = []

# All trucks start from from the Hub which has an index of 0
first_truck_index.append("0"),
second_truck_index.append("0")
third_truck_index.append("0")

def get_address():
        with open('./data/addressData.csv') as addCSV:
            address_CSV = csv.reader(addCSV, delimiter=',')
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

def get_current_distance(row, col):
        # getting the distance from the column and row from the distance data
        # This is to get the distance point
        with open('./data/distance.csv') as distCSV:
            distance_CSV = list(csv.reader(distCSV, delimiter=','))
            distance = distance_CSV[row][col]
            if distance == '':
                distance = distance_CSV[col][row]
        return float(distance)

# This is to calculate the time to travelled by each truck
# Then accordingly the truck delivery time will be calculated 
def get_time_travelled(distance, arrayList):
    # Speed that the truck could travel
    time = distance/ 18   
    # This converts the time into a string format at arrival time 
    time_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(time * 60, 60))
    arrival_time = time_in_minutes + ':00'
    arrayList.append(arrival_time)
    # Now we append to the list as this is the delivery time that will 
    # will calculate the total time travelled from starting point
    total = datetime.timedelta()
    for i in arrayList:
         (h,m,s) = i.split(':')
         d = datetime.timedelta(hours=int(h),minutes=int(m), seconds=int(s))
         total += d
    return str(total)     


def printing_distance(arrayList):
        total = 0
        for i in range(0, len(arrayList)):
            if i+1 < len(arrayList):
                distance = get_current_distance(
                    int(arrayList[i]), int(arrayList[i+1]))
                total += distance
            else:
                distance = get_current_distance(
                    int(arrayList[i]), int(arrayList[0]))
                total += distance

        # print('Final total is total is {:.2f}'.format(total))
        return total
# Getting the shortest points for the array list of trucks to follow
def get_shortest_point(row, arrayList):
        temp = 0.0
        shortest_distance = 0.0
        index = 0
        for i in range(0, len(arrayList)):
            distance = get_current_distance(row, int(arrayList[i]))
            if temp == 0.0:
                temp = distance
            else:
                if distance < temp:
                    temp = distance
                    index = i
            shortest_distance = temp
        return index

# This is to get the address of the location where the package is going 
def get_package_address(serial):
    with open('./data/addressData.csv') as addCSV:
        address_CSV = list(csv.reader(addCSV, delimiter=','))
        for i in range(0,len(address_CSV)):
             if serial == address_CSV[i][0]:
                  return address_CSV[i][2]
             
# Steps to get the nearest neighbor right
# First we need to start to check if the distance to any of the items in the list are closer from the starting point
# We do that by placing the starting point in a seperate list
# if the distance is closer for the line items in the list, then we place that point into the starting point list
def get_shortest_path(arrayList):
        # A starting array list to determine the shortest path. Since '0' is considered the HUB
        # Here all the shortest routes are determined and stored here
        startingPoint = ['0']
        # Since this is the starting point and this will change as we determine the shortest route from here on. 
        # Its replaced as the shortest next point is determined 
        arrayList.remove('0')
        arrayList.sort()
        currentPoint = '0'
        while len(arrayList) > 0:
            for i in range(0, len(arrayList)):
                # we first get the shortest distance from the first point
                check_value = get_shortest_point(int(currentPoint), arrayList)
                # After we identify the shortest distance from the first point, we append it to the starting Point Array
                startingPoint.append(arrayList[check_value])
                # We remove the visited location from the array list and declare it as the Current Point
                currentPoint = arrayList[check_value]
                arrayList.pop(check_value)
        startingPoint.append('0')
        num = printing_distance(startingPoint)
        d=dict()
        d['distance'] = round(num, 2)
        d['path'] = startingPoint
        return d