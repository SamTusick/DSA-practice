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

from collections import deque

class Node(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
def build_tree(values):
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root]) # creates new queue with root as first item
    i = 1  # start from the second element

    while queue and i < len(values):
        parent = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            left_node = Node(values[i])
            parent.left = left_node
            queue.append(left_node)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            right_node = Node(values[i])
            parent.right = right_node
            queue.append(right_node)
        i += 1

    return root 
def preorder(node, values):
    if not node:
        return values
    values.append(node.val)
    left = node.left
    right = node.right
    if left:
       preorder(left, values)
    if right:
        preorder(right, values)

    return values
def inorder(node, values):
    if not node:
        return values
    
    left = node.left
    right = node.right
    if left:
        inorder(left,values)
    values.append(node.val)
    if right:
        inorder(right,values)

    return values
def post_order(node,values):
    if not node:
        return values
    left = node.left
    right = node.right

    if left:
        post_order(left,values)
    if right:
        post_order(right,values)
    values.append(node.val)

    return values

def main():
    nums = [10, 5, 20, 3, 7, None, 30]
    root = build_tree(nums)
    pre_order_list = []
    preorder(root, pre_order_list)
    print("Pre order: ", pre_order_list)
    inorder_list = []
    inorder(root, inorder_list)
    print("Inorder : ", inorder_list)
    post_order_list = []
    post_order(root, post_order_list)
    print("Post Order: " , post_order_list)

if __name__ == "__main__":
    main()