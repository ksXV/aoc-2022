elfs_total_cals_arr = []
with open("input.txt", encoding='utf-8') as f:
    text_input = f.read()
    text_input_array = text_input.split("\n")
    current_max_cal = 0
    max_cal = 0

    for number in text_input_array:
        if number != '':
            current_max_cal = current_max_cal + int(number)
        else:
            if current_max_cal > max_cal:
                max_cal = current_max_cal
            elfs_total_cals_arr.append(current_max_cal)
            current_max_cal = 0


elfs_total_cals_arr.sort(reverse=True)

print("The highest calories found are: ", max_cal)

total_cal_of_n_elves_idx = int(input(
    "Please enter the number of elves that you wanna find out how many calories are they carrying in total : \n"))
total_cal_of_n_elves = 0

for number_of_cals in elfs_total_cals_arr[:total_cal_of_n_elves_idx]:
    total_cal_of_n_elves = total_cal_of_n_elves + number_of_cals

print(total_cal_of_n_elves)
