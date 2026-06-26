class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p_path = []
        self.q_path = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if the current one is p or q, this node is LCA
        # if root is None, return none for nothing found
        if root is None or root == p or root == q:
            return root

        # check left and right for p and q
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # if p and q in both left and right, this node is LCA
        if left and right:
            return root
    
        # just return if we found p or q
        return left or right


    
    # Just track the path to both p and q and compare it to get the result
    def lowestCommonAncestor_MySolution(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find([],root,p,q)
        result = None
        for i in range(min(len(self.p_path),len(self.q_path))):
            if self.p_path[i] == self.q_path[i]:
                result = self.p_path[i]

        return result

    
    def find(self,path,node,p,q):
        if node == None:
            return
        if self.p_path != [] and self.q_path != []:
            return
        
        path.append(node)

        if node == p:
            self.p_path = path.copy()
        if node == q:
            self.q_path = path.copy()

        self.find(path,node.left,p,q)
        self.find(path,node.right,p,q)

        path.pop()

def gen_tree(root,p,q):
    p_node = None
    q_node = None

    for i,n in enumerate(root):
        if n is None:
            continue
        root[i] = TreeNode(root[i])
        if n == p:
            p_node = root[i]
        if n == q:
            q_node = root[i]
        if i == 0:
            continue

        if i%2:
            root[(i-1)//2].left  = root[i]
        else:
            root[(i-1)//2].right = root[i]
    return (root[0],p_node,q_node)

def valid(root,p,q,wanted):
    [tree,p_node,q_node] = gen_tree(root.copy(),p,q)

    result = (Solution()).lowestCommonAncestor(tree,p_node,q_node)
    print("-----")
    if result.val == wanted:
        print("Ok")
    else:
        print("Failed")
        print("Input    :",root,p,q)
        print("Output   :",result)
        print("Excepted :",wanted)

valid([3,5,1,6,2,0,8,None,None,7,4],5,1,3)
valid([3,5,1,6,2,0,8,None,None,7,4],5,4,5)
valid([1,2],1,2,1)