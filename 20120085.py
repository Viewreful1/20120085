from bisect import bisect


def input_by_int():
    return map(int, input().split())


class Vertex:
    def __init__(self, number):
        self._edges = list()
        self._keys = list()
        self._number = number
        self.is_visited = False

    def connect(self, vertex):
        if vertex not in self._edges:
            key = bisect(self._keys, vertex.number)
            self._keys.insert(key, vertex.number)
            self._edges.insert(key, vertex)

    @property
    def edges(self):
        return tuple(self._edges)

    @property
    def number(self):
        return self._number


N, M, V = input_by_int()

vertices = [Vertex(i) for i in range(N)]

for _ in range(M):
    start, end = map(lambda x: x - 1, input_by_int())

    vertices[start].connect(vertices[end])
    vertices[end].connect(vertices[start])


def initialize_vertices(vertices):
    for vertex in vertices:
        vertex.is_visited = False


def dfs(start_vertex):
    initialize_vertices(vertices)

    def _dfs(vertex):
        vertex.is_visited = True

        print(str(vertex.number + 1), end=' ')

        for next_vertex in vertex.edges:
            if next_vertex.is_visited is not True:
                _dfs(next_vertex)

    _dfs(start_vertex)
    print()


def bfs(start_vertex):
    from queue import Queue

    initialize_vertices(vertices)
    visit_queue = Queue()

    start_vertex.is_visited = True
    visit_queue.put(start_vertex)

    while not visit_queue.empty():
        now_vertex = visit_queue.get()

        print(str(now_vertex.number + 1), end=' ')

        for next_vertex in now_vertex.edges:
            if next_vertex.is_visited is not True:
                next_vertex.is_visited = True
                visit_queue.put(next_vertex)

    print()


dfs(vertices[V - 1])
bfs(vertices[V - 1])
