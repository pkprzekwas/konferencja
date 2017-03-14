from math import ceil


def tree_gen(rows):
    if rows < 4:
        raise ValueError(
            'Input should be grater than 4')
    for row in range(rows):
        if row < rows - 1:
            print((rows - row) * ' ' + (2 * row - 1) * '#')
        else:
            print((ceil((2 * row - 1) / 2) * ' ' + '#'))


if __name__ == "__main__":
    tree_height = input("How tall is the tree: ")
    tree_height = int(tree_height)
    print(tree_gen(tree_height))
