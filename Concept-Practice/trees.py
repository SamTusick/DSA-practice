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
def build_tree(values):
    queue = []
    i = 0
    while len(queue) != 0 and i < len(values):
        if len(queue) == 0:
            root = Node(values[i])
            queue.append(root)
            i += 1
        node = Node(values[i])
        next_node = Node(values[i+1])
        queue[0].left = node
        queue[0].right = next_node

        


def main():
    nums = [10, 5, 20, 3, 7, None, 30]


if __name__ == "__main__":
    main()