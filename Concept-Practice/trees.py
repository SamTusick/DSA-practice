# Types: 
#   Binary Tree - Each node has <= 2 childern
#   Binary Search Tree (BST) - left < node < right
#   Balanced Tree - Height is controlled
#   Complete Tree - Filled left to right 
#   Full Tree - Each node has 0 or 2 childern 

# Traversal:
#   DFS(Depth First):
#       Preorder(Root,left,right)
#       Inorder(left,root,right)
#       Postorder(left,right,root)
#   BFS(Level Order):
#       Use a queue

class Node(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    root = Node(10)
    left = Node(5)
    root.left = left 
    right = Node(20)
    root.right = left
    n4 = Node(3) 
    n5 = Node(7)
    n6 = Node(30)
    left.left = n4
    left.right = n5
    right.right = n6

    print(root.val)
    print(left.val)
    print(right.right.val)

if __name__ == "__main__":
    main()