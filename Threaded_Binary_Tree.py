class TreeNodeThreaded:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.threaded_check = False

class TreeBinary:
    def __init__(self) -> None:
        self.root: TreeNodeThreaded | None = None

    def build(self, sexpr: list[str]) -> None:
        stack: list[TreeNodeThreaded] = []
        add = lambda node: node if node.data != "#" else None
        for token in sexpr:
            if token != ")":
                stack.append(TreeNodeThreaded(token))
                continue
            root = None
            while stack[-1].data != "(":
                node = stack.pop()
                if not root:
                    root = node
                    continue
                right, root = root, TreeNodeThreaded(None)
                root.left, root.right = add(node), add(right)
            stack.pop()
            if not stack:
                self.root = root
                return
            assert root
            root_ = stack.pop()
            root.data = root_.data
            stack.append(root)

class TreeBinaryThreadedBuilder:
    @staticmethod
    def build(root: TreeNodeThreaded | None) -> TreeNodeThreaded:
        head = TreeNodeThreaded()
        head.left, head.right = root, head

        def inorder_recursive(node, prev):
            if not node:
                return prev
            prev = inorder_recursive(node.left, prev)
            if prev and not prev.right:
                prev.right = node
                prev.threaded_check = True
            prev = node
            return inorder_recursive(node.right, prev)
        inorder_recursive(root, None)
        return head

class TreeBinaryThreaded:
    def __init__(self, head: TreeNodeThreaded) -> None:
        self.head = head

    def find_successor(self, root: TreeNodeThreaded) -> TreeNodeThreaded | None:
        if root.threaded_check:
            return root.right 
        node = root.right
        while node and node.left:
            node = node.left
        return node

    def traverse_inorder(self) -> list[str]:
        ret = []
        node = self.head.left
        while node and node.left:
            node = node.left
        while node:
            ret.append(node.data)
            node = self.find_successor(node)
        return ret

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    tree_binary = TreeBinary()
    tree_binary.build(sexpr)

    head = TreeBinaryThreadedBuilder.build(tree_binary.root)
    tree = TreeBinaryThreaded(head)

    actions = tree.traverse_inorder()
    print(actions)
