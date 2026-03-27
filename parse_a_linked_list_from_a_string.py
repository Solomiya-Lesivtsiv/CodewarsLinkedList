from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    tokens = list_repr.split(' -> ')
    if tokens == ["None"]:
        return None
    tokens.remove('None')
    head = None
    for _, el in enumerate(tokens[::-1]):
        head = Node(int(el), head)
    return head