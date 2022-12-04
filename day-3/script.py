with open("./input.txt", encoding='utf-8') as f:
    input_text_arr = f.read().split("\n")

recuring_char = {}

recuring_badge_1 = {}
recuring_badge_2 = {}
recuring_badge_3 = {}

total_sum = 0

total_sum_badge = 0

# first part
for word in input_text_arr:

    word_length = len(word)
    first_comparment = int(word_length / 2)

    for i in range(first_comparment):
        if not word[i] in recuring_char.keys():
            recuring_char[word[i]] = 1
    for char in word[first_comparment:word_length]:
        if char in recuring_char.keys() and recuring_char[char] == 1:
            recuring_char[char] = recuring_char[char] + 1
            if char.islower() == True:
                total_sum = total_sum + ord(char) - 96
            else:
                total_sum = total_sum + ord(char) - 38
    recuring_char = {}

# print(total_sum)

# second part
for i in range(len(input_text_arr)):
    if (i + 1) % 3 == 1:
        for char in input_text_arr[i]:
            if not char in recuring_badge_1.keys():
                recuring_badge_1[char] = 1
    if (i + 1) % 3 == 2:
        for char in input_text_arr[i]:
            if not char in recuring_badge_2.keys():
                recuring_badge_2[char] = 1
    if (i + 1) % 3 == 0:
        for char in input_text_arr[i]:
            if not char in recuring_badge_3.keys():
                recuring_badge_3[char] = 1
        for characther in recuring_badge_1.keys():
            if characther in recuring_badge_2.keys() and characther in recuring_badge_3.keys():
                if characther.islower() == True:
                    total_sum_badge = total_sum_badge + ord(characther) - 96
                else:
                    total_sum_badge = total_sum_badge + ord(characther) - 38
        recuring_badge_1 = {}
        recuring_badge_2 = {}
        recuring_badge_3 = {}
print(total_sum_badge)
