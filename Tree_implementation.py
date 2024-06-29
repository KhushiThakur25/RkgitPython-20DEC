class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder_traversal(root):
    if root is None:
        return 
    print(root.data, end = " ")
    preOrder_traversal(root.left)
    preOrder_traversal(root.right)

def inOrder_traversal(root):
    if root is None:
        return
    inOrder_traversal(root.left)
    print(root.data,end=" ")
    inOrder_traversal(root.right)

def postOrder_traversal(root):
    if root is None:
        return
    postOrder_traversal(root.left)
    postOrder_traversal(root.right)
    print(root.data, end= " ")

def bfs_traversal(root):
    ans = []
    q = []
    if root is None:
        return ans
    q.append(root)
    while (len(q) > 0):
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        ans.append(node.data)
    return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)


    preOrder_traversal(root)
    print()
    inOrder_traversal(root)
    print()
    postOrder_traversal(root)
    print()

    ans = bfs_traversal(root)

    for i in ans:
        print(i , end= " ")
    

