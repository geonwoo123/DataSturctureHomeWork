class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self):
        return f"{self.data}"


class GraphUndirectedListAdj:
    def __init__(self, vertices: set[int]) -> None:
        self.len_verts = len(vertices)
        self.arr: list[Vertex] = [Vertex(v) for v in sorted(vertices)]

    def insert_edge(self, u: int, v: int) -> None:
        if not (0 <= u < self.len_verts and 0 <= v < self.len_verts):
            return

        vertex = self.arr[u]
        while vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(v)

        vertex = self.arr[v]
        while vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(u)

    def delete_edge(self, u: int, v: int) -> None:
        if not (0 <= u < self.len_verts and 0 <= v < self.len_verts):
            return

        prev = vertex = self.arr[u]
        while vertex and vertex.data != v:
            prev, vertex = vertex, vertex.link

        if vertex:
            prev.link = vertex.link

        prev = vertex = self.arr[v]
        while vertex and vertex.data != u:
            prev, vertex = vertex, vertex.link

        if vertex:
            prev.link = vertex.link

    def total_edges(self) -> int:
        edges = 0
        for vertex in self.arr:
            temp = vertex.link
            while temp:
                edges += 1
                temp = temp.link
        return edges // 2

    def __repr__(self) -> str:
        ret = ""
        for vertex in self.arr:
            ret += f"[{vertex.data:2d}]"
            temp = vertex.link
            out = []
            while temp:
                out.append(str(temp.data))
                temp = temp.link
            if out:
                ret += " " + ", ".join(out)
            ret += "\n"
        return ret.rstrip()

    def traverse(self, first: int) -> list[int]:
        visit = [False] * self.len_verts
        ret = []
        stack = [first]
        while stack:
            v = stack.pop()
            if not visit[v]:
                visit[v] = True
                ret.append(v)
                temp = self.arr[v].link
                nei_arr = []
                while temp:
                    nei_arr.append(temp.data)
                    temp = temp.link
                for i in sorted(nei_arr, reverse = True):
                    if not visit[i]:
                        stack.append(i)
        return ret                    


if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}
    edges: set[tuple[int, int]] = {
        (0, 1),
        (2, 0),
        (2, 6),
        (1, 3),
        (1, 4),
        (2, 5),
        (7, 3),
        (4, 7),
        (5, 7),
        (6, 7),
    }
    graph = GraphUndirectedListAdj(vertices)
    for u, v in sorted(edges):
        graph.insert_edge(u, v)

    print(f"graph:\n{graph}")
    print(f"graph.total_edges = {graph.total_edges()}")
    print()
    actions = graph.traverse(0)
    print("graph.traversal:")
    print(actions)
