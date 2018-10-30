#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt


import csv

def top_10(file, num, constraint):
    '''First parameter is the file, second parameter is
    location of the list element of importance,
    third parameter is the location of STATUS of the application.
    '''
    dct = {}
    list = []
    count = 0
    for row in file:
        if row[constraint] == 'CERTIFIED':
            count = count + 1
            if row[num] not in dct:
                dct[row[num]] = 1
            else:  
                dct[row[num]] = dct[row[num]] + 1
    n = min(len(dct), 10)
    for tup in sorted(dct.items(), key=lambda x: (-x[1], x[0]))[:n]:
        list.append((tup[0], tup[1], str(round(tup[1]*100.0/count,1))+'%'))
    return list

        


employer_state_dict = [\
('TOP_STATES', \
'NUMBER_CERTIFIED_APPLICATIONS', \
'PERCENTAGE'),\
]
occupation = [\
('TOP_OCCUPATIONS', \
'NUMBER_CERTIFIED_APPLICATIONS', \
'PERCENTAGE'),\
]

loc = './input/h1b_input.csv'
with open(loc,'rt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    captions = next(csv_reader)
    for caps in captions:
        if 'STATUS' in caps:
            status_num =  captions.index(caps)
        if 'EMPLOYER_STATE' in caps:
            emp_state_num = captions.index(caps)
        if 'SOC_NAME' in caps:
            occupation_num = captions.index(caps)
    employer_state_dict.extend(top_10(csv.reader(csv_file, delimiter=';'), emp_state_num, status_num))
f = open("./output/top_10_states.txt","w")
for t in employer_state_dict:
    line = ';'.join(str(x) for x in t)
    f.write(line + '\n')
f.close()
with open(loc,'rt') as csv_file:
    occupation.extend(top_10(csv.reader(csv_file, delimiter=';'), occupation_num, status_num))
f = open("./output/top_10_occupations.txt","w")
for t in occupation:
    line = ';'.join(str(x) for x in t)
    f.write(line + '\n')
f.close()
