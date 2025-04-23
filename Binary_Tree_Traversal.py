class TreeBinary:
    class Node:
        def __init__(self, data: str | None = None):
            self.data = data
            self.left: TreeBinary.Node | None = None
            self.right: TreeBinary.Node | None = None

        def __repr__(self) -> str:
            return f"{self.data!r}"

    def __init__(self) -> None:
        self.root: TreeBinary.Node | None = None

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

def print_tree(tree: TreeBinary | None) -> None: 
    def print_tree(node: TreeBinary.Node | None, tag="", root=True, left=True ) -> None:
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

def traverse(tree: TreeBinary | None) -> list[TreeBinary.Node]:
        
    if not tree:
        return []

    ret: list[TreeBinary.Node] = []
    stack: list[TreeBinary.Node] = []
    root: TreeBinary.Node | None = tree.root
         
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        ret.append(cur)
        cur = cur.right
    return ret        
    

if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( + ( * ( * ( / ( A B ) C ) D ) E ) )".split())
    print_tree(tree)
    actions = traverse(tree)
    print(actions)