from typing import List, Optional
from typing_extensions import LiteralString

class TreeBinary: 
    class Node:
        def __init__(self, data: Optional[str] = None):
            self.data = data
            self.left: Optional["TreeBinary.Node"] = None
            self.right: Optional["TreeBinary.Node"] = None

        def __repr__(self):
            return f"{self.data}"

    def __init__(self) -> None:
        self.root: Optional[TreeBinary.Node] = None

    def build(self, sexpr: list[str]) -> None:
        stack: list[TreeBinary.Node] = []
        add = lambda node: node if node.data != "#" else None

        for token in sexpr:
            if token != ")":
                stack.append(self.Node(token))
                continue

            root = None
            while stack[-1].data != "(":
                node = stack.pop() 
                if not root:
                    root = node
                    continue

                right, root = root, self.Node(None)
                root.left, root.right = add(node), add(right)

            stack.pop()

            if not stack:
                self.root = root
                return

            assert root
            root_ = stack.pop()
            root.data = root_.data
            stack.append(root)

def print_tree(tree: Optional[TreeBinary]) -> None: 
    def print_tree(
        node: Optional[TreeBinary.Node], tag="", root=True, left=True
    ) -> None:
        if not node:
            return

        print(f"{node}" if root else f"{tag}{'├──' if left else '└──'} {node}")
        left_ = node.left if node.left else TreeBinary.Node("#")
        right_ = node.right if node.right else TreeBinary.Node("#")

        if not node.left and not node.right:
            return

        tag = "" if root else f"{tag}{'│ ' if left else ' '}"
        print_tree(left_, tag, False, True)
        print_tree(right_, tag, False, False)

    if not tree:
        return
    print_tree(tree.root)

if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( 30 ( 5 ( # 2 ) 40 ( 80 # ) ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( D ( H I ) E ) C ( F G ) ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( # D ) # ) )".split())
    print_tree(tree)

    tree.build("( A ( B ( C ( D ( E # ) # ) # ) # ) )".split())
    print_tree(tree)