#bài 1 :Phần A
def topological_sort_dfs(graph):
    """
    Topological Sort sử dụng DFS (post-order)
    """
    #if has_cycle_directed(graph):
    #return None

    visited = set()
    stack = []

    def dfs(vertex):
        """DFS helper với post-order"""
        # Đánh dấu visited
        visited.add(vertex)

        # Duyệt neighbors
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)

        # Thêm vào stack sau khi đã thăm hết các đỉnh kề (post-order)
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]

print("\n=== Test Topological Sort ===")
dag_graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
result = topological_sort_dfs(dag_graph)
print(f"Topological Sort: {result}")

#Phần B
from collections import deque

def can_finish(num_courses, prerequisites):
    """
    Kiểm tra có thể hoàn thành tất cả môn học không?
    """

    graph = {i: [] for i in range(num_courses)}
    in_degree = {i: 0 for i in range(num_courses)}
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        curr = queue.popleft()
        count += 1
        
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count == num_courses

print(can_finish(2, [[1, 0]]))        
print(can_finish(2, [[1, 0], [0, 1]]))  

# Phần c
from collections import deque
def can_finish(num_courses, prerequisites):
    """
    Kiểm tra có thể hoàn thành tất cả môn học không?
    """

    graph = {i: [] for i in range(num_courses)}
    in_degree = {i: 0 for i in range(num_courses)}
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        curr = queue.popleft()
        count += 1

        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count == num_courses

print(f"Có thể hoàn thành (2 môn, 1->0): {can_finish(2, [[1, 0]])}")          
print(f"Có thể hoàn thành (2 môn, 0<->1): {can_finish(2, [[1, 0], [0, 1]])}")


# Bài 2
def find_order(num_courses, prerequisites):
    """
    Tìm thứ tự học hợp lệ sử dụng thuật toán Kahn
    """

    graph = {i: [] for i in range(num_courses)}
    in_degree = {i: 0 for i in range(num_courses)}
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        curr = queue.popleft()
        order.append(curr)
        
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []

print("\n=== Test Course Schedule ===")
n1 = 4
prereqs1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(f"Order 1: {find_order(n1, prereqs1)}") 

n2 = 2
prereqs2 = [[1, 0], [0, 1]]
print(f"Order 2: {find_order(n2, prereqs2)}")