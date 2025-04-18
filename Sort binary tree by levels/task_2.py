def tree_by_levels(node):
    result = []
    if not node:
        return result
    queue = [node]
    i = 0
    while i < len(queue):
        current = queue[i]
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        i += 1
    return result