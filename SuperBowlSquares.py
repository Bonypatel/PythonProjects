import math
import random
import csv

if __name__ == "__main__":
    chiefs = [0,1,2,3,4,5,6,7,8,9]
    niners = [0,1,2,3,4,5,6,7,8,9]

    random.shuffle(chiefs)
    random.shuffle(niners)
    print(chiefs)
    print(niners)

    numbers = list(range(100)) # update
    random.shuffle(numbers)
    print(len(numbers))

    names_list = []
    bought_2 = ["Laith Abwini", "Dylan Altland", "Emily Helm", "Luke Wiley", "Tom Kaukonen", "Dr. Sholy"]
    bought_3 = ["Frank Garcia", "Chris McDonough", "Michael Sakele"]
    bought_4 = ["Mike Nezgoda", "Dan Donohoe"]
    bought_5 = ["Bony Patel", "Casper Tortella", "Dan Baran", "Gavin Hawkes", "Ken Thompson", "Justin McGinnis", "Jim Moody"]
    bought_6 = ["Kevin Subramanian"]
    bought_10 = ["Chris Sholy", "Justin Kuo", "Brandon Cook"]
    for i in range(2):
        names_list.extend(bought_2)
    for i in range(3):
        names_list.extend(bought_3)
    for i in range(4):
        names_list.extend(bought_4)
    for i in range(5):
        names_list.extend(bought_5)
    for i in range(6):
        names_list.extend(bought_6)
    for i in range(10):
        names_list.extend(bought_10)
    
    print(len(names_list))

    result = {}
    for number in numbers:
        for name in names_list:
            result[number] = name
            names_list.remove(name) 
            break

    print("final dictionary : " + str(result))

    csv_columns = ['Box Number', 'Name']
    csv_file = "test.csv"

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            
            for key, value in result.items():
                writer.writerow([key, value])
    except IOError:
        print("I/O Error")