class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def stringify(node):
    if node is None:
        return 'None'
    current = node
    list_of_nodes = ''
    while current is not None:
        list_of_nodes += f'{current.data} -> '
        current = current.next
        if current == None:
            list_of_nodes += 'None'
            break
    return list_of_nodes