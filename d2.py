lines = []

with open('d2input.txt') as f:
    lines = f.readlines()

def checksum(s):
    twos = False
    threes = False

    for c in s:
        if s.count(c) == 2:
            twos = True

        if s.count(c) == 3:
            threes = True

    return twos, threes

twos = 0
threes = 0

for line in lines:
    a, b = checksum(line)

    if a:
        twos += 1

    if b:
        threes += 1

print(twos, threes)

