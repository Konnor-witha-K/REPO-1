# The Series 1^1 + 2^2 + 3^3... 10^10 = 10405071317
# Find the last ten digits of the series up to 1000^1000


def count_sequence():
    sum = 0
    x = 1
    for i in range(1, 11):
        y = x**x
        sum = sum + y
        x += 1
    return sum

print(f"The Series of equal powers up to 10 == {count_sequence()}")