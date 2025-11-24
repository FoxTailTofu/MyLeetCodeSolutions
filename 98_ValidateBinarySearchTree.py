class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FirstSolution:
    def isValidBST(self, root) -> bool:
        return self.valid(root, None, None)

    def valid(self, node, minVal, maxVal) -> bool:
        nodeValid = True
        leftValid = True
        rightValid = True
        if minVal is not None:
            nodeValid = nodeValid and node.val > minVal
        if maxVal is not None:
            nodeValid = nodeValid and node.val < maxVal

        if node.left is not None:
            nodeValid = nodeValid and node.val > node.left.val
            leftValid = self.valid(node.left, minVal, min(maxVal or node.val, node.val))
        if node.right is not None:
            nodeValid = nodeValid and node.val < node.right.val
            rightValid = self.valid(
                node.right, max(node.val, minVal or node.val), maxVal
            )
        return nodeValid and leftValid and rightValid

# Somehow slower??
class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, minVal, maxVal):
            if node is None:
                return True
            if not (minVal < node.val < maxVal):
                return False
            left = valid(node.left, minVal, min(maxVal, node.val))
            right = valid(node.right, max(minVal, node.val), maxVal)
            return left and right
        # float("inf") for initial range is something I'm not really comfortable to use, but I guess I should use it to clean the code
        return valid(root, float("-inf"), float("inf"))


# AI generated because I'm lazy
def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(x) if x is not None else None for x in arr]
    n = len(arr)

    for i in range(n):
        if nodes[i] is None:
            continue
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < n:
            nodes[i].left = nodes[left_i]
        if right_i < n:
            nodes[i].right = nodes[right_i]

    return nodes[0]


# Test
def printValid(arr, ans):
    ret = (Solution()).isValidBST(build_tree(arr))
    print("Correct" if ret == ans else "!!Wrong")


printValid([2, 1, 3], True)
printValid([0, None, -1], False)
printValid([5, 4, 6, None, None, 3, 7], False)
printValid([5, 1, 4, None, None, 3, 6], False)
printValid([32, 26, 47, 19, None, None, 56, None, 27], False)
