import random

from modules.Interpreter.Layer import Layer
from modules.Interpreter.Struct import Struct
from modules.Interpreter.StructInstance import StructInstance

BSPNode = Struct("BSPNode", ["split_plane", "depth", "left", "right"])


def bsp(args):
    matrix = args[0]
    depth = args[1]

    if isinstance(matrix, Layer):
        matrix = matrix.rows

    rows, cols = len(matrix), len(matrix[0])

    # Amount of splits
    if depth == 1:
        if random.choice([True, False]):  # Vertical split
            split_point = int(cols / 2)

            # Slices each row up to the split point
            left_matrix = [row[:split_point] for row in matrix]
            # Slices from split point to end
            right_matrix = [row[split_point:] for row in matrix]

            node = StructInstance(BSPNode, {"split_plane": "vertical",
                                            "depth": depth,
                                            "left": left_matrix,
                                            "right": right_matrix})

            return node

        else:  # Horizontal split
            split_point = int(rows / 2)

            upper_matrix = matrix[:split_point]
            lower_matrix = matrix[split_point:]

            node = StructInstance(BSPNode, {"split_plane": "vertical",
                                            "depth": depth,
                                            "left": upper_matrix,
                                            "right": lower_matrix})

            return node

    if random.choice([True, False]):  # Vertical split
        split_point = int(cols / 2)
        node = StructInstance(BSPNode, {"split_plane": "vertical",
                                        "depth": depth,
                                        "left": None,
                                        "right": None})

        # Slices each row up to the split point
        left_matrix = [row[:split_point] for row in matrix]
        # Slices from split point to end
        right_matrix = [row[split_point:] for row in matrix]

        left_args = (left_matrix, depth - 1)
        right_args = (right_matrix, depth - 1)

        node.fields["left"] = bsp(left_args)
        node.fields["right"] = bsp(right_args)
    else:  # Horizontal split
        split_point = int(rows / 2)
        node = StructInstance(BSPNode, {"split_plane": "horizontal",
                                        "depth": depth,
                                        "left": None,
                                        "right": None})

        upper_matrix = matrix[:split_point]
        lower_matrix = matrix[split_point:]

        upper_args = (upper_matrix, depth - 1)
        lower_args = (lower_matrix, depth - 1)

        node.fields["left"] = bsp(upper_args)
        node.fields["right"] = bsp(lower_args)

    return node

def departition(args):
    node = args[0]

    if isinstance(node, StructInstance):
        left = departition([node.fields["left"]])
        right = departition([node.fields["right"]])

        if isinstance(left, Layer) and isinstance(right, Layer):
            left = left.rows
            right = right.rows
    else:
        return node

    matrix = []
    if node.fields["split_plane"] == "vertical":
        for row in range(len(left)):
            matrix.append(left[row])
        for row in range(len(right)):
            matrix.append(right[row])
    elif node.fields["split_plane"] == "horizontal":
        for row in range(len(left)):
            matrix.append(left[row] + right[row])

    layer = Layer(len(matrix), len(matrix[0]), 0)
    layer.rows = matrix
    return layer


def print_bsp_tree(node, level=0):
    if node is not None:
        print('  ' * level + str(node.fields["split_plane"]))
        print_bsp_tree(node.fields["left"], level + 1)
        print_bsp_tree(node.fields["right"], level + 1)
