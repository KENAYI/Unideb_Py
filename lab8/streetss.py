import sys

streets={}
with open(sys.argv[1]) as file:
    for line in file:
        data = line.strip().split(';')
        if data[0] in streets:
            streets[data[0]] += float(data[2])
        else:
            streets[data[0]] = float(data[2])

for key, value in sorted(streets.items(), key = lambda x: (-x[1], x[0])):
    print(key)