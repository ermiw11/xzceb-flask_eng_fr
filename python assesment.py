class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    res = []
    while stack2:
        node = stack2.pop()
        res.append(node.val)

    return res
