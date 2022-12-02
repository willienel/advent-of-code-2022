def get_food_sums():
    food_sums = []
    largest_sum = 0
    with open("input.txt", "r") as f:
        food_sum = 0
        for line in f.readlines():
            if len(line.strip()) == 0:
                if food_sum > largest_sum:
                    largest_sum = food_sum
                food_sums.append(food_sum)
                food_sum = 0
            else:
                food_sum += int(line)
    return sorted(food_sums)


if __name__ == '__main__':

    food_sums = get_food_sums()

    # part 1
    print(food_sums[-1])

    # part 2
    print(sum(food_sums[-3:]))
