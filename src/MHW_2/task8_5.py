"""
Simple
Pawn Brotherhood
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.
"""


def safe_pawns(pawns: set) -> int:
    safe_count = 0
    for pawn in pawns:
        column, row = pawn[0], int(pawn[1])
        left_defender = chr(ord(column) - 1) + str(row - 1)
        right_defender = chr(ord(column) + 1) + str(row - 1)

        if left_defender in pawns or right_defender in pawns:
            safe_count += 1

    return safe_count


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
