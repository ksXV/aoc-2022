with open("./input.txt", encoding='utf-8') as f:
    input_text_arr = f.read().split("\n")
wanted_intervals = []

for sets_intervals in input_text_arr:
    intervals = sets_intervals.split(",")
    for interval in intervals:
        numbers_arr = interval.split("-")
        wanted_intervals.append(numbers_arr)

first_max = 0
second_max = 0

counter = 0
counter_part_two = 0

# 2 8
# 3 7


def part1():
    ret = 0
    for i in range(len(wanted_intervals)):
        if i % 2 == 0:
            first_max = int(wanted_intervals[i][0])
            second_max = int(wanted_intervals[i][1])
        if i % 2 == 1:
            if int(wanted_intervals[i][0]) <= first_max and int(wanted_intervals[i][1]) >= second_max or int(wanted_intervals[i][0]) >= first_max and int(wanted_intervals[i][1]) <= second_max:
                ret += 1
    return ret


def part2():
    ret = 0
    for pair in input_text_arr:
        pair = pair.split(',')

        a = int(pair[0][:pair[0].find('-')])
        b = int(pair[0][pair[0].find('-'):].removeprefix('-'))

        c = int(pair[1][:pair[1].find('-')])
        d = int(pair[1][pair[1].find('-'):].removeprefix('-'))

        def has_a_match():
            for i in range(a, b+1):
                for j in range(c, d+1):
                    if i == j:
                        return True
        if has_a_match():
            ret += 1
    return ret


counter = part1()
counter_part_two = part2()

print(counter)
print(counter_part_two)
