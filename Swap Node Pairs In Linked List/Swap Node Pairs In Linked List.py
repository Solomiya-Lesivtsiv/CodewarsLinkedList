class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    node = Node(0)
    node.next = head
    prev = node
    while prev.next is not None and prev.next.next is not None:
        a = prev.next
        b = a.next
        a.next = b.next
        b.next = a
        prev.next = b
        prev = a
    return node.next
