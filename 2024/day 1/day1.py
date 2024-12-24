def open_file(file):
    left = []
    right = []

    with open(file, 'r') as f:
        for i in f:
            i = i.strip().split()
            left.append(int(i[0]))
            right.append(int(i[1]))
    return (left, right)


def part1():
    left, right = open_file("2024/day 1/input.txt")
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(total)


part1()

def part2():
    left, right = open_file("2024/day 1/input.txt")

    # first get the hash map
    hash = {}
    score = 0
    
    # store right freq
    for i in range(len(right)):
        hash[right[i]] = hash.get(right[i], 0) + 1

    for i in range(len(left)): 
        if left[i] in hash:
            score += hash[left[i]] * left[i] 

    print(score)

part2()
