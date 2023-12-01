
def datafy(filename):
    arrayofdata = []
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            arrayofdata.append(line)
    return arrayofdata


def main(data: str) -> int:
    result = ''
    first = None
    last = True
    for i in data:
        if i.isdigit():
            if not first:
                first = i
            if last:
                last = i
    result = int(f'{first}{last}')
    return result


if __name__ == '__main__':
    filename = 'inputdatapart1.txt'
    arrayofdata = datafy(filename)
    total = 0
    for i in arrayofdata:
        total += main(i)
    print(total)
