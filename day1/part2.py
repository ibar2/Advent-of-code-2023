import re
from part1 import main


ahashmaphh = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
              'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9, }


def mapper(match):
    return str(ahashmaphh[match.group(0)])


def datafy(filename):
    newerarray = []
    pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            data = re.sub(pattern, mapper, line)
            newerarray.append(data)
    return newerarray


filename = 'inputdatapart2.txt'
reformedData = datafy(filename)
total = 0
# pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
# data = re.sub(pattern, mapper, 'plckgsixeight6eight95bnrfonetwonej')
# print(main(data))
print(len(reformedData))
for i in reformedData:
    total += main(i)
print(total)
