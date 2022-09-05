class Node: 
    def __init__(self, value): 
        self.value = value
        self.parent = None
        self.left = None 
        self.right = None 
        
class ParseToBinaryTree():
    def __init__(self, s_expression):
        self.root = None
        cleaned_s_expression = self.clean_s_expression(s_expression)
        self.sum = int(cleaned_s_expression[0])
        self.values = cleaned_s_expression[1:]
        self.answer = 'no'

    def clean_s_expression(self, s_expression):
        """
        Returns an array whose first element is the sum the program is looking for and the remaining
        elements are the values in the tree. Note, that the parenthesis can be removed only
        because it's assumed that all S-expression are valid.

        The replace() functions are also specific to the input form, namely that regardless of how
        many children a tree has it will always have two pairs of braces, () ().
        """
        return s_expression.replace('()', '(null)').replace(')', '').split('(')

    def get_answer(self):
        return self.answer

    def build_binary_tree(self):
        """ Build the binary tree from a list of nodes in self.values """
        
        # check for empty tree
        try:
            value = int(self.values.pop(0))
        except:
            return

        self.root = Node(value)

        # node_stack to keep track of nodes that aren't yet full (ie, have 0 or 1 child)
        node_stack = [self.root]
        self._build_binary_tree(self.root, node_stack)
        
    def _build_binary_tree(self, root, node_stack):
        """ Recursively build the binary tree based on left and right child of a node """

        """
        If answer is yes return immediately to avoid unnecessary computation.
        Remove second predicate to test whether the entire binary tree was built correctly
        """
        if not node_stack or self.answer == 'yes':
            return

        if root.left is None:
            # catch error if next element is 'null' (which can't be converted to int)
            try:
                value = int(self.values.pop(0))
            except:
                value = None

            # create new node and assign it to the current root
            new_node = Node(value)
            new_node.parent = root
            root.left = new_node

            # recurse if the node isn't partly leaf
            if value is not None:
                node_stack.append(root.left)
                self._build_binary_tree(root.left, node_stack)

        if root.right is None:
            # catch error if next element is 'null' (which can't be converted to int)
            try:
                value = int(self.values.pop(0))
            except:
                value = None

            # create new node and assign it to the current root
            new_node = Node(value)
            new_node.parent = root
            root.right = new_node
            
            # recurse if the node isn't partly leaf
            if value is not None:
                node_stack.append(root.right)
                self._build_binary_tree(root.right, node_stack)

        if node_stack:
            # check if current root is leaf            
            if root.left.value is None and root.right.value is None:
                # check sum of root-to-leaf path
                sum = 0
                for node in node_stack:
                    sum += node.value
                
                if sum == self.sum:
                    self.answer = 'yes'
                    return

            # pop and current root and recurse with its parent node
            current_root = node_stack.pop()
            self._build_binary_tree(current_root.parent, node_stack)

    def print_binary_tree(self):
        """ Print binary tree for debugging purposes """
        self._print_binary_tree(self.root)
        print()

    def _print_binary_tree(self, root):
        """ Print binary tree for debugging purposes """
        if root is None:
            return

        print(root.value, end=' ')
        if root.left is not None:
            print('(', end=' ')
            self._print_binary_tree(root.left)
            print(')', end=' ')
        if root.right is not None:
            print('(', end=' ')
            self._print_binary_tree(root.right)
            print(')', end=' ')