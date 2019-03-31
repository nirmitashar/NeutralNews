import shutil
import os
import csv
ting = [["speech","party"]]
directory_in_str = "./training_set/"
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    f = open(directory_in_str+filename, "r")
    big_jack = f.read()
    print(big_jack)
    big_jack = big_jack.replace("\n","")
    if 'D' in filename:
        ting.append([big_jack,1])
    elif 'R' in filename:
        ting.append([big_jack,0])
    else:
        print("What the dog??")


print(ting)

with open('bigdat.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(ting)
