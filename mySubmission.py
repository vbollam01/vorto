import math
import sys

def cal_euclid_dist(p1, p2):
    distance = 0.0
    for i in range(0, len(p1)):
        distance += (p1[i] - p2[i]) ** 2
    return math.sqrt(distance)


def cal_distance(loads, pickUp, dropOff):
    fixed_depo = [0, 0]
    load_array_dic = {}
    for i in range(0, len(loads)):
        cal_load_dist =  cal_euclid_dist(fixed_depo, pickUp[i]) + cal_euclid_dist(pickUp[i], dropOff[i]) + cal_euclid_dist(dropOff[i], fixed_depo)
        load_array_dic[loads[i]] = cal_load_dist
    load_array_dic = sorted(load_array_dic.items(), key=lambda x:x[1])
    return load_array_dic

def cal_noOfDrivers(distanceMap):
    maxAllowedDsitance = 12 * 60
    noOfDrivers = []
    c = 1
    loadAppendArray = []
    i=0
    while i<len(distanceMap):
        if (maxAllowedDsitance - distanceMap[i][1]) > 0 :
            maxAllowedDsitance = maxAllowedDsitance - distanceMap[i][1]
            loadAppendArray.append(distanceMap[i][0])
        else :
            print(loadAppendArray)
            noOfDrivers.append(c)
            c=c+1
            loadAppendArray = []
            if(maxAllowedDsitance > 0):
                 if(distanceMap[-1][0] == distanceMap[i][0]):
                    noOfDrivers.append(c)
                    print([distanceMap[i][0]])
                 else:
                     i=i-1
            maxAllowedDsitance = 12 * 60
        i=i+1
            
    return noOfDrivers

def process_text_file(file_path):
    loads = []
    pickup = []
    dropOff = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.readlines()
               # Remove the first line
            content = content[1:]
            for line in content:
                input = line.strip().split()
                loads.append(int(input[0]))
                pickup.append([int(float(x)) for x in input[1].strip('()').split(',')])
                dropOff.append([int(float(x)) for x in input[2].strip('()').split(',')])
            # print(loads, dropOff, pickup)
            distanceMap = cal_distance(loads, pickup, dropOff)
            print(distanceMap)
            cal_noOfDrivers(distanceMap)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# Example usage:
if __name__ == "__main__":
    # Check if the user provided a command-line argument (file path)
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit(1)

file_path = sys.argv[1]  # Get the file path from command-line arguments
process_text_file(file_path)
