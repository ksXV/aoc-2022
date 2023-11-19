def parse_string(string: str) -> str:
    for char in string:
        if char in " []":
            continue
        return char
    return ""


def parse_number(line: str) -> int:
    i = 0
    number = 0
    pow = 1
    while line[i] in "0123456789":
        number = int(line[i]) + number * pow
        pow *= 10
        i += 1
    return number


def parse_line(line: str) -> list:
    result = []
    line = line.removeprefix("move ")
    quantity = parse_number(line)
    result.append(quantity)
    line = line.removeprefix("{number} from ".format(number=quantity))
    get_from = parse_number(line)
    result.append(get_from)
    line = line.removeprefix("{number} to ".format(number=get_from))
    result.append(parse_number(line))

    return result


with open("input.txt", "r+") as f:
    max_number = ""
    line_length = 0
    while True:
        max_number = f.readline()
        line_length = len(max_number)
        max_number = max_number.strip(" ")
        max_number = max_number.removesuffix(" \n")
        if max_number[0] in "123456789":
            max_number = max_number[len(max_number) - 1]
            break

    stacks = [[] for i in range(int(max_number))]
    count = 1

    f.seek(0)
    count = -1
    while True:
        readBytes = f.read(4)
        count += 1
        letter = parse_string(readBytes)
        if letter in " ":
            continue
        if letter in "123456789":
            break
        if letter not in " \n":
            stacks[count % int(max_number)].append(letter)
        if letter in "123456789":
            break
    f.seek(f.tell() + line_length - 3)

    while True:
        line = f.readline()
        if line == "":
            break
        instructions = parse_line(line)
        quantity = instructions[0]
        get_from = instructions[1]
        move_to = instructions[2]
        offset = len(stacks[get_from - 1]) - quantity
        for i in range(quantity):
            get_from_len = len(stacks[get_from - 1])
            # first problem
            # stacks[move_to - 1].insert(0, stacks[get_from - 1].pop())
            stacks[move_to - 1].insert(0, stacks[get_from - 1].pop(get_from_len - 1 - offset))
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)
