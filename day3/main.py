from string import ascii_lowercase, ascii_uppercase


def split_rucksack(rucksack):
    half_rucksack_length = int(len(rucksack) / 2)
    return rucksack[:half_rucksack_length], rucksack[half_rucksack_length::]


def get_rucksack_duplicate_item(rucksack):
    compartment1, compartment2 = split_rucksack(rucksack)
    duplicate_items = list(set(compartment1).intersection(set(compartment2)))
    return "".join(duplicate_items)


def get_rucksacks_duplicate_item(rucksacks):
    duplicate_items = set(rucksacks[0])
    for rucksack in rucksacks:
        duplicate_items = duplicate_items.intersection(set(rucksack))
    return "".join(list(duplicate_items))


def get_priority(item):
    return list(ascii_lowercase + ascii_uppercase).index(item) + 1


def get_rucksack_priority(rucksack):
    duplicate_item = get_rucksack_duplicate_item(rucksack)
    duplicate_item_priority = get_priority(duplicate_item)
    return duplicate_item_priority


def get_priority_sum_for_rucksacks(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        priority_sum += get_rucksack_priority(rucksack.strip())
    return priority_sum


def get_priority_sum_for_groups(groups):
    group_priority_sum = 0
    for rucksacks in groups:
        rucksacks_priority_item = get_rucksacks_duplicate_item(rucksacks)
        group_priority_sum += get_priority(rucksacks_priority_item)
    return group_priority_sum


if __name__ == '__main__':

    # Part 1
    with open("input.txt", "r") as f:
        rucksacks = f.readlines()
        print(get_priority_sum_for_rucksacks(rucksacks))

    # Part 2
    with open("input.txt", "r") as f:
        groups = []
        rucksacks = []
        for line in f.readlines():
            rucksacks.append(line.strip())
            if len(rucksacks) == 3:
                groups.append(list(rucksacks))
                rucksacks.clear()

        print(get_priority_sum_for_groups(groups))
