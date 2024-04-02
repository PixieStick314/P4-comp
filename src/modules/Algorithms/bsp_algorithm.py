#   BSP-Algorithm
class Node3D:
    def __init__(self, x, y, z, width, height, depth, parent=None):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.parent = parent
        self.children = []

def split_space_3d(node, min_size):
    """
    Recursively splits a given 3D space (node) into smaller partitions based on the BSP algorithm,
    until all partitions are smaller than the specified minimum size in any dimension.
    
    Parameters:
    - node: The current node (space) to be partitioned. It includes properties like x, y, z, width, height, and depth.
    - min_size: The minimum size of any dimension for the resulting partitions. If any dimension of the current node
                is less than or equal to this size, the node will not be split further.
    """
    # Base case: if the node is already smaller than the minimum size in all dimensions, do not split further.
    if node.width <= min_size or node.height <= min_size or node.depth <= min_size:
        return
    # Determine the axis along which to split. This example chooses the longest axis for simplicity,
    # but other heuristics can be applied.
    max_dimension = max(node.width, node.height, node.depth)

    if max_dimension == node.width:
        split_axis = 'x'
    elif max_dimension == node.height:
        split_axis = 'y'
    else:
        split_axis = 'z'
    
    # Perform the split along the chosen axis. This example splits the node in half along the axis, will need too implement random.
    # but other strategies (e.g., based on content or distribution within the space) can be used.
    if split_axis == 'x':
        split_point = node.width // 2
        left_child = Node3D(node.x, node.y, node.z, split_point, node.height, node.depth)
        right_child = Node3D(node.x + split_point, node.y, node.z, node.width - split_point, node.height, node.depth)
    elif split_axis == 'y':
        split_point = node.height // 2
        left_child = Node3D(node.x, node.y, node.z, node.width, split_point, node.depth)
        right_child = Node3D(node.x, node.y + split_point, node.z, node.width, node.height - split_point, node.depth)
    else: # split_axis == 'z'
        split_point = node.depth // 2
        left_child = Node3D(node.x, node.y, node.z, node.width, node.height, split_point)
        right_child = Node3D(node.x, node.y, node.z + split_point, node.width, node.height, node.depth - split_point)
    
    # Recursively split the child nodes.
    split_space_3d(left_child, min_size)
    split_space_3d(right_child, min_size)
    
    # After the split, the original node's children property can be updated to point to the new partitions.
    node.children = [left_child, right_child]

def bsp_partition(dimensions, min_size):
    root = Node3D(0, 0, 0, *dimensions)
    split_space_3d(root, min_size)
    return root

# Additional utility functions can be added here, such as for querying the BSP tree.
