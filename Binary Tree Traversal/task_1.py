# Pre-order traversal
def pre_order(node):
    result = []
    if not node:
        return result
    result.append(node.data)
    result += pre_order(node.left)
    result += pre_order(node.right)
    return result 

# In-order traversal
def in_order(node):
    result = []
    if not node:
        return result
    result += in_order(node.left)
    result.append(node.data)
    result += in_order(node.right)
    return result


# Post-order traversal
def post_order(node):
    result = []
    if not node:
        return result
    result += post_order(node.left)
    result += post_order(node.right)
    result.append(node.data)
    return result
