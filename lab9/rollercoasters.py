import sys
from typing import NamedTuple

RollerCoaster = NamedTuple('RollerCoaster', [('name', str),
                                                ('world', str),
                                                ('height', int),
                                                ('time', int)])


def line_to_coaster(line):
    data = line.strip().split(';')
    return RollerCoaster(data[0], data[1], int(data[2]), int(data[3]))


def coaster_to_line(coasters):
    return f'{coasters.name} ({coasters.world}): {coasters.time}'


def sort_coaster(coasters):
    coasters.sort(key=lambda rollercoaster: (rollercoaster.time, -rollercoaster.height, rollercoaster.name ))
    return coasters


def main():
    with open(sys.argv[1]) as file:
        coasters = []
        for line in file:
            coasters.append(line_to_coaster(line))
        for coaster in sort_coaster(coasters):
            print(coaster_to_line(coaster))


if __name__ == "__main__":
    main()
