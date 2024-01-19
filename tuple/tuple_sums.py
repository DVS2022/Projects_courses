import random


def change(nums):
    """Takes a tuple of numbers (nums), randomly selects an index within
    the range [0, 5], generates a random value in the range [100, 1000],
    replaces the value at the selected index with the new random value,
    and returns a tuple containing the modified numbers and the randomly
    generated value."""
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    return tuple(nums), value


my_nums = (1, 2, 3, 4, 5)

new_nums, rand_val = change(list(my_nums))
print(new_nums, rand_val)
sum_rand_val = rand_val
new_nums, rand_val = change(list(new_nums))
print(new_nums, rand_val)
sum_rand_val += rand_val
print(sum_rand_val)
