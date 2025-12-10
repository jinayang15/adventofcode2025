num_zeroes = 0
current = 50
with open("day1in.txt", "r") as file:
    for raw_line in file:
        line = raw_line.strip()
        direction = line[0]
        steps = int(line[1:])
        if direction == "L":
            current -= steps
        elif direction == "R":
            current += steps
        current %= 100
        if current == 0:
            num_zeroes += 1

print(num_zeroes)
