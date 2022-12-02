# Oponent letters:
# A : rock
# B : paper
# C : scissors

# My letters :
# X : rock      -> 1 point
# Y : paper     -> 2 points
# Z : scissors  -> 3 points

# 0 for lossing
# 3 for draw
# 6 for winning

# X beats C
# Y beats A
# Z beats B


first_guess_points = 0
actual_points = 0


with open("./input.txt", encoding='utf-8') as f:
    input_text_arr = f.read().split("\n")

    for played_match in input_text_arr:
        match played_match[2]:
            case "X":
                # lost
                first_guess_points = first_guess_points + 1
                if played_match[0] == "C":
                    first_guess_points = first_guess_points + 6
                    actual_points += 2
                elif played_match[0] == "A":
                    first_guess_points = first_guess_points + 3
                    actual_points += 3
                else:
                    actual_points += 1

            case "Y":
                # draw
                first_guess_points = first_guess_points + 2
                actual_points += 3
                if played_match[0] == "A":
                    first_guess_points = first_guess_points + 6
                    actual_points += 1

                elif played_match[0] == "B":
                    first_guess_points = first_guess_points + 3
                    actual_points += 2
                else:
                    actual_points += 3
            case "Z":
                # won
                first_guess_points = first_guess_points + 3
                actual_points += 6
                if played_match[0] == "B":
                    first_guess_points = first_guess_points + 6
                    actual_points += 3

                elif played_match[0] == "C":
                    first_guess_points = first_guess_points + 3
                    actual_points += 1
                else:
                    actual_points += 2
            case _:
                print("something went wrong")


print(first_guess_points)
print(actual_points)
