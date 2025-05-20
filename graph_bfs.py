from collections import deque

class Vertex:
    def __init__(self, data: int) -> None:
        self.data = data
        self.link: Vertex | None = None

    def __repr__(self):
        return f"{self.data}"
    
class Edge:
    def __init__(self, v1: int | None = None, v2: int | None = None) -> None:
        self.v1 = v1
        self.v2 = v2
        self.link_v1: Edge | None = None
        self.link_v2: Edge | None = None
    def __repr__(self):
        return f"{self.v1, self.v2}"    


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
        queue = deque()

        if not (0 <= first < self.len_verts): 
            return ret

        queue.append(first) 
        visit[first] = True 
        while queue:
            v = queue.popleft() 
            ret.append(v) 

            temp = self.arr[v].link
            nei_arr = []
            while temp:
                nei_arr.append(temp.data)
                temp = temp.link
            
           
            for neighbor in sorted(nei_arr):
                if not visit[neighbor]:
                    visit[neighbor] = True 
                    queue.append(neighbor) 
        return ret


# if __name__ == "__main__":
#     vertices: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}
#     edges: set[tuple[int, int]] = {
#     (0, 1),
#     (2, 0),
#     (2, 6),
#     (1, 3),
#     (1, 4),
#     (2, 5),
#     (7, 3),
#     (4, 7),
#     (5, 7),
#     (6, 7),
#     }
#     graph = GraphUndirectedListAdj(vertices)
#     for u, v in sorted(edges):
#         graph.insert_edge(u, v)
#     print(f"graph:\n{graph}")
#     print(f"graph.total_edges = {graph.total_edges()}")
#     print()
#     actions = graph.traverse(0)
#     print(f"graph.traversal:\n{actions}")

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
    graph = GraphUndirectedListAdjMultiple(vertices)
    for u, v in sorted(edges):
        print(f"graph.insert_edge({u}, {v})")
        graph.insert_edge(u, v)
    print()
    print(f"graph:")
    for i in range(len(vertices)):
        path = graph.explore(i)
        print(f"vertex[{i}]: path = {path}")
    actions = graph.traverse(0) # bfs
    print(f"actions = {actions}")
    print()    
