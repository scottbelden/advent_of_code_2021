from io import StringIO
from math import prod
from utils import answer1, answer2, get_input, debug

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_16_input")[0]

num_bits = 4 * len(puzzle_input)
binary = bin(int(puzzle_input, 16))[2:].zfill(num_bits)

sio = StringIO(binary)
version_sum = 0


def read_literal(sio):
    literal = ""
    while True:
        if sio.read(1) == "1":
            literal += sio.read(4)
            continue
        else:
            literal += sio.read(4)
            return int(literal, 2)


def read_packet(sio):
    global version_sum
    version = int(sio.read(3), 2)
    version_sum += version
    packet_id = int(sio.read(3), 2)
    if packet_id == 4:
        value = read_literal(sio)
        debug(f"literal: {value}")
        return value
    else:
        length_type_id = sio.read(1)
        literals = []
        if length_type_id == "0":
            sub_packet_len = int(sio.read(15), 2)
            current_pos = sio.tell()
            while sio.tell() < current_pos + sub_packet_len:
                literals.append(read_packet(sio))
        else:
            num_packets = int(sio.read(11), 2)
            for i in range(num_packets):
                literals.append(read_packet(sio))

        if packet_id == 0:
            debug(f"sum({literals})")
            return sum(literals)
        elif packet_id == 1:
            debug(f"prod({literals})")
            return prod(literals)
        elif packet_id == 2:
            debug(f"min({literals})")
            return min(literals)
        elif packet_id == 3:
            debug(f"max({literals})")
            return max(literals)
        elif packet_id == 5:
            debug(f"{literals[0]} > {literals[1]}")
            return 1 if literals[0] > literals[1] else 0
        elif packet_id == 6:
            debug(f"{literals[0]} < {literals[1]}")
            return 1 if literals[0] < literals[1] else 0
        elif packet_id == 7:
            debug(f"{literals[0]} == {literals[1]}")
            return 1 if literals[0] == literals[1] else 0


output = read_packet(sio)


ANSWER1 = answer1(version_sum)

ANSWER2 = answer2(output)
