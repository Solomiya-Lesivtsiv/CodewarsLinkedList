class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
