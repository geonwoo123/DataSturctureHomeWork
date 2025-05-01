class TreeNode:
    def __init__(self, key: int | str) -> None:
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
    def __repr__(self) -> str:
        return f"{self.key!r}"
    

class TreeBinaryBuilder:
    @staticmethod
    def build(sexpr: list[int | str]) -> TreeNode | None:
        stack: list[TreeNode] = []
        add = lambda node: node if node.key != "#" else None
        root = None
        for token in sexpr:
            if token != ")":
                stack.append(TreeNode(token))
                continue
            root_ = None
            while stack[-1].key != "(":
                node = stack.pop()
                if not root_:
                    root_ = node
                    continue
                right, root_ = root_, TreeNode("")
                root_.left, root_.right = add(node), add(right)
            stack.pop()
            if not stack:
                return root_
            assert root_
            root = stack.pop()
            root_.key = root.key
            stack.append(root_)
        return root
    
class TreeBinarySearch:
    def __init__(self, root: TreeNode | None = None) -> None:
        self.root: TreeNode | None = None
        self.root = root
    def search(self, key: int) -> TreeNode | None:
        # root = self.root
        # while root and key != int(root.key):
        #     root = root.left if key < int(root.key) else root.right
        # return root    
        
        def search_recursive(root: TreeNode | None) -> TreeNode | None:
            if not root:
                return
            if key == int(root.key):
                return root
            root = (search_recursive(root.left) if key < int(root.key) else search_recursive(root.right))
            return root
        return search_recursive(self.root)
    
    def insert(self, key:int):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return

        cur = self.root
        while True:
            if key == cur.key:
                return 
            elif key < cur.key:
                if cur.left is None:
                    cur.left = node
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    return
                cur = cur.right

    def delete(self, key: int) -> None:
        def delete_recursive(root: TreeNode | None, key: int) -> TreeNode | None:
            if root == None:
                return None
            if key < int(root.key):
                root.left = delete_recursive(root.left, key)
            elif key > int(root.key):
                root.right = delete_recursive(root.right, key)
            else:
                if root.left == None and root.right is None:
                    return None
                if root.left == None:
                    return root.right
                if root.right == None:
                    return root.left
                check = root.right
                while check.left:
                    check = check.left
                root.key = check.key
                root.right = delete_recursive(root.right, check.key)
            return root

        self.root = delete_recursive(self.root, key)

            
               



    def traverse(self) -> list[TreeNode]:
        if not self.root:
            return []
        ret: list[TreeNode] = []
        stack: list[TreeNode] = []
        root = self.root
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root)
            root = root.right
        return ret
    
if __name__ == "__main__":
    tree = TreeBinarySearch()
    elems = [40, 20, 60, 10, 30, 50, 70, 45, 55, 52]
    for i in elems:
        tree.insert(i)
    actions = tree.traverse()
    print(actions)
    n = 60
    print(f"node_deleted = {n}")
    tree.delete(n)
    actions = tree.traverse()
    print(actions)
    n = 40
    print(f"node_deleted = {n}")
    tree.delete(n)
    actions = tree.traverse()
    print(actions)
    
    


# if __name__ == "__main__":
#     tree = TreeBinarySearch()
#     elems = [30, 5, 40, 2, 80, 80, 35, 5]
#     for i in elems:
#         tree.insert(i)
#     actions = tree.traverse()
#     print(actions)

# if __name__ == "__main__":
#     sexpr = "( 44 ( 17 ( # 32 ( 28 ( # 29 ) # ) ) 88 ( 65 ( 54 82 ( 76 ( #80 ) # ) ) 97 ) ) )".split()
#     sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
#     root = TreeBinaryBuilder.build(sexpr)
#     tree = TreeBinarySearch(root)
#     for elem in (25, 76, 97):
#         node = tree.search(elem)
#         print(f"search ({elem}) = {node}")