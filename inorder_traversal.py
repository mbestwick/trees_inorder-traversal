"""
Complete the inOrder function in your editor below, which has 1 parameter: a
pointer to the root of a binary tree. It must print the values in the tree's
inorder traversal as a single line of space-separated values.

Input Format
Our hidden tester code passes the root node of a binary tree to your inOrder
function.

Output Format
Print the tree's inorder traversal as a single line of space-separated values.

"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inOrder(root):
    # initialize a visit list with root
    to_visit = [root]
    # initialize a data empty list
    data = []
    # traverse the tree and add data to the data list
    while to_visit:
        curr = to_visit.pop()
        data.append(curr.data)
        if curr.left:
            to_visit.append(curr.left)
        if curr.right:
            to_visit.append(curr.right)
    # sort the data list
    data.sort()
    # print in order
    for num in data:
        print num,


def inOrder2(root):
    # recurisvely - since it's a BST, can just print in the right order
    if root:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)
