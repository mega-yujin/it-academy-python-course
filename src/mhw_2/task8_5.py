"""You have a sequence of strings, and you’d like to determine
the most frequently occurring string in the sequence.
It can be the only one."""


def most_frequent(data: list[str]) -> str:
    # your code here
    data_set = set(data)
    answer = ''
    value = 0
    for element in data_set:
        if data.count(element) > value:
            value = data.count(element)
            answer = element
    return answer


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
