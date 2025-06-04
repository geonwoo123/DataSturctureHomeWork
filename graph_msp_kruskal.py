class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: 'Vertex' | None = None

    def __repr__(self) -> str:
        return f"({self.data})"


class Edge:
    def __init__(self, u: 'Vertex', v: 'Vertex', w: int) -> None:
        self.u = u
        self.v = v
        self.w = w
    def __repr__(self) -> str:
        return f"({self.u}, {self.v}, {self.w})"


class GraphUndirectedListAdj:
    def __init__(self, vertices: set[int]) -> None:
        self.len_verts = len(vertices)
        self.arr: list[Vertex] = [Vertex(v) for v in sorted(vertices)]

        # For Union-Find
        self.parent = list(range(self.len_verts))

        # For Kruskal's algorithm
        self.edges: list[Edge] = []

    def insert_edge(self, u: int, v: int, w: int) -> None:
        if not (0 <= u < self.len_verts and 0 <= v < self.len_verts):
            return

        vertex = self.arr[u]
        while vertex and vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(v)

        vertex = self.arr[v]
        while vertex and vertex.link:
            vertex = vertex.link
        vertex.link = Vertex(u)

        # For Kruskal's algorithm
        self.edges.append(Edge(self.arr[u], self.arr[v], w))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        self.parent[yroot] = xroot
        return True

    def kruskal(self) -> list[Edge]:
        edges: list[Edge] = []
        self.parent = list(range(self.len_verts))  # Union-Find 초기화
        self.edges.sort(key=lambda x: x.w)
        for edge in self.edges:
            if self.union(edge.u.data, edge.v.data):
                edges.append(edge)
            if len(edges) == self.len_verts - 1:
                break
        return edges

    def __repr__(self) -> str:
        ret = ""
        for i, vt in enumerate(self.arr):
            ret += f"[{i}] -> "
            if not vt or not vt.link:
                ret += "None\n"
                continue
            vt = vt.link
            while vt is not None:
                ret += f"({vt}), "
                vt = vt.link
            ret += "\n"
        return ret

if __name__ == "__main__":
    vertices: set[int] = {0, 1, 2, 3, 4, 5, 6}
    edges: set[tuple[int, int, int]] = {
    (0, 1, 28),
    (0, 5, 10),
    (1, 2, 16),
    (1, 6, 14),
    (2, 3, 12),
    (3, 6, 18),
    (3, 4, 22),
    (4, 5, 25),
    (4, 6, 24),
    }
    graph = GraphUndirectedListAdj(vertices)
    for u, v, w in sorted(edges):
        print(f"graph.insert_edge({u}, {v}, {w})")
        graph.insert_edge(u, v, w)
    print()
    print(f"graph:\n{graph}")
    actions = graph.kruskal()
    print("MST Kruskal's algorithm:")
    cost = 0
    for n, edge in enumerate(actions):
        print(f"{n}: {edge}")
        cost += edge.w
    print(f"total cost = {cost}")        