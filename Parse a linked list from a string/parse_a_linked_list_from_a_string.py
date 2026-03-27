class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    tokens = list_repr.split(' -> ')
    if tokens == ["None"]:
        return None
    tokens.remove('None')
    head = None
    for _, el in enumerate(tokens[::-1]):
        head = Node(int(el), head)
    return head
