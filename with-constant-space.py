class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
	left, right = flatten(root)
	return left
	

def flatten(node):
	if node.left is None:
		leftMost = node
	else:
		leftMostSubLeft, RightMostSubLeft = flatten(node.left)
		connect(RightMostSubLeft, node)
		leftMost = leftMostSubLeft
		
	if node.right is None:
		rightMost = node
	else:
		leftMostSubRight, RightMostSubRight = flatten(node.right)
		connect(node, leftMostSubRight)
		rightMost = RightMostSubRight
	return [leftMost, rightMost]

def connect(left, right):
	left.right = right
	right.left = left