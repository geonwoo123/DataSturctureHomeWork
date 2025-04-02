class Node:
    class NodeIterator:
        def __init__(self, node):
            self.current = node

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            data = self.current
            self.current = self.current.link
            return data

    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def __iter__(self):
        return Node.NodeIterator(self)


def build(size):
    head = Node(data=f"node:0")
    current = head
    for i in range(1, size):
        new_node = Node(data=f"node:{i}")
        current.link = new_node
        current = new_node
    return head


def explore(head):
    current = head
    while current is not None:
        if current.link:
            print(f"({current.data})->", end="")
        else:
            print(f"({current.data})")
        current = current.link


if __name__ == "__main__":
    head = build(5)
    explore(head)
    for node in head:
        print(node.data)

