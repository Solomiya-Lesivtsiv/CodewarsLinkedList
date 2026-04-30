class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index")
    current = node
    i = 0
    while current is not None and i < index:
        current = current.next
        i += 1
    if current is None:
        raise Exception("Invalid index")
    return current
  