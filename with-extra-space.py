# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
	Nodes = getNodesInOrder(root,[])
	for i in range(len(Nodes)-1):
		leftNode = Nodes[i]
		rightNode = Nodes[i+1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return Nodes[0]
		
def getNodesInOrder(node,array):
	if node is not None:
		getNodesInOrder(node.left, array)
		array.append(node)
		getNodesInOrder(node.right, array)
	return array

