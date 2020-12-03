#The given string has pipe delimited nodes that represent family members in a family tree. Each node is a CSV with the values being "parent_id, node_id, node_name". Write a method that takes an input string and return a single result that represents the data as a hierarchy (root, children, siblings, etc).
#Sample input: "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
#• Solve it in any language that you prefer
#• Display the hierarchical result any way you prefer (as long as the parent/child connections are clear)

# solution: 1) build tree 2) print tree.

### USING PYTHON 3.9.0 ###

class Node:
    def __init__(self, parent_id, node_id, node_name) -> None:
        self.parent_id = parent_id
        self.node_id = node_id
        self.node_name = node_name
        self.children = []

    def add_child(self, node) -> None:
        self.children.append(node)

    def get_children(self) -> list:
        return self.children


# make sure we always have a root
def find_root(nodes) -> tuple:
    for node in nodes:
        if node.startswith('null'):
            return True, node
    return False, "null,0,root not found in input"


def find_children(node, nodes) -> list:
    return [child for child in nodes if child.parent_id == node.node_id]
    

def print_tree(node, level=0) -> None:
    print("{}{} (id {})" \
        .format(("-" * level), node.node_name, node.node_id))
    for node in node.get_children():
        print_tree(node, level + 1)


def create_tree(parent, nodes) -> Node:
    children = find_children(parent, nodes)
    if len(children) > 0:
        for node in children:
            parent.add_child(node)
            create_tree(node, nodes)
    return parent


def get_parent_id(node) -> str:
    parent_id,_,_ = node.split(',')
    return parent_id


##
# use this function to coordinate all the work
#
def pipe_to_tree(flat_input) -> None:

    # split string into a list
    node_values = flat_input.split("|")
    # make sure we always have a root
    found, root_value = find_root(node_values)
    if not found:
        node_values.append(root_value)

    # sort to make things easier
    # node_values.sort(key=get_parent_id)
    # move root node to the front to make it even easier
    # node_values.insert(0, node_values.pop())

    # convert to list of node objects
    root = None
    nodes = []
    for node_value in node_values:
        parent_id, node_id, node_name = node_value.split(',')
        node = Node(parent_id, node_id, node_name)
        nodes.append(node)
        if(parent_id == 'null'):
            root = node
    
    # now build and print the tree
    print_tree(create_tree(root, nodes))


### TESTS ###
test1 = "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
test2 = "0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
test3 = "null,0,grandpa|1,3,grandkid|1,4,grandkid|0,1,son|0,2,daugther|2,5,grandkid|5,6,greatgrandkid"

print("\nTEST 1 =-=-=-=-=-=-=-=\n")
pipe_to_tree(test1)
print("\nTEST 2 =-=-=-=-=-=-=-=\n")
pipe_to_tree(test2)
print("\nTEST 3 =-=-=-=-=-=-=-=\n")
pipe_to_tree(test3)



