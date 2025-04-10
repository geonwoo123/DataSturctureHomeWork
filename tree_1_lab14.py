from typing import List, Optional
from typing_extensions import LiteralString

class Tree:
    class Node:
        def __init__(self, data: str) -> None:
            self.data = data
            self.left_child: Optional["Tree.Node"] = None 
            self.right_sibling: Optional["Tree.Node"] = None

        def __repr__(self) -> str:
            return f"{self.data}"

    def __init__(self):
        self.root: Optional["Tree.Node"] = None

    def build(self, sexpr: List[LiteralString]) -> Optional["Tree.Node"]:
        stack: List[Tree.Node] = []
        current: Optional[Tree.Node] = None
               
        for token in sexpr:
            if token == "(":
                stack.append(current)
            elif token == ")":
                stack.pop()
            else:
                node = Tree.Node(token)
                if not self.root:
                    self.root = node
                else:
                    parent = stack[-1]
                    if not parent.left_child:
                        parent.left_child = node
                    else:
                        sibling = parent.left_child
                        while sibling.right_sibling:
                            sibling = sibling.right_sibling
                        sibling.right_sibling = node                
                current = node
        return self.root


def display_tree(tree: Tree) -> None:
    if not tree.root:
        return

    stack = [(tree.root, "", True)]
    
    while stack:
        node, prefix, is_last = stack.pop()

        connect = ""
        if prefix != "":
            connect = "└── " if is_last else "├── "
        print(prefix + connect + node.data)

        children = []
        child = node.left_child
        while child:
            children.append(child)
            child = child.right_sibling



        for i in reversed(range(len(children))):
            new_prefix = prefix + ("    " if is_last else "│   ")
            stack.append((children[i], new_prefix, i == len(children) - 1))


def print_tree(tree: Tree) -> None: 
    def print_tree(node: Optional[Tree.Node], tag: str = "", last: bool = True, root: bool = True) -> None:
        if node is None:
            return

        print(f"{node}" if root else f"{tag}{'└──' if last else '├──'} {node}")
        child = node.left_child
        while child:
            node = child.right_sibling 
            print_tree(child, tag=f"{tag}{'    ' if last else '│   '}", last=(node is None), root=False)
            child = node 
    print_tree(tree.root)


if __name__ == "__main__":
    expr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    tree = Tree()
    tree.build(expr.split())
    print_tree(tree) # recursive
    print()
    display_tree(tree) # iterative