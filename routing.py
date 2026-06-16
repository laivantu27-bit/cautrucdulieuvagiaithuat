import heapq

# --- 1.1. Shortest Path - Dijkstra ---
def build_graph(edges):
    graph = {}
    for u, v, cost in edges:
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost)) # Đồ thị vô hướng
    return graph

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, parent

def shortest_route(graph, source, target):
    dist, parent = dijkstra(graph, source)
    if dist[target] == float('inf'):
        return float('inf'), []
    
    route = []
    curr = target
    while curr is not None:
        route.append(curr)
        curr = parent[curr]
    route.reverse()
    return dist[target], route

def demo_routing_shortest_path():
    edges = [("WH1", "WH2", 10), ("WH1", "HCM", 50), ("WH2", "HN", 40), 
             ("HCM", "DN", 20), ("HN", "DN", 30), ("WH2", "HCM", 15)]
    graph = build_graph(edges)
    source, target = "WH1", "DN"
    cost, route = shortest_route(graph, source, target)
    print(f"--- Demo Routing (Dijkstra) ---")
    print(f"Tuyến đường ngắn nhất từ {source} đến {target}: {' -> '.join(route)}")
    print(f"Tổng chi phí: {cost}\n")

# --- 1.2. MST – Kruskal + DSU ---
class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.size = {v: 1 for v in vertices}
        
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v]) # Path compression
        return self.parent[v]
        
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            return True
        return False

def kruskal_mst(vertices, edges):
    dsu = DSU(vertices)
    edges.sort(key=lambda x: x[2]) # Sort theo chi phí
    mst = []
    total_cost = 0
    
    for u, v, cost in edges:
        if dsu.union(u, v):
            mst.append((u, v, cost))
            total_cost += cost
    return mst, total_cost

def demo_mst_network():
    vertices = ["WH1", "WH2", "HCM", "HN", "DN"]
    edges = [("WH1", "WH2", 10), ("WH1", "HCM", 50), ("WH2", "HN", 40), 
             ("HCM", "DN", 20), ("HN", "DN", 30), ("WH2", "HCM", 15)]
    mst, total_cost = kruskal_mst(vertices, edges)
    print(f"--- Demo MST (Kruskal) ---")
    print("Danh sách đường truyền được chọn:")
    for u, v, c in mst: print(f"  {u} - {v}: {c}")
    print(f"Tổng chi phí lắp đặt: {total_cost}")
    print("Nhận xét: Đây là bộ khung tối thiểu, các tuyến giao hàng chi tiết dùng Dijkstra trên mạng này.\n")