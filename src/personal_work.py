# Creating a binary search tree. 

# Creating the Root 

class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 
# Insert def 
    def insert(self, value): 
        if self.value:
            
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        
        else:
            self.vale = value
# Print def 
    def SeeTree(self):
        if self.left:
            self.left.SeeTree()
        print(self.value),
        if self.right:
            self.right.SeeTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.SeeTree()

# Inserting
# To insert into a tree we use the node class created and add a insert def to it. 
# The insert function compares the value passed to the parent node and decides to add it as a left node or a right based on a condition 

# Traversal 
# Traversing a tree is the process of visiting all the nodes of a tree. 
# All nodes are connected via edges 
# We always START at the root (head) node - we cannot randomly access a node in a tree
# There are 3 ways to traverse a tree: 
# - In-order traversal
# - Pre-order traversal
# - Post-order traversal