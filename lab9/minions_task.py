from typing import NamedTuple
import sys

Minion = NamedTuple('Minion', [('name', str),
                               ('hunger', int),
                               ('motivation', int),
                               ('size', str)])

def line_to_minion(line):
    data = line.strip().split(';')
    return Minion(data[0], int(data[1]), int(data[2]), data[3])

def minion_to_line(minions):
    return f'{minions.name} {minions.hunger} ({minions.size})'

def sort_minions(minions):
    minions.sort(key = lambda minion: (-minion.motivation, minion.name))
    return minions

def main():
    with open(sys.argv[1]) as file:
        minions = []
        for line in file:
            minions.append(line_to_minion(line))
        for minion in sort_minions(minions):
            print(minion_to_line(minion))

if __name__ == '__main__':
    main()

