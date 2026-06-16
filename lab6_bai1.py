import heapq

def dijkstra(graph, source):
    """
    Dijkstra: tìm đường đi ngắn nhất từ source đến tất cả các đỉnh.
    """
    # Bước 1: Khởi tạo khoảng cách là vô cực
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    parent = {v: None for v in graph}
    
    # Priority queue: (khoảng_cách, đỉnh)
    pq = [(0, source)]
    visited = set()

    while pq:
        # Lấy đỉnh có khoảng cách nhỏ nhất
        current_dist, u = heapq.heappop(pq)

        # Nếu đã xử lý u rồi thì bỏ qua
        if u in visited:
            continue
        visited.add(u)

        # Thử nới lỏng (relaxation) các hàng xóm
        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, parent

def reconstruct_path(parent, target):
    """Truy vết ngược từ target về source để lấy đường đi."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    return path[::-1] # Đảo ngược danh sách

# --- Test với đồ thị của bạn ---
graph = {
    'A': [('B', 4), ('D', 1)],
    'B': [('A', 4), ('C', 2), ('E', 3)],
    'C': [('B', 2), ('F', 5)],
    'D': [('A', 1), ('E', 2)],
    'E': [('D', 2), ('B', 3), ('F', 1)],
    'F': [('E', 1), ('C', 5)]
}

distances, parent = dijkstra(graph, 'A')

print("Khoảng cách ngắn nhất từ A:")
for vertex, dist in distances.items():
    print(f"Đến {vertex}: {dist}")

target = 'F'
print(f"\nĐường đi ngắn nhất từ A đến {target}: {reconstruct_path(parent, target)}")
def reconstruct_path(parent, source, target):
    """
    Dựng lại đường đi từ source đến target dùng mảng parent.
    """
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    
    path.reverse()
    
    # Kiểm tra đường đi có tồn tại và bắt đầu đúng từ source
    if not path or path[0] != source:
        return None
    return path

def print_distances(distances, source):
    print(f"Bảng khoảng cách từ {source}:")
    for v in sorted(distances.keys()):
        d = distances[v]
        if d == float('inf'):
            print(f"  {source} → {v}: INF (không tới được)")
        else:
            print(f"  {source} → {v}: {d}")

def test_dijkstra():
    # Đồ thị đã định nghĩa trước đó
    graph = {
        'A': [('B', 4), ('D', 1)],
        'B': [('A', 4), ('C', 2), ('E', 3)],
        'C': [('B', 2), ('F', 5)],
        'D': [('A', 1), ('E', 2)],
        'E': [('D', 2), ('B', 3), ('F', 1)],
        'F': [('E', 1), ('C', 5)]
    }

    source = 'A'
    distances, parent = dijkstra(graph, source)

    print_distances(distances, source)
    
    print("\nĐường đi chi tiết:")
    for v in sorted(graph.keys()):
        if v == source:
            continue
        path = reconstruct_path(parent, source, v)
        if path is None:
            print(f"  {source} → {v}: không có đường đi")
        else:
            cost = distances[v]
            print(f"  {source} → {v}: {' → '.join(path)} (cost = {cost})")

if __name__ == "__main__":
    test_dijkstra()