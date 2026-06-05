#Phần A
def has_cycle_undirected(graph):
    """
    Phát hiện chu trình trong đồ thị vô hướng
    """
    visited = set()
    def dfs(vertex, parent):
        """
        DFS helper:
        vertex: đỉnh hiện tại
        parent: đỉnh cha (đỉnh đã đi qua để tới vertex)
        """
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False
print("=== Test Cycle Detection - Undirected ===")
graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(f"Test 1 (có chu trình): {has_cycle_undirected(graph1)}")

graph2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print(f"Test 2 (không có chu trình): {has_cycle_undirected(graph2)}") 

graph3 = {
    0: [1],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3]
}
print(f"Test 3 (nhiều components, có chu trình): {has_cycle_undirected(graph3)}") 

#Phần B
def has_cycle_directed(graph):
    """
    Phát hiện chu trình trong đồ thị có hướng
    Sử dụng three-color approach
    
    WHITE: Chưa thăm
    GRAY: Đang xử lý (trong recursion stack)
    BLACK: Đã xử lý xong
    """
    WHITE, GRAY, BLACK = 0, 1, 2

    color = {vertex: WHITE for vertex in graph}

    def dfs(vertex):
        """DFS helper với three-color"""

        color[vertex] = GRAY

        for neighbor in graph[vertex]:
            if color[neighbor] == GRAY:
                return True
            
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True


        color[vertex] = BLACK
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False

print("\n=== Test Cycle Detection - Directed ===")

graph1 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print(f"Test 1 (có chu trình A→B→C→A): {has_cycle_directed(graph1)}") 

graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print(f"Test 2 (DAG): {has_cycle_directed(graph2)}") 

graph3 = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['C']
}
print(f"Test 3 (cross edge, không có chu trình): {has_cycle_directed(graph3)}") 

#Phần C
def compare_cycle_detection():
    """
    So sánh cycle detection giữa đồ thị vô hướng và có hướng
    """
    print("\n" + "="*60)
    print("SO SÁNH CYCLE DETECTION")
    print("="*60)

    print("\n[1] ĐỒ THỊ VÔ HƯỚNG:")
    undirected = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    result_u = has_cycle_undirected(undirected)
    print(f"  Đồ thị vô hướng (A-B-C-A): {'Có' if result_u else 'Không'} chu trình")

    print("\n[2] ĐỒ THỊ CÓ HƯỚNG:")

    directed = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    result_d = has_cycle_directed(directed)
    print(f"  Đồ thị có hướng (A->B->C->A): {'Có' if result_d else 'Không'} chu trình")

    print("\n[3] SO SÁNH:")
    print("  - Vô hướng: Sử dụng DFS + tham số 'parent' để tránh ghi nhận cạnh ngược trở lại là chu trình.")
    print("  - Có hướng: Sử dụng kỹ thuật Three-color (WHITE/GRAY/BLACK) để xác định 'back edge'.")
    print("  - Độ phức tạp: Cả hai đều đạt O(V + E), trong đó V là số đỉnh và E là số cạnh.")

compare_cycle_detection()