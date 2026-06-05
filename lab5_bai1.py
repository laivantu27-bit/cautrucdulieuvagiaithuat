#hàm 1
def build_graph(edges, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh
    Input:
    edges: list của các tuple (u, v) đại diện cho cạnh
    directed: True nếu đồ thị có hướng, False nếu vô hướng

    Output:
    graph: dictionary với key là đỉnh, value là list các đỉnh kề
    """
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
print("=== Test 1: Đồ thị vô hướng ===")
edges1 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]
graph1 = build_graph(edges1, directed=False)
print("Đồ thị vô hướng:")
for vertex, neighbors in graph1.items():
    print(f"  {vertex}: {neighbors}")
print("\n=== Test 2: Đồ thị có hướng ===")
edges2 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]
graph2 = build_graph(edges2, directed=True)
print("Đồ thị có hướng:")
for vertex, neighbors in graph2.items():
    print(f"  {vertex}: {neighbors}")



#hàm 2
from collections import deque
def bfs(graph, start):
    """
    BFS - Duyệt đồ thị theo chiều rộng

    Chiến lược:
    1. Dùng Queue để lưu các đỉnh cần thăm
    2. Dùng Set để đánh dấu đã thăm
    3. Lặp: Lấy đỉnh từ queue, thăm, thêm neighbors chưa thăm vào queue

    Input:
    graph: dictionary biểu diễn đồ thị
    start: đỉnh bắt đầu

    Output:
    result: list các đỉnh theo thứ tự duyệt
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            # Nếu chưa thăm, đánh dấu và thêm vào queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
print("\n=== Test BFS ===")
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
result = bfs(graph, 'A')
print(f"BFS từ A: {result}")
result2 = bfs(graph, 'D')
print(f"BFS từ D: {result2}")



#hàm 3
def dfs_recursive(graph, start, visited=None, result=None):
    """
    DFS - Duyệt đồ thị theo chiều sâu (đệ quy)

    Chiến lược:
    1. Đánh dấu đỉnh hiện tại là visited
    2. Thêm vào kết quả
    3. Với mỗi neighbor chưa visited, đệ quy DFS
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(start)
    result.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    return result
print("\n=== Test DFS Recursive ===")
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
result = bfs_result = dfs_recursive(graph, 'A')
print(f"DFS từ A: {result}")
result2 = dfs_recursive(graph, 'C')
print(f"DFS từ C: {result2}")

#hàm 4
from collections import deque

def count_connected_components(graph):
    """
    Đếm số connected components trong đồ thị

    Chiến lược:
    1. Duyệt tất cả các đỉnh
    2. Với mỗi đỉnh chưa visited:
       - Chạy BFS từ đỉnh đó
       - Tất cả đỉnh được thăm tạo thành 1 component
    3. Số lần chạy BFS = số components
    """
    visited = set()
    components = []

    def bfs_component(start):
        """BFS helper để tìm một component"""
        queue = deque([start])
        visited.add(start)
        component = []
        while queue:
            vertex = queue.popleft()
            component.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return component

    for vertex in graph:
        if vertex not in visited:
            component = bfs_component(vertex)
            components.append(component)

    return len(components), components
print("\n=== Test Connected Components ===")
print("Test 1: 1 component")
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
count1, comps1 = count_connected_components(graph1)
print(f"Số components: {count1}")
for i, comp in enumerate(comps1, 1):
    print(f"  Component {i}: {comp}")
print("\nTest 2: 3 components")
graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['C'],
    'F': [],
}

count2, comps2 = count_connected_components(graph2)
print(f"Số components: {count2}")
for i, comp in enumerate(comps2, 1):
    print(f"  Component {i}: {comp}")