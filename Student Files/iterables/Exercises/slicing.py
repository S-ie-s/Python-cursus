import math

def split_list(orig_list):
    length_list = len(orig_list)
    mid_length = math.ceil(length_list/2)
    split_list_1 = orig_list[:mid_length]
    split_list_2 = orig_list[mid_length:]
    return [split_list_1, split_list_2]

    # split_list_1 = orig_list[:3]
    # split_list_2 = orig_list[3:]
    # return split_list_1, split_list_2

def main():
    colors = ["red", "blue", "green", "orange", "purple"]
    colors_split = split_list(colors)
    print(colors_split[0])
    print(colors_split[1])

main()