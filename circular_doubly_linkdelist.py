from typing import Optional

class Node:
    def __init__(self,data: Optional[int] = None, ) -> None:
        self.data = data
        self.rlink: Optional["Node"] = self
        self.llink: Optional["Node"] = self

    def __repr__(self) -> str:
        return f"{self.data}"


class ListLinkedDoublyCircular: 
    """Circular Doubly Linked List"""
    def __init__(self) -> None:
        self.head_node = Node()
        self.head_node.rlink = self.head_node
        self.head_node.llink = self.head_node

    def empty(self):
        return self.head_node.rlink == self.head_node
    
    def head(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.head_node.rlink.data

    def tail(self) -> Optional[Node]:
        if self.empty():
            return None
        return self.head_node.llink.data

    def insert_head(self, data) -> None:
        new_node = Node(data) #새 노드 하나 만들어주고
        first = self.head_node.rlink
        new_node.rlink = first
        new_node.llink = self.head_node
        self.head_node.rlink = new_node
        first.llink = new_node

    def insert_tail(self, data) -> None:
        new_node = Node(data)
        last = self.head_node.llink
        new_node.rlink = self.head_node
        new_node.llink = last
        last.rlink = new_node
        self.head_node.llink = new_node

    def insert(self, tgt: int, data: int) -> None:
        """target node 뒤에 insert 한다."""
        curr = self.head_node.rlink
        while curr != self.head_node:
            if curr.data == tgt:
                new_node = Node(data)
                next_node = curr.rlink
                new_node.rlink = next_node
                new_node.llink = curr
                curr.rlink = new_node
                next_node.llink = new_node
                return
            curr = curr.rlink

    def delete(self, tgt: int) -> None:
        """target node 를 삭제한다."""
        curr = self.head_node.rlink
        while curr != self.head_node:
            if curr.data == tgt:
                prev_node = curr.llink
                next_node = curr.rlink
                prev_node.rlink = next_node
                next_node.llink = prev_node
                return
            curr = curr.rlink

    def __repr__(self) -> str:
        result = []
        curr = self.head_node.rlink
        while curr != self.head_node:
            result.append(curr.data)
            curr = curr.rlink
        return f"{result}"

def info(list_: ListLinkedDoublyCircular) -> None:
    print(f"list{list_.head(), list_.tail()} = {list_}")


if __name__ == "__main__":
    llist = ListLinkedDoublyCircular()
    info(llist)
    llist.insert_tail(30)
    info(llist)
    llist.insert_tail(40)
    info(llist)
    llist.insert_head(20)
    info(llist)
    llist.delete(20)
    info(llist)
    llist.delete(40)
    info(llist)
    llist.insert_head(20)
    info(llist)
    llist.insert(30, 40)
    info(llist)
    llist.insert_tail(50)
    info(llist)
    llist.insert(30, 35)
    info(llist)
    llist.insert(20, 25)
    info(llist)
    llist.delete(20)
    info(llist)
    llist.delete(25)
    info(llist)
