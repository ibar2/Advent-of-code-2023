import re


ahashmaphh = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
              'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9,     '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8,  '9': 9}


def mapper(match):
    return int(ahashmaphh[match])


def main(filename):
    total = 0
    pattern = "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            data = re.findall(pattern, line)
            total += int(str(mapper(data[0])) + str(mapper(data[-1])))
    return total


filename = 'input.txt'
print(main(filename))
