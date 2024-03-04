import random

def shuffle_and_print(items):
    random.shuffle(items)
    for item in items:
        print(item)

# Example usage
my_list = [1, 2, 3, 4, 5]
shuffle_and_print(my_list)
