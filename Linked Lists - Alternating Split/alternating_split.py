class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise ValueError("Cannot split an empty list")
    elif head.next is None:
        raise ValueError("Cannot split a list with 1 element")
    first = None
    second = None
    line1 = None
    line2 = None
    current = head
    i = 0

    while current is not None:
        cur = current.next
        current.next = None
        if i % 2 == 0:
            if first is None:
                first = line1 = current
            else:
                line1.next = current
                line1 = current
        else:
            if second is None:
                second = line2 = current
            else:
                line2.next = current
                line2 = current
        i += 1
        current = cur
    return Context(first, second)
