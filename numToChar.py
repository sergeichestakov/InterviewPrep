MAPPING = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    0: 'Z'
}

NUM_LETTERS = len(MAPPING)

def numToChar(num: int) -> str:
    ret = ""

    while num > 0:
        ret += MAPPING[num % NUM_LETTERS]
        nextNum = num // NUM_LETTERS
        if num % NUM_LETTERS == 0:
            nextNum -= 1

        num = nextNum

    return ret[::-1]

def run_tests():
    # Only one letter
    assert numToChar(1) == "A"
    assert numToChar(2) == "B"
    assert numToChar(25) == "Y"
    assert numToChar(26) == "Z"

    # Two letters starting with A
    assert numToChar(27) == "AA"
    assert numToChar(28) == "AB"
    assert numToChar(52) == "AZ"

    # Two letters starting with B
    assert numToChar(53) == "BA"
    assert numToChar(54) == "BB"
    assert numToChar(78) == "BZ"

    # Two letters starting with C
    assert numToChar(79) == "CA"
    assert numToChar(80) == "CB"
    assert numToChar(104) == "CZ"

    # Two letters starting with D
    assert numToChar(105) == "DA"

    # 26 iterations of the alphabet: two letters starting with Y
    assert numToChar(26 * 26) == "YZ"

    # 27 iterations of the alphabet: two letters starting with Z
    assert numToChar(26 * 27) == "ZZ"

    # Three letter examples: > 27 iterations of the alphabet
    assert numToChar(26 * 27 + 1) == "AAA"
    assert numToChar(26 * 27 + 2) == "AAB"
    assert numToChar(26 * 28) == "AAZ"
    assert numToChar(26 * 28 + 1) == "ABA"

if __name__ == '__main__':
    run_tests()

