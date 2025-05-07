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

    # def preorder(tree: TreeBinary | None) -> list[TreeBinary.Node]:
    #     if not tree or not tree.root:
    #         return []

    #     ret: list[TreeBinary.Node] = []
    #     stack: list[TreeBinary.Node] = [tree.root]

    #     while stack:
    #         node = stack.pop()
    #         ret.append(node)

    #         # 오른쪽을 먼저 넣어야 왼쪽이 먼저 나오므로
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)

    #     return ret


    # def postorder(tree: TreeBinary | None) -> list[TreeBinary.Node]:
    #     if not tree or not tree.root:
    #         return []

    #     ret: list[TreeBinary.Node] = []
    #     stack1: list[TreeBinary.Node] = [tree.root]
    #     stack2: list[TreeBinary.Node] = []

    #     while stack1:
    #         node = stack1.pop()
    #         stack2.append(node)
    #         if node.left:
    #             stack1.append(node.left)
    #         if node.right:
    #             stack1.append(node.right)

    #     while stack2:
    #         ret.append(stack2.pop())

    #     return ret 
            
    

if __name__ == "__main__":
    tree = TreeBinary()
    tree.build("( + ( * ( * ( / ( A B ) C ) D ) E ) )".split())
    print_tree(tree)
    actions = traverse(tree)
    print(actions)